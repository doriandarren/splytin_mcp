from gen.helpers.helper_print import print_green, run_command


class ReactTsZodReactHookForm:
    
    def invoke(self, full_path):
        self.install(full_path)
      
        
    def install(self, full_path):
        # Instalar dependencias
        run_command(
            "npm install zod react-hook-form @hookform/resolvers",
            cwd=full_path
        )
        
        print_green("zod creado correctamente.")
        print_green("react-hook-form creado correctamente.")
    
