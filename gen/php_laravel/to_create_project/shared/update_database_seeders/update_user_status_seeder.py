import os
from gen.helpers.helper_print import print_message, GREEN, CYAN

def update_user_status_seeder(full_path):
    """
    Genera el archivo
    """

    folder_path = os.path.join(full_path, "database", "seeders")
    file_path = os.path.join(folder_path, "UserStatusSeeder.php")

    os.makedirs(folder_path, exist_ok=True)

    content = r'''<?php

namespace Database\Seeders;

use App\Enums\UserStatuses\EnumUserStatus;
use App\Models\SHARED\UserStatuses\UserStatus;
use Illuminate\Database\Seeder;


class UserStatusSeeder extends Seeder
{

	/**
	* Run the database seeds.
	*
	* @return void
	*/
	public function run()
	{

        //Create UserStatus
        $userStatuses = [
            EnumUserStatus::ACTIVE_NAME,
            EnumUserStatus::INACTIVE_NAME,
            EnumUserStatus::BLOCKED_NAME,
        ];

        foreach ($userStatuses as $userStatus) {
            if (!UserStatus::where('name', $userStatus)->exists()) {

                UserStatus::factory()->create(['name' => $userStatus]);
            }
        }


    }

}
'''

    try:
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)