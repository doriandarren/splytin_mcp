import os
from gen.helpers.helper_print import print_cyan, print_green, print_message, GREEN, CYAN, run_command
from gen.python_django.helpers.helper_file import helper_add_import, helper_append_content, helper_replace_block

from gen.helpers.helper_file import HelperFile



class DjGenerateEnv:
    

    def invoke(self, full_path, project_name_format, project_name, domain_name, app_main, venv_python):
        
        self.install_env(full_path, venv_python)
        self.update_settings(full_path, app_main)
        
        self.create_env(full_path, project_name_format, project_name, domain_name)
        self.create_env_example(full_path, project_name_format, project_name, domain_name)



    def install_env(self, full_path, venv_python):
        print_cyan("Instalando python-dotenv...")
        run_command(f'"{venv_python}" -m pip install python-dotenv', cwd=full_path)
        print_green("python-dotenv instalado correctamente.")



    def update_settings(self, full_path, app_name):
        
        helper_add_import(
            full_path, 
            f"{app_name}/settings.py", 
            "import os"
        )
        
        helper_add_import(
            full_path, 
            f"{app_name}/settings.py", 
            "from dotenv import load_dotenv"
        )
        
        helper_append_content(
            full_path,
            f"{app_name}/settings.py",
            f'load_dotenv(BASE_DIR / ".env")                          # Enviroment',
            end_line=19
        )
        
        
        str = f"""\n## ENV
APP_NAME = os.getenv("APP_NAME", "splytin")
APP_ENV = os.getenv("APP_ENV", "local")
MESSAGE_CHANNEL_URL = os.getenv("MESSAGE_CHANNEL_URL")
        """
        
        helper_append_content(
            full_path, 
            f"{app_name}/settings.py", 
            str
        )



    
    def create_env(self, full_path, project_name_format, project_name, domain_name):
        """
        Genera el archivo .env
        """

        content = f'''# Application
APP_NAME={project_name_format}
APP_ENV=local

# Django Security
SECRET_KEY=
DEBUG=true
ALLOWED_HOSTS=localhost,127.0.0.1,{project_name}        # Production: {project_name}

# External Services
MESSAGE_CHANNEL_URL=https://discord.com/api/webhooks/1457825506153074817/TMV5itefILgSPbdhnaBktU0dmqI7DEk1FAU7ZG6lNqW8tYinmzmhc38R5qZGkVZofYcB

# Local Security
SECURE_SSL_REDIRECT=false
SESSION_COOKIE_SECURE=false
CSRF_COOKIE_SECURE=false
SECURE_HSTS_SECONDS=0

# Production Security
# DEBUG=false
# SECURE_SSL_REDIRECT=true
# SESSION_COOKIE_SECURE=true
# CSRF_COOKIE_SECURE=true
# SECURE_HSTS_SECONDS=3600

# Database Settings: [sqlite | postgresql | mysql]
DB_ENGINE=postgresql
DB_NAME={project_name_format}_db
DB_USER={project_name_format}_user
DB_PASSWORD={project_name_format}_pass
DB_HOST=127.0.0.1
DB_PORT=5432

# Email
EMAIL_HOST=smtp.ionos.es
EMAIL_PORT=465
EMAIL_USE_TLS=False
EMAIL_USE_SSL=True
EMAIL_HOST_USER=webmaster@{domain_name}
EMAIL_HOST_PASSWORD="pass"
DEFAULT_FROM_EMAIL=webmaster@{domain_name}
EMAIL_TIMEOUT=30

# Internationalization
LANGUAGE_CODE=es-es
TIME_ZONE=Europe/Madrid

# CORS
CORS_ALLOW_ALL_ORIGINS=true

# Seed Users
SEED_USER_PASSWORD=Tailandia2026
'''


        # Crear el archivo
        HelperFile.write(
            folder_path=full_path,
            file_name=".env",
            content=content
        )





    def create_env_example(self, full_path, project_name_format, project_name, domain_name):
        """
        Genera el archivo .env.example
        """
        
        content = f'''# Application
APP_NAME={project_name_format}
APP_ENV=local

# Django Security
SECRET_KEY=
DEBUG=true
ALLOWED_HOSTS=localhost,127.0.0.1,{project_name}        # Production: {project_name}

# External Services
MESSAGE_CHANNEL_URL=

# Local Security
SECURE_SSL_REDIRECT=false
SESSION_COOKIE_SECURE=false
CSRF_COOKIE_SECURE=false
SECURE_HSTS_SECONDS=0

# Production Security
# DEBUG=false
# SECURE_SSL_REDIRECT=true
# SESSION_COOKIE_SECURE=true
# CSRF_COOKIE_SECURE=true
# SECURE_HSTS_SECONDS=3600

# Database Settings: [sqlite | postgresql | mysql]
DB_ENGINE=postgresql
DB_NAME=
DB_USER=
DB_PASSWORD=
DB_HOST=127.0.0.1
DB_PORT=5432

# Email
EMAIL_HOST=smtp.ionos.es
EMAIL_PORT=465
EMAIL_USE_TLS=False
EMAIL_USE_SSL=True
EMAIL_HOST_USER=webmaster@{domain_name}
EMAIL_HOST_PASSWORD="pass"
DEFAULT_FROM_EMAIL=webmaster@{domain_name}
EMAIL_TIMEOUT=30

# Internationalization
LANGUAGE_CODE=es-es
TIME_ZONE=Europe/Madrid

# CORS
CORS_ALLOW_ALL_ORIGINS=true

# Seed Users
SEED_USER_PASSWORD=
'''


        # Crear el archivo
        HelperFile.write(
            folder_path=full_path,
            file_name=".env.example",
            content=content
        )