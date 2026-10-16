import os
from dotenv import load_dotenv
from helpers.helper_menu import pause
from helpers.helper_print import input_with_validation

load_dotenv()


def start_project_react_ts():
    
    # Defaults
    default_path = os.getenv("DEFAULT_PATH_PROJECT_REACT")
    default_name = os.getenv("DEFAULT_PROJECT_NAME_REACT")

    # Inputs
    project_name = input_with_validation(
        f"Nombre del proyecto",
        default_name
    )
    project_path = input_with_validation(
        f"Ruta del proyecto",
        default_path
    )

    # Join Full Path
    full_path = f"{project_path}/{project_name}"
    
    # TODO llamadas a las funciones "generate_"
    # generate_by_command_line(full_path)

    pause()
