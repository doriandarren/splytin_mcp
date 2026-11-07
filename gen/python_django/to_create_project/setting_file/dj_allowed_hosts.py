
import os
import re

from gen.helpers.helper_print import print_green, print_red


class DjAllowedHosts:

    def invoke(self, full_path, app_main):
        return self.update_file(full_path, app_main)

    def update_file(self, full_path, app_main):
        """
        Reemplaza ALLOWED_HOSTS en settings.py por una variable de entorno.
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

            # Buscar la línea que empieza por ALLOWED_HOSTS =
            pattern = r"^[ \t]*ALLOWED_HOSTS\s*=.*$"

            replacement = '''ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "localhost,127.0.0.1").split(",")

# Production Security
SECURE_SSL_REDIRECT = os.getenv("SECURE_SSL_REDIRECT", "False").lower() == "true"
SESSION_COOKIE_SECURE = os.getenv("SESSION_COOKIE_SECURE", "False").lower() == "true"
CSRF_COOKIE_SECURE = os.getenv("CSRF_COOKIE_SECURE", "False").lower() == "true"

# HTTP Strict Transport Security
SECURE_HSTS_SECONDS = int(os.getenv("SECURE_HSTS_SECONDS", "0"))
'''

            # Reemplazar únicamente la primera coincidencia
            new_content, count = re.subn(
                pattern,
                lambda match: replacement,
                content,
                count=1,
                flags=re.MULTILINE
            )

            # Validar el reemplazo
            if count == 0:
                raise ValueError("No se encontró ALLOWED_HOSTS en settings.py")

            # Evitar modificar el archivo si ya está configurado
            if new_content == content:
                print_green("ALLOWED_HOSTS ya está configurado correctamente.")
                return True

            # Escribir el contenido actualizado
            with open(main_path, "w", encoding="utf-8") as f:
                f.write(new_content)

            print_green(f"{main_path} actualizado correctamente.")
            return True

        except Exception as e:
            print_red(f"Error al actualizar {main_path}: {e}")
            return False
