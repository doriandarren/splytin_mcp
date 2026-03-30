import os
from gen.helpers.helper_columns import parse_columns_input
from gen.python_django.helpers.helper_file import helper_append_content, helper_create_init_file, helper_update_line, helper_update_list
from gen.python_django.to_create_module_crud.standard_module_crud_python_django import standard_module_crud_python_django
from gen.helpers.helper_print import print_message, GREEN, CYAN



def generate_module_users(full_path, project_name_format, app_main):
    create_module_users(full_path, project_name_format, app_main)
    update_setting_auth_user_model(full_path, project_name_format, app_main)
    update_model(full_path, project_name_format, app_main)
    create_seeder(full_path, project_name_format, app_main)
    
    
def create_module_users(full_path, project_name_format, app_main):
    
    print_message(f"Generando el modulo de Users", CYAN)
    singular_name = "User"
    plural_name = "Users"
    columns = "email password"
    input_menu_checkbox = ['api_route', 'api_serializer', 'api_wiewset', 'api_model', 'api_service']
    formatColumns = parse_columns_input(columns)
    
    standard_module_crud_python_django(full_path, app_main, singular_name, plural_name, formatColumns, input_menu_checkbox)



def update_setting_auth_user_model(full_path, project_name_format, app_main):
    
    helper_append_content(
        full_path,
        f"{app_main}/settings.py",
        "\n# USERS"
    )
    
    helper_append_content(
        full_path,
        f"{app_main}/settings.py",
        "AUTH_USER_MODEL = 'users.User'"
    )

    print_message("settings.py actualizado correctamente.", GREEN)
      


def update_model(full_path, project_name_format, app_main):
    """
    Genera el archivo
    """

    folder_path = os.path.join(full_path, "apps", "users")
    file_path = os.path.join(folder_path, "models.py")

    os.makedirs(folder_path, exist_ok=True)

    content = f'''from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.username
'''

    try:
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)



def create_seeder(full_path, project_name_format, app_main):
    """
    Genera el archivo
    """

    folder_path = os.path.join(full_path, "apps", "users", "management", "commands")
    file_path = os.path.join(folder_path, "seed_users.py")

    os.makedirs(folder_path, exist_ok=True)
    
    # Crear el archivo __init__.py en la carpeta commands
    helper_create_init_file(folder_path)
    
    
    # Crear el archivo __init__.py en la carpeta management
    folder_path_management = os.path.join(full_path, "apps", "users", "management")
    helper_create_init_file(folder_path_management)
    

    # Content
    content = f'''from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    help = "Crea o actualiza usuarios por defecto"

    def handle(self, *args, **kwargs):
        self.create_user(
            username="admin",
            email="admin@{project_name_format}.com",
            password="Tailandia2026",
            is_staff=True,
            is_superuser=True,
        )

        self.create_user(
            username="manager",
            email="manager@{project_name_format}.com",
            password="Tailandia2026",
            is_staff=True,
            is_superuser=False,
        )

        self.create_user(
            username="user",
            email="user@{project_name_format}.com",
            password="Tailandia2026",
            is_staff=True,
            is_superuser=False,
        )

    def create_user(self, username, email, password, is_staff=False, is_superuser=False):
        User = get_user_model()

        user, created = User.objects.get_or_create(
            username=username,
            defaults={"email": email},
        )

        user.email = email
        user.is_active = True
        user.is_staff = is_staff
        user.is_superuser = is_superuser
        user.set_password(password)
        user.save()

        if created:
            self.stdout.write(self.style.SUCCESS(f"Usuario creado: {{user.username}}"))
        else:
            self.stdout.write(self.style.WARNING(f"Usuario actualizado: {{user.username}}"))

        return user
'''

    try:
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)


