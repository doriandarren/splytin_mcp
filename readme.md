## Project

## MCP

Este repositorio ya incluye un servidor MCP por `stdio` en [`mcp_server.py`](/Users/dorian/PythonProjects/splytin_mcp/mcp_server.py).

### Ejecutar

```sh
python3 mcp_server.py
```

### Tools disponibles

- `create_python_django_project`
- `create_python_django_crud`
- `create_react_project`
- `create_php_project`

### Ejemplo de configuración MCP

```json
{
  "mcpServers": {
    "project-generator": {
      "command": "python3",
      "args": ["/Users/dorian/PythonProjects/splytin_mcp/mcp_server.py"]
    }
  }
}
```

### Smoke test local

```sh
python3 tests/test_mcp.py
```

### Notas

- El CLI interactivo actual sigue funcionando.
- El MCP usa la misma lógica de generación, pero sin menús ni `input()`.
- Si vas a ejecutar generadores reales, necesitarás tener instaladas las dependencias del proyecto y las herramientas externas que cada stack use, por ejemplo `python3`, `npm` o `composer`.

## Crear entorno virtual

```sh
## Entorno virtual MacOs
python3 -m venv .venv
source .venv/bin/activate                     # Activar entorno
deactivate                                    # Desactivar entorno

## Entorno virtual Windows
py -m venv .venv                               # Windows
.\.venv\Scripts\activate                       # Windows
py -m pip install --upgrade pip                # Windows
deactivate                                     # Desactivar
py -m pip xxx                                  # Usar este comando para instrucciones

## Actualizar
python3 -m pip install --upgrade pip


## Instala los requerimientos:
pip list
python3 -m pip install -r requirements.txt      # Instalar requerimientos

# Si No se tiene el archivo: requirements.txt
pip install pipreqs                             # Install
pipreqs . --force                               # Ejecutar


## Instalar paquetes
pip3 freeze                                     # Ver Paquetes instalados
py -m pip freeze                                # Para Windows
pip3 install requests                           # Conexion API
pip3 install schedule                           # CronJobs


## Si no funciona VSCode:
( Cmd + Shift + P ) -> luego "Python: Select Interpreter" elegir ".venv/bin/python"
```
