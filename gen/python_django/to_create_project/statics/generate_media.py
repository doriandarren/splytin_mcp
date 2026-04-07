import os
from gen.python_django.helpers.helper_file import helper_add_import, helper_append_content
from gen.helpers.helper_print import print_message, GREEN, CYAN



def generate_media(full_path, project_name_format, app_main, venv_python):
    create_media(full_path, project_name_format, app_main, venv_python)
    update_settings(full_path, project_name_format, app_main)
    update_urls(full_path, project_name_format, app_main)




def create_media(full_path, project_name_format, app_main, venv_python):
    """
    Genera el archivo
    """

    folder_path = os.path.join(full_path, "media")
    os.makedirs(folder_path, exist_ok=True)

    print_message(f"Carpeta generado: {folder_path}", GREEN)




def update_settings(full_path, project_name_format, app_main):
    
    str = r"""
# Media files
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"
"""
    
    helper_append_content(
        full_path, 
        f"{app_main}/settings.py", 
        str
    )
    
    

def update_urls(full_path, project_name_format, app_main):
    
    helper_add_import(
        full_path, 
        f"{app_main}/urls.py", 
        f"from django.conf import settings"
    )  
    
    
    helper_add_import(
        full_path, 
        f"{app_main}/urls.py", 
        f"from django.conf.urls.static import static"
    )  
    
    
    str = r"""

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
"""
    
    helper_append_content(
        full_path, 
        f"{app_main}/urls.py", 
        str
    )
    