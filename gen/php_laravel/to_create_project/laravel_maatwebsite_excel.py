from helpers.helper_print import print_cyan, print_green, run_command


class LaravelMaatwebsiteExcel:

    def invoke(self, full_path):
        self.install_excel(full_path)
        self.install_publish(full_path)


    def install_excel(self, full_path):
        print_cyan("Instalando Excel...")
        run_command("composer require maatwebsite/excel", cwd=full_path)
        print_green("Excel instalado correctamente.")


    def install_publish(self, full_path):
        print_cyan("Publicando Excel...")
        ##run_command("php artisan vendor:publish --provider=\"Maatwebsite\Excel\ExcelServiceProvider\"", cwd=full_path)
        run_command('php artisan vendor:publish --provider="Maatwebsite\\Excel\\ExcelServiceProvider"', cwd=full_path)
        print_green("Excel publicado correctamente.")
