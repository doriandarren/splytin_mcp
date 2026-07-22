import os
from helpers.helper_print import print_message, GREEN, CYAN



def update_role_user_model(full_path):
    """
    Genera el archivo
    """
    main_jsx_path = os.path.join(full_path, "app", "Models", "SHARED", "RoleUsers", "RoleUser.php")

    # Verificar si el archivo existe
    if not os.path.exists(main_jsx_path):
        print_message(f"Error: {main_jsx_path} no existe.", CYAN)
        return

    try:

        # Leer el contenido del archivo
        with open(main_jsx_path, "r") as f:
            content = f.read()
        

        ## Replace
        content = content.replace(
            r"""protected $table = 'role_users';""",
            r"""protected $table = 'role_user';"""
        )



        # Escribir el contenido actualizado
        with open(main_jsx_path, "w") as f:
            f.write(content)

        print_message("use User Models correctamente.", GREEN)

    except Exception as e:
        print_message(f"Error al actualizar {main_jsx_path}: {e}", CYAN)




