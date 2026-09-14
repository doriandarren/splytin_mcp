import os
from gen.helpers.helper_print import print_message, GREEN, CYAN





def generate_abilities(full_path):
    """
    Genera el archivo
    """

    folder_path = os.path.join(full_path, "app", "Permissions", "V1")
    file_path = os.path.join(folder_path, "Abilities.php")

    os.makedirs(folder_path, exist_ok=True)

    content = r"""<?php

namespace App\Permissions\V1;

use App\Enums\EnumAbilitySuffix;
use App\Models\User;

final class Abilities
{

    // Abilities
    public const INDEX_ABILITY = 'ability:' . EnumAbilitySuffix::INDEX;
    public const SHOW_ABILITY = 'ability:' . EnumAbilitySuffix::SHOW;
    public const STORE_ABILITY = 'ability:' . EnumAbilitySuffix::STORE;
    public const UPDATE_ABILITY = 'ability:' . EnumAbilitySuffix::UPDATE;
    public const DELETE_ABILITY = 'ability:' . EnumAbilitySuffix::DELETE;

    // Own
    public const UPDATE_OWN_ABILITY = 'ability:own:' . EnumAbilitySuffix::UPDATE;
    public const DELETE_OWN_ABILITY = 'ability:own:' . EnumAbilitySuffix::DELETE;


    // #GENERATOR ...



    /**
     * Get Abilities
     *
     * @param User $user
     * @return void
     */
    public function getAbilities(User $user)
    {
        if($user->is_manager) {
            return [
                self::INDEX_ABILITY,
                self::SHOW_ABILITY,
                self::STORE_ABILITY,
                self::UPDATE_ABILITY,
                self::DELETE_ABILITY,
            ];
        } else {
            return [
                self::STORE_ABILITY,
                self::UPDATE_OWN_ABILITY,
                self::DELETE_OWN_ABILITY,
            ];
        }

    }
}

"""

    try:
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)
