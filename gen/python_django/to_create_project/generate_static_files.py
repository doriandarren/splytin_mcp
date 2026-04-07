import os
from gen.helpers.helper_print import print_message, GREEN, CYAN
from gen.python_django.helpers.helper_file import helper_append_content, helper_replace_block



def generate_static_files(full_path, app_main):
    """
    Genera el archivo
    """
    create_static_files(full_path, app_main)
    create_folder(full_path)



def create_static_files(full_path, app_main):
    
    str = r"""
# Static files
STATIC_URL = "/static/"
STATICFILES_DIRS = [
    BASE_DIR / "static",
]
STATIC_ROOT = BASE_DIR / "staticfiles"
"""
    
    helper_append_content(
        full_path,
        f"{app_main}/settings.py",
        str
    )
    


def create_folder(full_path):
    
    ## Folder static
    folder_path = os.path.join(full_path, "static", "images")
    os.makedirs(folder_path, exist_ok=True)
    print_message(f"Carpeta uploads creada", GREEN)


    ## Folder staticfiles
    folder_path = os.path.join(full_path, "staticfiles")
    os.makedirs(folder_path, exist_ok=True)
    print_message(f"Carpeta staticfiles creada", GREEN)