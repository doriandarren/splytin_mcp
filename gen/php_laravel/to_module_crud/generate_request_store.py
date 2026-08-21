import os
from gen.helpers.helper_print import print_message, GREEN, CYAN

def generate_request_store(
    full_path,
    namespace,
    project_name,
    singular_name,
    plural_name,
    singular_name_kebab,
    plural_name_kebab,
    singular_name_snake,
    plural_name_snake,
    columns
):
    """
    Genera el archivo
    """

    folder_path = os.path.join(full_path, "src", "components", "")
    file_path = os.path.join(folder_path, ".jsx")

    os.makedirs(folder_path, exist_ok=True)

    content = f'''
    ## TODO Content
'''

    try:
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)
