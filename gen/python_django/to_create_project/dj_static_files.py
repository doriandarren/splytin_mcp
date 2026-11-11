import os
from gen.helpers.helper_print import print_green, print_red


class DjStaticFiles:
    

    def invoke(self, full_path, app_main):
        """
        Genera el archivo
        """
        self.create_folder(full_path)
        self.update_file(full_path, app_main)

        
        
    def update_file(self, full_path, app_main):
        """
        Actualiza el archivo
        """
        main_path = os.path.join(full_path, app_main, "settings.py")
    
        # Verificar si el archivo existe
        if not os.path.exists(main_path):
            print_red(f"Error: {main_path} no existe.")
            return False
    
        try:
            # Leer el contenido del archivo
            with open(main_path, "r", encoding="utf-8") as f:
                content = f.read()
    
            # Reemplazos
            replacements = {
                ## New Item -> KEY : VALUE
                """STATIC_URL = 'static/'""":
                '''# Static files
STATIC_URL = "/static/"

STATICFILES_DIRS = [
    BASE_DIR / "static",
]

STATIC_ROOT = BASE_DIR / "staticfiles"''',
            }
    
            # Validar y aplicar los reemplazos
            new_content = content
    
            for old_text, new_text in replacements.items():
                if old_text not in new_content:
                    raise ValueError(f"No se encontró el texto esperado: {old_text}")
    
                new_content = new_content.replace(old_text, new_text, 1)
    
            if new_content == content:
                raise ValueError("No se realizó ningún reemplazo.")
    
            # Escribir el contenido actualizado
            with open(main_path, "w", encoding="utf-8") as f:
                f.write(new_content)
    
            print_green(f"{main_path} actualizado correctamente.")
    
            return True
    
        except Exception as e:
            print_red(f"Error al actualizar {main_path}: {e}")
            return False
    
        
        
        
        


    def create_folder(self, full_path):
        
        ## Folder static
        folder_path = os.path.join(full_path, "static", "images")
        os.makedirs(folder_path, exist_ok=True)
        print_green(f"Carpeta uploads creada")


        ## Folder staticfiles
        folder_path = os.path.join(full_path, "staticfiles")
        os.makedirs(folder_path, exist_ok=True)
        print_green(f"Carpeta staticfiles creada")