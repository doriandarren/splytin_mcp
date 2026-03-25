from __future__ import annotations

import contextlib
import io
import json
import sys
import traceback
from typing import Any

from gen.services import (
    create_php_project_service,
    create_python_django_crud_service,
    create_python_django_project_service,
    create_react_project_service,
)


SERVER_INFO = {
    "name": "project-generator-mcp",
    "version": "0.1.0",
}
PROTOCOL_VERSION = "2024-11-05"


class CapturedToolError(Exception):
    def __init__(self, original: Exception, logs: str, trace: str):
        super().__init__(str(original))
        self.original = original
        self.logs = logs
        self.trace = trace


def _read_message() -> tuple[dict[str, Any] | None, bool]:
    line = sys.stdin.readline()
    if not line:
        return None, True
    line = line.strip()
    if not line:
        return None, False
    return json.loads(line), False


def _send(message: dict[str, Any]) -> None:
    sys.stdout.write(json.dumps(message, ensure_ascii=False) + "\n")
    sys.stdout.flush()


def _response(message_id: Any, result: dict[str, Any]) -> dict[str, Any]:
    return {"jsonrpc": "2.0", "id": message_id, "result": result}


def _error(message_id: Any, code: int, message: str, data: Any = None) -> dict[str, Any]:
    payload: dict[str, Any] = {
        "jsonrpc": "2.0",
        "id": message_id,
        "error": {"code": code, "message": message},
    }
    if data is not None:
        payload["error"]["data"] = data
    return payload


def _tool_result(payload: dict[str, Any], logs: str = "", is_error: bool = False) -> dict[str, Any]:
    text = json.dumps(payload, indent=2, ensure_ascii=False)
    if logs.strip():
        text = f"{text}\n\nLogs:\n{logs.strip()}"
    result: dict[str, Any] = {
        "content": [{"type": "text", "text": text}],
    }
    if is_error:
        result["isError"] = True
    return result


def _call_with_capture(handler, arguments: dict[str, Any]) -> tuple[dict[str, Any], str]:
    stdout_buffer = io.StringIO()
    stderr_buffer = io.StringIO()
    try:
        with contextlib.redirect_stdout(stdout_buffer), contextlib.redirect_stderr(stderr_buffer):
            result = handler(**arguments)
    except Exception as exc:
        logs = "\n".join(part for part in [stdout_buffer.getvalue(), stderr_buffer.getvalue()] if part.strip())
        raise CapturedToolError(exc, logs, traceback.format_exc()) from exc

    logs = "\n".join(part for part in [stdout_buffer.getvalue(), stderr_buffer.getvalue()] if part.strip())
    return result, logs


def _tools() -> list[dict[str, Any]]:
    return [
        {
            "name": "create_python_django_project",
            "description": "Crea un proyecto Django usando los generadores actuales del repositorio.",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "project_name": {"type": "string"},
                    "project_path": {"type": "string"},
                    "app_name": {"type": "string", "default": "main"},
                },
                "required": ["project_name", "project_path"],
                "additionalProperties": False,
            },
        },
        {
            "name": "create_python_django_crud",
            "description": "Crea un módulo CRUD Django dentro de un proyecto existente.",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "full_path": {"type": "string"},
                    "app_main": {"type": "string"},
                    "singular_name": {"type": "string"},
                    "plural_name": {"type": "string"},
                    "columns": {
                        "oneOf": [
                            {"type": "string"},
                            {"type": "array", "items": {"type": "object"}},
                        ]
                    },
                    "components": {"type": "array", "items": {"type": "string"}},
                },
                "required": ["full_path", "app_main", "singular_name", "plural_name", "columns"],
                "additionalProperties": False,
            },
        },
        {
            "name": "create_react_project",
            "description": "Crea un proyecto React basado en Vite usando los generadores actuales.",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "project_name": {"type": "string"},
                    "project_path": {"type": "string"},
                },
                "required": ["project_name", "project_path"],
                "additionalProperties": False,
            },
        },
        {
            "name": "create_php_project",
            "description": "Crea un proyecto Laravel/PHP usando los generadores actuales.",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "project_name": {"type": "string"},
                    "project_path": {"type": "string"},
                },
                "required": ["project_name", "project_path"],
                "additionalProperties": False,
            },
        },
    ]


TOOL_HANDLERS = {
    "create_python_django_project": create_python_django_project_service,
    "create_python_django_crud": create_python_django_crud_service,
    "create_react_project": create_react_project_service,
    "create_php_project": create_php_project_service,
}


def _handle_initialize(message_id: Any, params: dict[str, Any]) -> dict[str, Any]:
    requested_protocol = params.get("protocolVersion") or PROTOCOL_VERSION
    return _response(
        message_id,
        {
            "protocolVersion": requested_protocol,
            "capabilities": {"tools": {}},
            "serverInfo": SERVER_INFO,
        },
    )


def _handle_tools_list(message_id: Any) -> dict[str, Any]:
    return _response(message_id, {"tools": _tools()})


def _handle_tools_call(message_id: Any, params: dict[str, Any]) -> dict[str, Any]:
    tool_name = params.get("name")
    arguments = params.get("arguments") or {}

    handler = TOOL_HANDLERS.get(tool_name)
    if handler is None:
        return _response(
            message_id,
            _tool_result({"error": f"Herramienta no soportada: {tool_name}"}, is_error=True),
        )

    try:
        result, logs = _call_with_capture(handler, arguments)
        return _response(message_id, _tool_result(result, logs=logs))
    except CapturedToolError as exc:
        return _response(
            message_id,
            _tool_result(
                {
                    "error": str(exc.original),
                    "tool": tool_name,
                },
                logs="\n\n".join(part for part in [exc.logs, exc.trace] if part.strip()),
                is_error=True,
            ),
        )
    except Exception as exc:
        trace = traceback.format_exc()
        return _response(
            message_id,
            _tool_result(
                {
                    "error": str(exc),
                    "tool": tool_name,
                },
                logs=trace,
                is_error=True,
            ),
        )


def main() -> int:
    while True:
        try:
            message, should_exit = _read_message()
            if should_exit:
                return 0
            if message is None:
                continue

            method = message.get("method")
            message_id = message.get("id")
            params = message.get("params") or {}

            if method == "initialize":
                _send(_handle_initialize(message_id, params))
            elif method == "notifications/initialized":
                continue
            elif method == "tools/list":
                _send(_handle_tools_list(message_id))
            elif method == "tools/call":
                _send(_handle_tools_call(message_id, params))
            elif method == "ping":
                _send(_response(message_id, {}))
            elif message_id is not None:
                _send(_error(message_id, -32601, f"Método no soportado: {method}"))
        except json.JSONDecodeError as exc:
            _send(_error(None, -32700, "JSON inválido", {"detail": str(exc)}))
        except KeyboardInterrupt:
            return 0
        except Exception as exc:
            _send(_error(None, -32603, "Error interno del servidor", {"detail": str(exc)}))


if __name__ == "__main__":
    raise SystemExit(main())
