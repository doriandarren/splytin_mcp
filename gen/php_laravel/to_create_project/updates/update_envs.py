import os
from gen.helpers.helper_print import print_message, GREEN, CYAN



def update_envs(full_path, project_name, domain_name):
    update_env(full_path, project_name, domain_name)
    update_env_example(full_path, project_name, domain_name)



def update_env(full_path, project_name, domain_name):
    """
    Actualiza el archivo
    """
    main_path = os.path.join(full_path, ".env")

    # Verificar si el archivo existe
    if not os.path.exists(main_path):
        print_message(f"Error: {main_path} no existe.", CYAN)
        return

    try:

        # Leer el contenido del archivo
        with open(main_path, "r") as f:
            content = f.read()


        # Replace
        content = content.replace(
            r"""APP_NAME=Laravel""",
            r"""APP_NAME=__DOMAIN_NAME__Local"""
        )
        
        content = content.replace('__DOMAIN_NAME__', domain_name)


        content = content.replace(
            r"""DB_CONNECTION=sqlite""",
            r"""DB_CONNECTION=database

# DEFAULT
DB_CONNECTION=mysql
DB_HOST=host.docker.internal
DB_PORT=3306
DB_DATABASE=api_integrations
DB_USERNAME=
DB_PASSWORD=

# API
DB_CONNECTION_API=api
DB_HOST_API=host.docker.internal
DB_PORT_API=3306
DB_DATABASE_API=api_integrations
DB_USERNAME_API=
DB_PASSWORD_API=

# SHARED
DB_CONNECTION_SHARED=shared
DB_HOST_SHARED=host.docker.internal
DB_PORT_SHARED=3306
DB_DATABASE_SHARED=api_integrations
DB_USERNAME_SHARED=
DB_PASSWORD_SHARED=
"""
        )

        content = content.replace(
            f"""APP_URL=http://localhost:8000""",
            f"""APP_URL=http://{domain_name}

MESSAGE_CHANNEL_URL="""
        )


        content = content.replace(
            f"""LOG_CHANNEL=stack""",
            f"""LOG_CHANNEL=daily"""
        )


        # Escribir el contenido actualizado
        with open(main_path, "w") as f:
            f.write(content)

        print_message("use User Models correctamente.", GREEN)

    except Exception as e:
        print_message(f"Error al actualizar {main_path}: {e}", CYAN)
        





def update_env_example(full_path, project_name, domain_name):
    """
    Actualiza el archivo
    """
    main_path = os.path.join(full_path, ".env.example")

    # Verificar si el archivo existe
    if not os.path.exists(main_path):
        print_message(f"Error: {main_path} no existe.", CYAN)
        return

    try:

        # Leer el contenido del archivo
        with open(main_path, "r") as f:
            content = f.read()


        # Replace
        content = content.replace(
            r"""APP_NAME=Laravel""",
            r"""APP_NAME=__DOMAIN_NAME__Local"""
        )
        
        content = content.replace('__DOMAIN_NAME__', domain_name)


        content = content.replace(
            r"""DB_CONNECTION=sqlite""",
            r"""DB_CONNECTION=database

# DEFAULT
DB_CONNECTION=mysql
DB_HOST=host.docker.internal
DB_PORT=3306
DB_DATABASE=api_integrations
DB_USERNAME=
DB_PASSWORD=

# API
DB_CONNECTION_API=api
DB_HOST_API=host.docker.internal
DB_PORT_API=3306
DB_DATABASE_API=api_integrations
DB_USERNAME_API=
DB_PASSWORD_API=

# SHARED
DB_CONNECTION_SHARED=shared
DB_HOST_SHARED=host.docker.internal
DB_PORT_SHARED=3306
DB_DATABASE_SHARED=api_integrations
DB_USERNAME_SHARED=
DB_PASSWORD_SHARED=
"""
        )

        content = content.replace(
            f"""APP_URL=http://localhost:8000""",
            f"""APP_URL=http://{domain_name}

MESSAGE_CHANNEL_URL="""
        )


        content = content.replace(
            f"""LOG_CHANNEL=stack""",
            f"""LOG_CHANNEL=daily"""
        )


        # Escribir el contenido actualizado
        with open(main_path, "w") as f:
            f.write(content)

        print_message("use User Models correctamente.", GREEN)

    except Exception as e:
        print_message(f"Error al actualizar {main_path}: {e}", CYAN)
        
