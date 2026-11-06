
import os
from gen.helpers.helper_file import HelperFile


class LaravelCrudPermission:

    def invoke(
        self,
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
        Genera el archivo.
        """

        folder_path = os.path.join(
            full_path,
            "app",
            "Permissions",
            version_api,
            plural_name
        )

        change_name = [
            'ability_users',
            'role_users'
        ]

        plural_name_snake_temp = plural_name_snake

        if plural_name_snake in change_name:
            if plural_name_snake == 'ability_users':
                plural_name_snake_temp = 'ability_user'
            if plural_name_snake == 'role_users':
                plural_name_snake_temp = 'role_user'

        content = f"""<?php

namespace App\\Permissions\\{version_api}\\{plural_name};

use App\\Enums\\EnumAbilitySuffix;


final class {singular_name}Permission
{{

    // Abilities
    public const INDEX = '{plural_name_snake_temp}' . EnumAbilitySuffix::INDEX;
    public const SHOW = '{plural_name_snake_temp}' . EnumAbilitySuffix::SHOW;
    public const STORE = '{plural_name_snake_temp}' . EnumAbilitySuffix::STORE;
    public const UPDATE = '{plural_name_snake_temp}' . EnumAbilitySuffix::UPDATE;
    public const DELETE = '{plural_name_snake_temp}' . EnumAbilitySuffix::DELETE;

    // Own
    public const UPDATE_OWN = '{plural_name_snake_temp}' . EnumAbilitySuffix::UPDATE_OWN;
    public const DELETE_OWN = '{plural_name_snake_temp}' . EnumAbilitySuffix::DELETE_OWN;
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
    /**
     * Admin
     * Tiene permiso por defecto * en cada
     */
    /**
     * Manager
     *
     * @return array
     */
    public static function manager(): array
    {{
        return [
            self::INDEX,
            self::SHOW,
            self::STORE,
            self::UPDATE,
            self::DELETE,
        ];
    }}

    /**
     * User
     *
     * @return array
     */
    public static function user(): array
    {{
        return [
            self::INDEX,
            self::SHOW,
            self::STORE,
            self::UPDATE_OWN,
            self::DELETE_OWN,
        ];
    }}
}}
"""

        # Crear el archivo
        HelperFile.write(
            folder_path=folder_path,
            file_name=f"{singular_name}Permission.php",
            content=content
        )
