## Project

## MCP

Este repositorio ya incluye un servidor MCP por `stdio` en [`mcp_server.py`](/Users/dorian/PythonProjects/splytin_mcp/mcp_server.py).

### Ejecutar

```sh
python3 cli.py
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

{
  "mcpServers": {
    "project-generator": {
      "command": "/Users/dorian/PythonProjects/splytin_mcp/.venv/bin/python",
      "args": [
        "/Users/dorian/PythonProjects/splytin_mcp/mcp_server.py"
      ]
    }
  }
}
```

```json
{
  "mcpServers": {
    "project-generator": {
      "command": "python3",
      "args": ["/Users/milena/workspaces/WorkSpacePython/PROJECTS/splytin_mcp"]
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
python -m pip install --upgrade pip


## Instala los requerimientos:
python -m pip list
python -m pip check                                     # Comprobar posibles incompatibilidades
python -m pip freeze > requirements.txt                 # Crear archivo requerimientos -> Respaldo / Export
python -m pip install -r requirements.txt               # Instalar requerimientos Restore / Import

# Si No se tiene el archivo: requirements.txt
pip install pipreqs                             # Install
pipreqs . --force                               # Ejecutar

```

## Libraries gen

```sh


# Console / Terminal
python -m pip install questionary        # Menús interactivos
python -m pip install colorama           # Colores en terminal

# HTTP / API
python -m pip install requests           # Peticiones HTTP y APIs

# Scheduling / Cronjobs
python -m pip install schedule           # Tareas programadas

# Utilities
python -m pip install inflect            # Singularización y pluralización
python -m pip install python-dotenv      # Variables de entorno (.env)
python -m pip install json5              # Lectura de JSON y JSONC

# Database / ORM
python -m pip install sqlalchemy         # ORM para bases de datos
python -m pip install alembic            # Migraciones de bases de datos
python -m pip install psycopg2-binary    # PostgreSQL
python -m pip install pymysql            # MySQL / MariaDB


```

## Flujo del proyecto

```sh
## Para proyectos (to_create_project)
pymain -> pystart -> pystartproject -> pygenerate

## Para modulos (to_create_module_crud)
pymain -> pystart -> pystartmodule -> pystandard -> pygenerate
```


