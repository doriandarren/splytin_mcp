import os

from gen.helpers.helper_print import print_cyan, print_green, print_red, run_command


class DjGunicornAndWhitenoise:

    

    def invoke(self, full_path, app_main, venv_python):
        """
            Method Invoke
            
            gunicorn: Servidor WSGI para ejecutar Django en producción en Ubuntu.
            whitenoise: Permite servir archivos estáticos de Django (CSS, JS, imágenes)
            
            Args:
                full_path (_type_): Full Path
                venv_python (_type_): Path Venv
        """
        
        self.install_gunicorn(full_path, venv_python)
        self.install_whitenoise(full_path, venv_python)
        self.update_file_settings(full_path, app_main)
        
        
    
    def install_gunicorn(self, full_path, venv_python):
        print_cyan("Instalando gunicorn...")
        run_command(f'"{venv_python}" -m pip install gunicorn', cwd=full_path)
        print_green("gunicorn instalado correctamente.")
    
    
    def install_whitenoise(self, full_path, venv_python):
        print_cyan("Instalando whitenoise...")
        run_command(f'"{venv_python}" -m pip install whitenoise', cwd=full_path)
        print_green("whitenoise instalado correctamente.")
        
        
    
    def update_file_settings(self, full_path, app_main):
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
                """    'django.middleware.security.SecurityMiddleware',""":
                """    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',""",
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
    
        