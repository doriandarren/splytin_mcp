from helpers.helper_print import print_cyan, print_green, run_command


class LaravelSnappy:

    def invoke(self, full_path):
        self.install_snappy(full_path)
        self.install_publish(full_path)



    def install_snappy(self, full_path):
        print_cyan("Instalando Snappy...")
        run_command("composer require barryvdh/laravel-snappy", cwd=full_path)
        print_green("Snappy instalado correctamente.")



    def install_publish(self, full_path):
        print_cyan("Publicando Snappy...")
        run_command("php artisan vendor:publish --provider='Barryvdh\Snappy\ServiceProvider'", cwd=full_path)
        print_green("Snappy publicado correctamente.")


