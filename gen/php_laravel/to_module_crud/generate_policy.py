import os
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
    """
    Genera el archivo
    """

    folder_path = os.path.join(full_path, "app", "Policies", version_api, plural_name)
    file_path = os.path.join(folder_path, f"{singular_name}Policy.php")

    os.makedirs(folder_path, exist_ok=True)

    content = f"""<?php

namespace App\\Policies\\{version_api}\\{plural_name};

use App\\Models\\{namespace}\\{plural_name}\\{singular_name};
use App\\Permissions\\V1\\Abilities;
use App\\Models\\User;


class {singular_name}Policy
{{
    /**
     * Create a new policy instance.
     */
    public function __construct(){{ }}


    public function update(User $user, {singular_name} ${singular_name_camel})
    {{

        // if($user->tokenCan(Abilities::UPDATE_{singular_name_snake.upper()})){{
        //     return true;
        // }}else if($user->tokenCan(Abilities::UPDATE_OWN_{singular_name_snake.upper()})){{
        //     return $user->id === ${singular_name_camel}->created_by;
        // }}

        return $user->id === ${singular_name_camel}->created_by;
    }}
    
}}
"""

    try:
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)
