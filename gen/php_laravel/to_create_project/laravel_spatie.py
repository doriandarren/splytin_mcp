import os
from helpers.helper_file import HelperFile
from helpers.helper_print import dd, print_green, print_red, run_command


class LaravelSpatie:

    def invoke(self, full_path):
        self.install(full_path)
        ##self.update_file(full_path)
    
    
    def install(self, full_path):
        # Instalar dependencias
        run_command(
            "composer require spatie/laravel-activitylog",
            cwd=full_path
        )
        print_green("spatie/laravel-activitylog instalado.")
    
    
    
    
    def update_file(self, full_path):
        """
        Actualiza el archivo
        """
        main_path = os.path.join(full_path, "settings.py")
    
        # Verificar si el archivo existe
        if not os.path.exists(main_path):
            print_red(f"Error: {main_path} no existe.")
            dd(f"Error: {main_path} no existe.")
            return False
    
        try:
            # Leer el contenido del archivo
            with open(main_path, "r", encoding="utf-8") as f:
                content = f.read()
    
            # Reemplazos
            replacements = {
                ## New Item -> KEY : VALUE
                """    'rest_framework',                   # required for DRF,""":
                """    'rest_framework_json_api',          # required JSON API,""",
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
    
        