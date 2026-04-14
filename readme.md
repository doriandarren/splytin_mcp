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
pip install --upgrade pip


## Instala los requerimientos:
pip list
pip freeze > requirements.txt                  # Crear archivo requerimientos -> Respaldo / Export
pip install -r requirements.txt                # Instalar requerimientos Restore / Import

# Si No se tiene el archivo: requirements.txt
pip install pipreqs                             # Install
pipreqs . --force                               # Ejecutar

```

## Libraries gen

```sh

pip install questionary                                      # Console / Terminal
pip install colorama                                         # Console / Terminal
pip install requests                                         # Conexion API
pip install schedule                                         # Cronjobs
pip install inflect                                          # Pluralize

pip install sqlalchemy psycopg2-binary alembic python-dotenv  # DB
pip install pymysql                                           # DB

```

## Flujo del proyecto

```sh
## Para proyectos (to_create_project)
pymain -> pystart -> pystartproject -> pygenerate

## Para modulos (to_create_module_crud)
pymain -> pystart -> pystartmodule -> pystandard -> pygenerate
```

# Pasos:

```sh
1. crear carpeta proyecto "xxx" y archivo "_ _ init _ _.py" y el archivo: "main_xxx"
2. crear carpetas con sus respectivos archivos "_ _ init _ _.py":

   - "to_create_module_crud"
   - "to_create_project"

3. crear dentro de la carpeta "to_create_project" el archivo: start_project_xxx.py
4. crear dentro de la carpeta "to_create_module_crud" el archivo: start_module_xxx.py

```

# Format Example -> columns

```sh
[{'name': 'user_id', 'type': 'fk', 'is_fk': True, 'related_table': 'users', 'related_model': 'User'}, {'name': 'name', 'type': 'string', 'is_fk': False}, {'name': 'age', 'type': 'integer', 'is_fk': False}, {'name': 'description', 'type': 'string', 'is_fk': False}]
```

# Ejemplo: CRUD

```sh

/Users/dorian/PythonProjects/python.generator
main
AgendaUnloading
AgendaUnloadings
[{'name': 'user_id', 'type': 'fk', 'is_fk': True, 'related_table': 'users', 'related_model': 'User'}, {'name': 'name', 'type': 'string', 'is_fk': False}, {'name': 'age', 'type': 'integer', 'is_fk': False}, {'name': 'description', 'type': 'string', 'is_fk': False}]
['api_route', 'api_serializer', 'api_wiewset', 'api_model', 'api_service']

```

# TODOS:

PYTHON:

- las cors: 'corsheaders.middleware.CorsMiddleware', # required for cors,
  va encima de: 'django.middleware.common.CommonMiddleware',

- En PHP: cuando se crea un proyecto, se tiene que cambiar en el ".env" y en el ".env.example" lo siguientes: "LOG_CHANNEL=daily"
- en el archivo para API de postman hay que agregar en el Dev: el "execute"

