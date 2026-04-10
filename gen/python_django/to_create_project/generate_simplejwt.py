import os
from gen.helpers.helper_print import print_message, GREEN, CYAN, run_command
from gen.python_django.helpers.helper_file import helper_add_import, helper_append_content, helper_update_list

def generate_simplejwt(full_path, project_name_format, app_main, venv_python):
    install_simplejwt(full_path, venv_python)
    add_settings(full_path, app_main)



def install_simplejwt(full_path, venv_python):
    print_message("Instalando djangorestframework-simplejwt...", CYAN)
    run_command(f'"{venv_python}" -m pip install djangorestframework-simplejwt', cwd=full_path)
    print_message("djangorestframework-simplejwt instalado correctamente.", GREEN)
    




def add_settings(full_path, app_main):
    
    helper_add_import(full_path, f"{app_main}/settings.py", "import datetime")
    
    
    str = f"""\n# Simple JWT and Rest Framework
REST_FRAMEWORK = {{
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    "DEFAULT_RENDERER_CLASSES": [
        "rest_framework.renderers.JSONRenderer",
    ],
}}
    """
    
    
    helper_append_content(
        full_path, 
        f"{app_main}/settings.py", 
        str
    )
    
    
    str = """SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': datetime.timedelta(days=120), ## Controla el tiempo de expiración del token
}
    """
    
    helper_append_content(
        full_path, 
        f"{app_main}/settings.py",
        str
    )
    
    print_message("Simple JWT configurado correctamente.", GREEN)