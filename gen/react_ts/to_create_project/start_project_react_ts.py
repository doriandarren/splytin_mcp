import os
from dotenv import load_dotenv
from gen.helpers.helper_menu import pause
from gen.helpers.helper_print import input_with_validation
from gen.react_ts.to_create_project.react_ts_command_line import ReactTsCommandLine
from gen.react_ts.to_create_project.react_ts_module_auth import ReactTsModuleAuth
from gen.react_ts.to_create_project.react_ts_react_router import ReactTsReactRouter

load_dotenv()


class StartProjectReactTs:
    def invoke(self):
        # Defaults
        default_path = os.getenv("DEFAULT_PATH_PROJECT_REACT_TS")
        default_name = os.getenv("DEFAULT_PROJECT_NAME_REACT_TS")

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
        
        
        
        
        
        # Command Line
        obj = ReactTsCommandLine()
        obj.invoke(full_path)
        
        
        # Create Module Auth
        obj = ReactTsModuleAuth()
        obj.invoke(full_path)
        
        # Create Module Home
        
        
        
        # React Router
        obj = ReactTsReactRouter()
        obj.invoke(full_path)
        
        

        pause()
