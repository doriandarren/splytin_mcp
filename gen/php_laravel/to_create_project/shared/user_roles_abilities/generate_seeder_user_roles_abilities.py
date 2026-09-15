import os
from gen.helpers.helper_print import print_message, GREEN, CYAN



def generate_seeder_user_roles_abilities(full_path):
    """
    Genera un archivo

    Args:
        full_path (str): Ruta completa del proyecto.
    """
    styles_path = os.path.join(full_path, "database", "seeders")

    # Crear la carpeta si no existe
    if not os.path.exists(styles_path):
        os.makedirs(styles_path)
        print_message(f"Carpeta creada: {styles_path}", GREEN)

    # Ruta completa del archivo
    file_path = os.path.join(styles_path, "UserRolesAbilitiesSeeder.php")

    # Contenido por defecto
    content = r"""<?php

namespace Database\Seeders;


use Illuminate\Database\Seeder;
use App\Permissions\V1\DefaultRolePermissions\DefaultRolePermissions;
use App\Enums\Dev\EnumDefaultCompany;
use App\Enums\Roles\EnumRole;
use App\Enums\UserStatuses\EnumUserStatus;
use App\Models\User;
use App\Models\API\Roles\Role;
use App\Models\API\Abilities\Ability;
use App\Models\API\UserStatuses\UserStatus;



class UserRolesAbilitiesSeeder extends Seeder
{

    /**
     * Run the database seeds.
     *
     * @return void
     */
    public function run()
    {
        
        /**
         * Create User
         */
        // SYSTEM
        $this->createUser(EnumDefaultCompany::SYSTEM_NAME, EnumDefaultCompany::SYSTEM_EMAIL, EnumDefaultCompany::PASSWORD, EnumRole::ADMIN);

        /**
         * Create User
         */
        // ADMIN
        $this->createUser(EnumDefaultCompany::ADMIN_NAME, EnumDefaultCompany::ADMIN_EMAIL, EnumDefaultCompany::PASSWORD, EnumRole::ADMIN);

        /**
         * Create Manager
         */

        $this->createUser(EnumDefaultCompany::MANAGER_NAME, EnumDefaultCompany::MANAGER_EMAIL, EnumDefaultCompany::PASSWORD, EnumRole::MANAGER);

        /**
         * Create User
         */
        $this->createUser(EnumDefaultCompany::USER_NAME, EnumDefaultCompany::USER_EMAIL, EnumDefaultCompany::PASSWORD, EnumRole::USER);



    }


    /**
     * @param $user
     * @param $roleName
     * @return void
     */
    private function createRoleUser($user, $roleName): void
    {
        $user = User::find($user->id);

        $role = Role::where('name', strtolower($roleName))->first();
        $user->assignRole($role);

    }


    /**
     * @param $name
     * @param $email
     * @param $password
     * @param $roleName
     * @return void
     */
    private function createUser($name, $email, $password, $roleName): void
    {

        // Create User
        $userActiveId = UserStatus::where('name', EnumUserStatus::ACTIVE_NAME)->first()->id;

        // User Inactive - SYSTEM
        if($name === EnumDefaultCompany::SYSTEM_NAME){
            $userActiveId = UserStatus::where('name', EnumUserStatus::INACTIVE_NAME)->first()->id;
        }

        $user = User::where('email', $email)->first();
        if (!$user) {
            $user = User::factory()->create([
                'name' => $name,
                'email' => $email,
                'email_verified_at' => now(),
                'password' => bcrypt($password), // password
                'remember_token' => NULL,
                'user_status_id' => $userActiveId,
                'created_by' => EnumDefaultCompany::SYSTEM_ID,
                'updated_by' => EnumDefaultCompany::SYSTEM_ID,
            ]);
        }


        // Crete RoleUser
        $this->createRoleUser($user, $roleName);

        // Create AbilityUser
        $this->createAbilityUser($user, $roleName);

    }



    /**
     * @param User $user
     * @param string $roleName
     * @return void
     */
    private function createAbilityUser(User $user, string $roleName): void
    {
        if ($roleName === EnumRole::ADMIN) {
            $this->assignAbilities(
                $user,
                DefaultRolePermissions::admin()
            );

            return;
        }

        if ($roleName === EnumRole::MANAGER) {
            $this->assignAbilities(
                $user,
                DefaultRolePermissions::manager()
            );

            return;
        }

        if ($roleName === EnumRole::USER) {
            $this->assignAbilities(
                $user,
                DefaultRolePermissions::user()
            );

            return;
        }

        // if ($roleName === EnumRole::ERP) {
        //     $this->assignAbilities(
        //         $user,
        //         DefaultRolePermissions::erp()
        //     );

        //     return;
        // }
    }


    /**
     * Assign Abilities
     *
     * @param User $user
     * @param array $abilities
     * @return void
     */
    private function assignAbilities(User $user, array $abilities): void
    {
        foreach ($abilities as $abilityName) {

            $ability = Ability::where('name', $abilityName)->first();

            if (!$ability) {
                throw new \RuntimeException(
                    "La habilidad '{$abilityName}' no existe en la tabla abilities."
                );
            }

            $user->allowTo($ability);
        }
    }

}
"""

    try:
        # Crear o sobrescribir el archivo con el contenido
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)
