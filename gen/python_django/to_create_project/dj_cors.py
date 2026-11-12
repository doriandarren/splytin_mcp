import os
from helpers.helper_print import print_message, GREEN, CYAN, run_command
from gen.python_django.helpers.helper_dj_file import helper_append_content, helper_insert_after_line, helper_replace_block, helper_update_list




class DjCors:
    

    def invoke(self, full_path, project_name_format, app_main, venv_python):
        """
        Genera el archivo
        """
        self.install_cors(full_path, venv_python)
        self.update_settings(full_path, project_name_format, app_main)
        
        
        
        
    def install_cors(self, full_path, venv_python):
        print_message("Instalando django-cors-headers...", CYAN)
        run_command(f'"{venv_python}" -m pip install django-cors-headers', cwd=full_path)
        print_message("django-cors-headers instalado correctamente.", GREEN)
        

    def update_settings(self, full_path, project_name_format, app_main):
        
        helper_update_list(
            full_path, 
            f"{app_main}/settings.py", 
            "INSTALLED_APPS", 
            f"'corsheaders',                      # required for cors"
        )
        
        helper_insert_after_line(
            full_path,
            f"{app_main}/settings.py",
            "    'django.middleware.security.SecurityMiddleware',",
            "    'corsheaders.middleware.CorsMiddleware',"
        )
        
        helper_append_content(
            full_path, 
            f"{app_main}/settings.py", 
            "\n## CORS"
        )
        
        helper_append_content(
            full_path, 
            f"{app_main}/settings.py", 
            'CORS_ALLOW_ALL_ORIGINS = os.getenv("CORS_ALLOW_ALL_ORIGINS", "False").lower() == "true"'
        )
    
        helper_append_content(
            full_path, 
            f"{app_main}/settings.py", 
            "CORS_ALLOW_CREDENTIALS = False"
        )
        
        print_message("settings.py actualizado correctamente.", GREEN)
   