import os
from gen.helpers.helper_file import HelperFile
from gen.helpers.helper_json import HelperJson
from gen.helpers.helper_print import print_green, run_command





class ReactTsChadcn:
    
    
    def invoke(self, full_path):
        self.install_tailwind(full_path)
        self.install_types(full_path)
        self.update_file_ts_config_json(full_path)
    
    
    
    def install_tailwind(self, full_path):
        # Instalar dependencias
        run_command(
            "npm install tailwindcss @tailwindcss/vite",
            cwd=full_path
        )
        print_green("tailwindcss creado correctamente.")
        
        
    
    
    def install_types(self, full_path):
        # Instalar dependencias
        run_command(
            "npm install -D @types/node",
            cwd=full_path
        )
        print_green("@types/node creado correctamente.")
        
        
        
        
    def update_file_ts_config_json(self, full_path):
        """Actualiza tsconfig.json."""

        file_path = os.path.join(full_path, "tsconfig.json")

        HelperJson.update(
            file_path=file_path,
            new_data={
                "compilerOptions": {
                    "baseUrl": ".",
                    "paths": {
                        "@/*": ["./src/*"]
                    }
                }
            }
        )

        print_green("tsconfig.json actualizado correctamente.")
        
        
    
    
    

    def invokehh(self, full_path):
        """
        Genera el archivo.
        """

        folder_path = os.path.join(full_path, "src")

        content = r'''/* index.css */
@import "tailwindcss";'''

        # Crear el archivo
        HelperFile.write(
            folder_path=folder_path,
            file_name="index.css",
            content=content
        )