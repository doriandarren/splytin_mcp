import os
from dotenv import load_dotenv
from gen.helpers.helper_menu import pause
from gen.helpers.helper_print import input_with_validation
from gen.services.generator_services import create_php_project_service


load_dotenv()


def start_project_php():
    
    # Defaults
    default_path = os.getenv("DEFAULT_PATH_PHP")    
    default_name = "api.app1.com"

    # Inputs
    project_name = input_with_validation(
        f"Nombre del proyecto",
        default_name
    )
    project_path = input_with_validation(
        f"Ruta del proyecto",
        default_path
    )

    create_php_project_service(project_name, project_path)
    
    pause()
    
