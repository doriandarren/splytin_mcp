from gen.helpers.helper_print import input_with_validation
from gen.helpers.helper_menu import pause
from gen.services.generator_services import create_python_django_project_service


def start_project_python_django():
    
    # Defaults
    default_path = "/Users/dorian/PythonProjects"
    default_project_name = "app1.com"
    default_app_name = "main"

    # Inputs
    project_name = input_with_validation(
        f"Nombre del proyecto",
        default_project_name
    )
    project_path = input_with_validation(
        f"Ruta del proyecto",
        default_path
    )
    
    app_name = input_with_validation(
        f"Nombre de la aplicación principal",
        default_app_name
    )

    create_python_django_project_service(project_name, project_path, app_name)

    pause()
