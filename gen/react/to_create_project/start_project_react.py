import os
from gen.helpers.helper_menu import pause
from gen.helpers.helper_print import RED, dd, print_message, GREEN, CYAN, input_with_validation
from gen.services.generator_services import create_react_project_service



def start_project_react():
    
    # Defaults
    default_path = "/Users/dorian/ReactProjects"
    default_name = "app1.com"

    # Inputs
    project_name = input_with_validation(
        f"Nombre del proyecto",
        default_name
    )
    project_path = input_with_validation(
        f"Ruta del proyecto",
        default_path
    )

    result = create_react_project_service(project_name, project_path)

    # Mensaje final
    print_message(f"¡Proyecto React creado exitosamente en {result['full_path']}!", GREEN)
    print_message(f"Para empezar: cd {result['full_path']} && npm run dev", CYAN)
    


    pause()
