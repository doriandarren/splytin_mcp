
import os
import re
import subprocess

from gen.helpers.helper_print import print_green, print_red, print_cyan


class DjSecretKey:

    def invoke(self, full_path, app_main, venv_python):
        secret_key = self.get_secret_key(full_path, venv_python)
        self.update_file(full_path, app_main)
        self.update_env(full_path, app_main, secret_key)



    def get_secret_key(self, full_path, venv_python):
        """
        Genera una SECRET_KEY de Django y la captura en una variable.
        """
        print_cyan("Generando SECRET_KEY de Django...")

        try:
            result = subprocess.run(
                [
                    venv_python,
                    "-c",
                    "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
                ],
                cwd=full_path,
                capture_output=True,
                text=True,
                check=True
            )

            secret_key = result.stdout.strip()

            print_green("SECRET_KEY generada correctamente.")

            return secret_key

        except subprocess.CalledProcessError as e:
            print_red(f"Error al generar SECRET_KEY: {e.stderr}")
            return None




    def update_file(self, full_path, app_main):
        """
        Reemplaza SECRET_KEY en settings.py por una variable de entorno.
        """
        main_path = os.path.join(full_path, app_main, "settings.py")

        if not os.path.exists(main_path):
            print_red(f"Error: {main_path} no existe.")
            return False

        try:
            with open(main_path, "r", encoding="utf-8") as f:
                content = f.read()

            pattern = r"^[ \t]*SECRET_KEY\s*=.*$"
            replacement = 'SECRET_KEY = os.environ["SECRET_KEY"]'

            new_content, count = re.subn(
                pattern,
                replacement,
                content,
                count=1,
                flags=re.MULTILINE
            )

            if count == 0:
                raise ValueError("No se encontró SECRET_KEY en settings.py")

            if new_content == content:
                print_green("SECRET_KEY ya está configurada correctamente.")
                return True

            with open(main_path, "w", encoding="utf-8") as f:
                f.write(new_content)

            print_green(f"{main_path} actualizado correctamente.")
            return True

        except Exception as e:
            print_red(f"Error al actualizar {main_path}: {e}")
            return False



    def update_env(self, full_path, app_main, secret_key):
        """
        Actualiza el archivo
        """
        main_path = os.path.join(full_path, ".env")
    
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
                """SECRET_KEY=""":
                f'''SECRET_KEY="{secret_key}"''',
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
    
        