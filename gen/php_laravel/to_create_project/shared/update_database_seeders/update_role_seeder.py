import os
from helpers.helper_print import print_message, GREEN, CYAN

def update_role_seeder(full_path):
    """
    Genera el archivo
    """

    folder_path = os.path.join(full_path, "database", "seeders")
    file_path = os.path.join(folder_path, "RoleSeeder.php")

    os.makedirs(folder_path, exist_ok=True)

    content = r'''<?php

namespace Database\Seeders;

use App\Enums\Roles\EnumRole;
use App\Models\SHARED\Roles\Role;
use Illuminate\Database\Seeder;



class RoleSeeder extends Seeder
{

	/**
	* Run the database seeds.
	*
	* @return void
	*/
	public function run()
	{
        // ADMIN
        Role::factory()->create([
            'name' => EnumRole::ADMIN,
            'description' => EnumRole::ADMIN_DESCRIPTION,
        ]);


        // MANAGER
        Role::factory()->create([
            'name' => EnumRole::MANAGER,
            'description' => EnumRole::MANAGER_DESCRIPTION,
        ]);


        // USER
        Role::factory()->create([
            'name' => EnumRole::USER,
            'description' => EnumRole::USER_DESCRIPTION,
        ]);


        // ERP
        Role::factory()->create([
            'name' => EnumRole::ERP,
            'description' => EnumRole::ERP_DESCRIPTION,
        ]);

	}

}
'''

    try:
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)