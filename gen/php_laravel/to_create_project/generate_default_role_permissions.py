import os
from gen.helpers.helper_print import print_message, GREEN, CYAN

def generate_default_role_permissions(full_path):
    """
    Genera el archivo
    """

    folder_path = os.path.join(full_path, "app", "Permissions", "V1", "DefaultRolePermissions")
    file_path = os.path.join(folder_path, "DefaultRolePermissions.php")

    os.makedirs(folder_path, exist_ok=True)

    content = r"""<?php

namespace App\Permissions\V1\DefaultRolePermissions;

use App\Permissions\V1\Abilities\AbilityPermission;
use App\Permissions\V1\AbilityGroups\AbilityGroupPermission;
use App\Permissions\V1\AbilityUsers\AbilityUserPermission;
use App\Permissions\V1\Countries\CountryPermission;
use App\Permissions\V1\Roles\RolePermission;
use App\Permissions\V1\RoleUsers\RoleUserPermission;
use App\Permissions\V1\Users\UserPermission;
use App\Permissions\V1\UserStatuses\UserStatusPermission;

final class DefaultRolePermissions
{
    public static function admin(): array
    {
        return ['*'];
    }

    public static function manager(): array
    {
        return [
            ...AbilityPermission::manager(),
            ...AbilityGroupPermission::manager(),
            ...AbilityUserPermission::manager(),
            ...CountryPermission::manager(),
            ...RolePermission::manager(),
            ...RoleUserPermission::manager(),
            ...UserPermission::manager(),
            ...UserStatusPermission::manager(),
        ];
    }

    public static function user(): array
    {
        return [
            ...AbilityPermission::user(),
            ...AbilityGroupPermission::user(),
            ...AbilityUserPermission::user(),
            ...CountryPermission::user(),
            ...RolePermission::user(),
            ...RoleUserPermission::user(),
            ...UserPermission::user(),
            ...UserStatusPermission::user(),
        ];
    }
}
"""

    try:
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)
