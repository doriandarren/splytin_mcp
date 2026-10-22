import os
from gen.helpers.helper_file import HelperFile
from gen.helpers.helper_print import print_cyan, print_green, run_command


class DjGenerateFaker:

    def invoke(self, full_path, venv_python):
        """
        Install
        """
        print_cyan("Instalando Faker...")
        run_command(f'"{venv_python}" -m pip install Faker', cwd=full_path)
        print_green("Faker instalado correctamente.")
                

        