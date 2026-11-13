import os
from helpers.helper_file import HelperFile
from helpers.helper_print import print_green, run_command


class ReactTsComponentChart:

    def invoke(self, full_path):
        self.install(full_path)
    
    
    
    def install(self, full_path):
        # Instalar dependencias
        run_command(
            "npm install react-router",
            cwd=full_path
        )

        print_green("react-router instalado.")