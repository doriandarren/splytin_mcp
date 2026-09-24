import os
from sys import api_version
from gen.helpers.helper_print import print_message, GREEN, CYAN




def generate_policy(
    full_path,
    namespace,
    version_api,
    project_name,
    folder_group,
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
    create_policy(
        full_path,
        namespace,
        version_api,
        project_name,
        folder_group,
        singular_name,
        plural_name,
        singular_name_camel,
        plural_name_camel,
        singular_name_kebab,
        plural_name_kebab,
        singular_name_snake,
        plural_name_snake,
        columns
    )
    
    update_app_service_provider(
        full_path,
        namespace,
        version_api,
        project_name,
        folder_group,
        singular_name,
        plural_name,
        singular_name_camel,
        plural_name_camel,
        singular_name_kebab,
        plural_name_kebab,
        singular_name_snake,
        plural_name_snake,
        columns
    )




def create_policy(
    full_path,
    namespace,
    version_api,
    project_name,
    folder_group,
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
    Genera el archivo
    """

    folder_path = os.path.join(full_path, "app", "Policies", version_api, plural_name)
    file_path = os.path.join(folder_path, f"{singular_name}Policy.php")

    os.makedirs(folder_path, exist_ok=True)

    content = f"""<?php

namespace App\\Policies\\{version_api}\\{plural_name};

use App\\Models\\{namespace}\\{plural_name}\\{singular_name};
use App\\Permissions\\V1\\{plural_name}\\{singular_name}Permission;
use App\\Models\\User;


class {singular_name}Policy
{{
    
    /**
     * Create a new policy instance.
     */
    public function __construct(){{ }}
    
    
    public function viewAny(User $user): bool
    {{
        return $user->tokenCan('*')
            || $user->tokenCan({singular_name}Permission::INDEX);
    }}
    
    
    public function view(User $user, {singular_name} ${singular_name_camel}): bool
    {{
        return $user->tokenCan('*')
            || $user->tokenCan({singular_name}Permission::SHOW);
    }}

    
    public function create(User $user): bool
    {{
        return $user->tokenCan('*')
            || $user->tokenCan({singular_name}Permission::STORE);
    }}


    public function update(User $user, {singular_name} ${singular_name_camel})
    {{
        if ($user->tokenCan('*')) {{
            return true;
        }}

        if ($user->tokenCan({singular_name}Permission::UPDATE)) {{
            return true;
        }}

        if ($user->tokenCan({singular_name}Permission::UPDATE_OWN)) {{
            return $user->id === ${singular_name_camel}->created_by;
        }}

        return false;
    }}
    
    public function delete(User $user, {singular_name} ${singular_name_camel}): bool
    {{
        if ($user->tokenCan('*')) {{
            return true;
        }}

        if ($user->tokenCan({singular_name}Permission::DELETE)) {{
            return true;
        }}

        if ($user->tokenCan({singular_name}Permission::DELETE_OWN)) {{
            return $user->id === ${singular_name_camel}->created_by;
        }}

        return false;
    }}
    
}}
"""

    try:
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)





def update_app_service_provider(
        full_path,
        namespace,
        version_api,
        project_name,
        folder_group,
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
    main_path = os.path.join(full_path, "app", "Providers", "AppServiceProvider.php")

    # Verificar si el archivo existe
    if not os.path.exists(main_path):
        print_message(f"Error: {main_path} no existe.", CYAN)
        return

    try:
        # Leer el contenido del archivo
        with open(main_path, "r") as f:
            content = f.read()
        
        path_temp = f"App\\Models\\{namespace}\\{plural_name}\\{singular_name}"
            
        ## Only model User
        if singular_name == 'User':
            path_temp = f"App\\Models\\{singular_name}"
            

        # Reemplazos
        content = content.replace(
            """use Illuminate\Support\ServiceProvider;""",
            f"""use {path_temp};
use App\\Policies\\{version_api}\\{plural_name}\\{singular_name}Policy;
use Illuminate\\Support\\ServiceProvider;"""
        )
        
        
        
        
        # Reemplazos
        content = content.replace(
            """    public function boot(): void
    {""",
            f"""    public function boot(): void
    {{
        // {singular_name}
        Gate::policy({singular_name}::class, {singular_name}Policy::class);
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

    




