
import os
from gen.helpers.helper_print import print_message, GREEN, CYAN



def add_route_api_php(
    full_path,
    namespace,
    version_api,
    project_name,
    singular_name,
    plural_name,
    singular_name_camel,
    plural_name_camel,
    singular_name_kebab,
    plural_name_kebab,
    singular_name_snake,
    plural_name_snake,
    columns
):
    """
    Actualiza el archivo
    """
    main_path = os.path.join(full_path, "routes", "api.php")

    # Verificar si el archivo existe
    if not os.path.exists(main_path):
        print_message(f"Error: {main_path} no existe.", CYAN)
        return

    try:
        # Leer el contenido del archivo
        with open(main_path, "r") as f:
            content = f.read()

        # Reemplazos
        content = content.replace(
            f"""    // API
    // ...
""",
            f"""    // API
    // ...
    require base_path('routes/{namespace}/{version_api}/{plural_name_snake}.php');
"""
        )

        # Escribir el contenido actualizado
        with open(main_path, "w") as f:
            f.write(content)

        print_message(
            f"{main_path} actualizado correctamente.",
            GREEN
        )

    except Exception as e:
        print_message(
            f"Error al actualizar {main_path}: {e}",
            CYAN
        )

    