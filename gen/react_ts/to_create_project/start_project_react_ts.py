import os
from dotenv import load_dotenv
from gen.helpers.helper_menu import pause
from gen.helpers.helper_print import input_with_validation
from gen.react_ts.to_create_project.components.react_ts_component_public import ReactTsComponentPublic
from gen.react_ts.to_create_project.components.react_ts_custom_components import ReactTsCustomComponents
from gen.react_ts.to_create_project.modules.react_ts_module_dashboard import ReactTsModuleDashboard
from gen.react_ts.to_create_project.react_ts_api import ReactTsApi
from gen.react_ts.to_create_project.react_ts_chadcn import ReactTsChadcn
from gen.react_ts.to_create_project.react_ts_command_line import ReactTsCommandLine
from gen.react_ts.to_create_project.modules.react_ts_module_auth import ReactTsModuleAuth
from gen.react_ts.to_create_project.modules.react_ts_module_home import ReactTsModuleHome
from gen.react_ts.to_create_project.react_ts_env import ReactTsEnv
from gen.react_ts.to_create_project.react_ts_gitignore import ReactTsGitignore
from gen.react_ts.to_create_project.react_ts_google_fonts import ReactTsGoogleFonts
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
        
        
        # Env
        obj = ReactTsEnv()
        obj.invoke(full_path)
        
        
        # Gitignore
        obj = ReactTsGitignore()
        obj.invoke(full_path)
        
    
        
        
        # Module Auth
        obj = ReactTsModuleAuth()
        obj.invoke(full_path)
        
        
        # Components Public
        obj = ReactTsComponentPublic()
        obj.invoke(full_path)
        
        # Module Home
        obj = ReactTsModuleHome()
        obj.invoke(full_path)
        
        
        
        
        # Components Custom
        obj = ReactTsCustomComponents()
        obj.invoke(full_path)
        
        
        # Module Dashboard
        obj = ReactTsModuleDashboard()
        obj.invoke(full_path)
        
        
        
        
        
        # React Router
        obj = ReactTsReactRouter()
        obj.invoke(full_path)
        
        
        # Chadcn/ ui
        obj = ReactTsChadcn()
        obj.invoke(full_path)
        
        
        # Google Fonts
        obj = ReactTsGoogleFonts()
        obj.invoke(full_path, project_name)
        
        
        # API
        obj = ReactTsApi()
        obj.invoke(full_path)
        
        

        

        pause()
