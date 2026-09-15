import os
from gen.helpers.helper_print import print_message, GREEN, CYAN

def generate_permissions_abilities(
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

    folder_path = os.path.join(full_path, "app", "Permissions", version_api, plural_name)
    file_path = os.path.join(folder_path, f"{singular_name}Permission.php")

    os.makedirs(folder_path, exist_ok=True)

    content = f"""<?php

namespace App\\Permissions\\{version_api}\\{plural_name};

use App\\Enums\\EnumAbilitySuffix;


final class {singular_name}Permission
{{

    // Abilities
    public const INDEX = '{singular_name_snake}' . EnumAbilitySuffix::INDEX;
    public const SHOW = '{singular_name_snake}' . EnumAbilitySuffix::SHOW;
    public const STORE = '{singular_name_snake}' . EnumAbilitySuffix::STORE;
    public const UPDATE = '{singular_name_snake}' . EnumAbilitySuffix::UPDATE;
    public const DELETE = '{singular_name_snake}' . EnumAbilitySuffix::DELETE;

    // Own
    public const UPDATE_OWN = '{singular_name_snake}' . EnumAbilitySuffix::UPDATE_OWN;
    public const DELETE_OWN = '{singular_name_snake}' . EnumAbilitySuffix::DELETE_OWN;
    
    
    /**
     * Function All
     *
     * @return array
     */
    public static function all(): array
    {{
        return [
            self::INDEX,
            self::SHOW,
            self::STORE,
            self::UPDATE,
            self::DELETE,
            self::UPDATE_OWN,
            self::DELETE_OWN,
        ];
    }}
    
}}
"""

    try:
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)
