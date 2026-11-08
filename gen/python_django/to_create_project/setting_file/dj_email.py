import os
from gen.helpers.helper_print import dd, print_green, print_red


class DjEmail:

    def invoke(self, full_path, app_main):
        """
        Actualiza el archivo
        """
        main_path = os.path.join(full_path, app_main, "settings.py")
    
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
                """MAILERS = {
    'default': {
        'BACKEND': 'django.core.mail.backends.console.EmailBackend',
    },
}""":
                """
# Email - SMTP Configuration
MAILERS = {
    "default": {
        "BACKEND": "django.core.mail.backends.smtp.EmailBackend",
        "OPTIONS": {
            # SMTP Server
            "host": os.getenv("EMAIL_HOST", "smtp.ionos.es"),
            "port": int(os.getenv("EMAIL_PORT", "465")),

            # Security
            "use_tls": os.getenv("EMAIL_USE_TLS", "False").lower() == "true",
            "use_ssl": os.getenv("EMAIL_USE_SSL", "True").lower() == "true",

            # Authentication
            "username": os.getenv("EMAIL_HOST_USER", ""),
            "password": os.getenv("EMAIL_HOST_PASSWORD", ""),

            # Connection timeout
            "timeout": int(os.getenv("EMAIL_TIMEOUT", "30")),
        },
    },
}

# Default Sender
DEFAULT_FROM_EMAIL = os.getenv("DEFAULT_FROM_EMAIL", "")
""",
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
    
        