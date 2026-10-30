import os
from gen.helpers.helper_file import HelperFile
from gen.helpers.helper_print import print_green, run_command


class ReactTsZustand:

    def invoke(self, full_path):
        self.install(full_path)
  
    
    def install(self, full_path):
        # Instalar dependencias
        run_command(
            "npm install zustand",
            cwd=full_path
        )
        
        print_green("zustand creado correctamente.")
    
    
    
  
        
    
        
        
