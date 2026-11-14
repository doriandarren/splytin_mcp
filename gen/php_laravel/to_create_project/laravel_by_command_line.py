import os
from helpers.helper_print import print_cyan, print_green, run_command


class LaravelByCommandLine:

    def invoke(self, full_path):
        self.create_project(full_path)
        self.create_install_sanctum(full_path)



    def create_project(self, full_path):
        # Verifica si el directorio ya existe
        if os.path.exists(full_path):
            print_green(f'El directorio {full_path} ya existe. Abortando.')
            return

        # Comando para crear un nuevo proyecto Laravel
        command = f'composer create-project --prefer-dist laravel/laravel {full_path}'
        run_command(command)
        print_green(f'Proyecto Laravel creado en: {full_path}')


    def create_install_sanctum(self, full_path):
        print_cyan("Instalando Sanctum...")
        run_command("php artisan install:api -n", cwd=full_path)
        print_green("Sanctum instalado correctamente.")



