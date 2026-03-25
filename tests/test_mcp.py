import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]


def send(proc: subprocess.Popen, payload: dict) -> None:
    assert proc.stdin is not None
    proc.stdin.write(json.dumps(payload) + "\n")
    proc.stdin.flush()


def recv(proc: subprocess.Popen) -> dict:
    assert proc.stdout is not None
    line = proc.stdout.readline()
    if not line:
        raise RuntimeError("El servidor MCP cerró stdout antes de responder.")
    return json.loads(line)


proc = subprocess.Popen(
    [sys.executable, str(ROOT / "mcp_server.py")],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True,
    cwd=str(ROOT),
)

try:
    send(
        proc,
        {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "initialize",
            "params": {"protocolVersion": "2024-11-05"},
        },
    )
    init_response = recv(proc)
    assert init_response["id"] == 1
    assert init_response["result"]["serverInfo"]["name"] == "project-generator-mcp"

    send(proc, {"jsonrpc": "2.0", "id": 2, "method": "tools/list"})
    tools_response = recv(proc)
    tools = tools_response["result"]["tools"]
    tool_names = {tool["name"] for tool in tools}
    assert "create_python_django_project" in tool_names
    assert "create_python_django_crud" in tool_names
    assert "create_react_project" in tool_names
    assert "create_php_project" in tool_names

    send(proc, {"jsonrpc": "2.0", "id": 3, "method": "ping"})
    ping_response = recv(proc)
    assert ping_response == {"jsonrpc": "2.0", "id": 3, "result": {}}

    send(
        proc,
        {
            "jsonrpc": "2.0",
            "id": 4,
            "method": "tools/call",
            "params": {"name": "tool_inexistente", "arguments": {}},
        },
    )
    invalid_tool_response = recv(proc)
    assert invalid_tool_response["id"] == 4
    assert invalid_tool_response["result"]["isError"] is True
    content_text = invalid_tool_response["result"]["content"][0]["text"]
    assert "Herramienta no soportada" in content_text
finally:
    assert proc.stdin is not None
    proc.stdin.close()
    return_code = proc.wait(timeout=5)
    if return_code != 0:
        stderr = ""
        if proc.stderr is not None:
            stderr = proc.stderr.read()
        raise RuntimeError(f"El servidor MCP terminó con código {return_code}: {stderr}")


print("MCP smoke test OK")
