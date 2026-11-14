from helpers.helper_print import print_cyan, print_green, run_command


class LaravelFpdfMerge:

    def invoke(self, full_path):
        self.install_fpdf_merge(full_path)


    def install_fpdf_merge(self, full_path):
        print_cyan("Instalando FPDF Merge...")
        run_command("composer require setasign/fpdf setasign/fpdi", cwd=full_path)
        print_green("FPDF Merge instalado correctamente.")
