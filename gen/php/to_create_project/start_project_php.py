from gen.helpers.helper_menu import pause
from gen.helpers.helper_print import input_with_validation
from gen.services.generator_services import create_php_project_service



def start_project_php():
     # Defaults
    default_path = "/Users/dorian/PhpstormProjects81"
    default_name = "app-1"

    # Inputs
    project_name = input_with_validation(
        f"Nombre del proyecto (defecto: {default_name}): ",
        default_name
    )
    project_path = input_with_validation(
        f"Ruta del proyecto (defecto: {default_path}): ",
        default_path
    )

    create_php_project_service(project_name, project_path)
    
    pause()
    
