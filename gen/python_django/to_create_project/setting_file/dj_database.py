
import os
from gen.helpers.helper_print import print_green, print_red


class DjDatabase:

    def invoke(self, full_path, app_main, project_name_format):
        """
        Actualiza la configuración de la base de datos.
        """
        return self.update_file(full_path, app_main, project_name_format)




    def update_file(self, full_path, app_main, project_name_format):
        """
        Actualiza el archivo settings.py.
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

            # Configuración original de Django
            old_databases = """DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}"""

            # Nueva configuración
            new_databases = f'''DB_ENGINE = os.getenv("DB_ENGINE", "sqlite")

if DB_ENGINE == "postgresql":
    DATABASES = {{
        "default": {{
            "ENGINE": "django.db.backends.postgresql",
            "NAME": os.getenv("DB_NAME", "{project_name_format}_db"),
            "USER": os.getenv("DB_USER", "{project_name_format}_user"),
            "PASSWORD": os.getenv("DB_PASSWORD", ""),
            "HOST": os.getenv("DB_HOST", "127.0.0.1"),
            "PORT": os.getenv("DB_PORT", "5432"),
        }}
    }}

elif DB_ENGINE == "mysql":
    DATABASES = {{
        "default": {{
            "ENGINE": "django.db.backends.mysql",
            "NAME": os.getenv("DB_NAME", "{project_name_format}_db"),
            "USER": os.getenv("DB_USER", "{project_name_format}_user"),
            "PASSWORD": os.getenv("DB_PASSWORD", ""),
            "HOST": os.getenv("DB_HOST", "127.0.0.1"),
            "PORT": os.getenv("DB_PORT", "3306"),
        }}
    }}

else:
    DATABASES = {{
        "default": {{
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }}
    }}
    

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
'''

            # Reemplazos
            replacements = {
                old_databases: new_databases,
            }

            # Validar y aplicar los reemplazos
            new_content = content

            for old_text, new_text in replacements.items():
                if old_text not in new_content:
                    raise ValueError(
                        f"No se encontró el texto esperado: {old_text}"
                    )

                new_content = new_content.replace(
                    old_text,
                    new_text,
                    1
                )

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
