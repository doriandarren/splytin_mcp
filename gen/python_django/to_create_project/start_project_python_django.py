import os
from dotenv import load_dotenv
from gen.helpers.helper_print import input_with_validation
from gen.helpers.helper_menu import pause
from gen.helpers.helpers import dd
from gen.python_django.helpers.helper_data_fake import HelperDataFake
from gen.services.generator_services import create_python_django_project_service


load_dotenv()



def start_project_python_django():
    
    # Defaults
    default_project_name = os.getenv("DEFAULT_PROJECT_NAME_DJANGO")
    default_path = os.getenv("DEFAULT_PATH_PROJECT_DJANGO")
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
    
    
    ## TODO borrar luego solo para PRuebas:
    full_path = f"{project_path}/{project_name}"
    HelperDataFake.createCRUD(full_path, app_name)
    
    

    pause()

