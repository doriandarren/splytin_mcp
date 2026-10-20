import os
from gen.helpers.helper_print import print_message, GREEN, CYAN, RED, run_command



def generate_djangorestframework_jsonapi(full_path, venv_python, app_main):
    install(full_path, venv_python)
    update_file_settings_installed_apps(full_path, app_main)
    update_file_settings_rest_framework(full_path, app_main)




def install(full_path, venv_python):
    print_message("Instalando djangorestframework-jsonapi...", CYAN)
    run_command(f'"{venv_python}" -m pip install djangorestframework-jsonapi', cwd=full_path)
    print_message("djangorestframework-jsonapi instalado correctamente.", GREEN)




def update_file_settings_installed_apps(full_path, app_main):
    """
    Actualiza el archivo settings.py
    """
    main_path = os.path.join(full_path, app_main, "settings.py")

    # Verificar si el archivo existe
    if not os.path.exists(main_path):
        print_message(f"Error: {main_path} no existe.", CYAN)
        return False

    try:
        # Leer el contenido del archivo
        with open(main_path, "r", encoding="utf-8") as f:
            content = f.read()

        # Reemplazos
        replacements = {
            ## KEY : VALUE
            """    'rest_framework',                   # required for DRF,""":
            """    'rest_framework',                   # required for DRF,
    'rest_framework_json_api',          # required JSON API,""",
        }

        # Validar y aplicar los reemplazos
        new_content = content

        for old_text, new_text in replacements.items():
            if old_text not in new_content:
                raise ValueError(f"No se encontró el texto esperado: {old_text}")

            new_content = new_content.replace(old_text, new_text, 1)

        if new_content == content:
            raise ValueError("No se realizó ningún reemplazo.")

        # Escribir el contenido actualizado
        with open(main_path, "w", encoding="utf-8") as f:
            f.write(new_content)

        print_message(
            f"{main_path} actualizado correctamente. ----------------------------****************",
            GREEN
        )

        return True

    except Exception as e:
        print_message(
            f"Error al actualizar {main_path}: {e}",
            RED
        )
        return False

    






def update_file_settings_rest_framework(full_path, app_main):
    """
    Actualiza el archivo settings.py
    """
    main_path = os.path.join(full_path, app_main, "settings.py")

    # Verificar si el archivo existe
    if not os.path.exists(main_path):
        print_message(f"Error: {main_path} no existe.", CYAN)
        return False

    try:
        # Leer el contenido del archivo
        with open(main_path, "r", encoding="utf-8") as f:
            content = f.read()

        # Reemplazos
        replacements = {
            ## New Item -> KEY : VALUE
            """# Rest Framework
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    ),
    "DEFAULT_RENDERER_CLASSES": [
        "rest_framework.renderers.JSONRenderer",
    ],
}""":
            """# Django REST Framework - Token + JSON:API
REST_FRAMEWORK = {
    # Authentication
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.TokenAuthentication",
    ],

    # JSON:API - Responses
    "DEFAULT_RENDERER_CLASSES": [
        "rest_framework_json_api.renderers.JSONRenderer",
    ],

    # JSON:API - Requests
    "DEFAULT_PARSER_CLASSES": [
        "rest_framework_json_api.parsers.JSONParser",
    ],

    # JSON:API - Metadata
    "DEFAULT_METADATA_CLASS":
        "rest_framework_json_api.metadata.JSONAPIMetadata",

    # JSON:API - Exceptions
    "EXCEPTION_HANDLER":
        "rest_framework_json_api.exceptions.exception_handler",
}
""",
        }

        # Validar y aplicar los reemplazos
        new_content = content

        for old_text, new_text in replacements.items():
            if old_text not in new_content:
                raise ValueError(f"No se encontró el texto esperado: {old_text}")

            new_content = new_content.replace(old_text, new_text, 1)

        if new_content == content:
            raise ValueError("No se realizó ningún reemplazo.")

        # Escribir el contenido actualizado
        with open(main_path, "w", encoding="utf-8") as f:
            f.write(new_content)

        print_message(
            f"{main_path} actualizado correctamente.",
            GREEN
        )

        return True

    except Exception as e:
        print_message(
            f"Error al actualizar {main_path}: {e}",
            RED
        )
        return False

    








if __name__ == '__main__':
    
    ## Data Fake
    full_path = '/Users/dorian/PythonProjects'  + '/api.app1.com'
    venv = '/Users/dorian/PythonProjects/api.app1.com/.venv/bin/python' 
    main = 'main'
    
    generate_djangorestframework_jsonapi(full_path, venv, main)
