import os
from gen.helpers.helper_columns import parse_columns_input
from gen.python_django.helpers.helper_file import (
    helper_append_content, 
    helper_create_init_file, 
    helper_update_line, 
    helper_update_list
)
from gen.python_django.to_create_module_crud.standard_module_crud_python_django import standard_module_crud_python_django
from gen.helpers.helper_print import print_message, GREEN, CYAN




import os
from gen.helpers.helper_file import HelperFile


class DjGenerateModuleUsers:
    
    def invoke(self, full_path, project_name, project_name_format, app_main, domain_name):
    
        self.create_module_users(full_path, project_name_format, app_main)
        self.update_setting_auth_user_model(full_path, project_name_format, app_main)
        self.update_model(full_path, project_name_format, app_main)
        self.create_seeder(full_path, domain_name)
        self.update_serializer(full_path)
    
    
    

    def create_module_users(self, full_path, project_name_format, app_main):
        print_message(f"Generando el modulo de Users", CYAN)
        singular_name = "User"
        plural_name = "Users"
        input_menu_checkbox=["api_route", "api_serializer", "api_wiewset", "api_model", "api_service", "api_postman"]
        columns = parse_columns_input("email password")
        
        standard_module_crud_python_django(full_path, app_main, singular_name, plural_name, columns, input_menu_checkbox)
        
    
    
    def update_setting_auth_user_model(self, full_path, project_name_format, app_main):
        
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
      
    
    def create_seeder(self, full_path, domain_name):
        """
        Genera el archivo.
        """
        
        folder_path = os.path.join(full_path, "apps", "users", "management")
        HelperFile.create_init_file(folder_path)
        
        
        folder_path = os.path.join(full_path, "apps", "users", "management", "commands")
        HelperFile.create_init_file(folder_path)


        content = f'''import os
from dotenv import load_dotenv
from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth import get_user_model

load_dotenv()

class Command(BaseCommand):
    help = "Crea o actualiza usuarios por defecto"

    def handle(self, *args, **kwargs):
        
        password = os.getenv("SEED_USER_PASSWORD")

        if not password:
            raise CommandError(
                "La variable SEED_USER_PASSWORD no está configurada."
            )
    
        self.create_user(
            username="admin",
            email="admin@{domain_name}",
            password=password,
            first_name="Admin",
            last_name="Admin",
            is_staff=True,
            is_superuser=True,
        )

        self.create_user(
            username="manager",
            email="manager@{domain_name}",
            password=password,
            first_name="Manager",
            last_name="Manager",
            is_staff=True,
            is_superuser=False,
        )

        self.create_user(
            username="user",
            email="user@{domain_name}",
            password=password,
            first_name="User",
            last_name="User",
            is_staff=True,
            is_superuser=False,
        )

    def create_user(self, username, email, password, first_name, last_name, is_staff=False, is_superuser=False):
        User = get_user_model()

        user, created = User.objects.get_or_create(
            username=username,
            defaults={{"email": email}},
        )

        user.email = email
        user.first_name = first_name
        user.last_name = last_name
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

        # Crear el archivo
        HelperFile.write(
            folder_path=folder_path,
            file_name="seed_users.py",
            content=content
        )
    
    
    def update_serializer(self, full_path):
        """
        Genera el archivo.
        """

        folder_path = os.path.join(full_path, "apps", "users", "api")

        content = f'''#from rest_framework.serializers import ModelSerializer
from rest_framework_json_api.serializers import ModelSerializer
from apps.users.models import User


class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = [
            'id',
            'email',
            'first_name',
            'last_name',
            'is_active',
            'is_staff',
        ]
'''

        # Crear el archivo
        HelperFile.write(
            folder_path=folder_path,
            file_name="serializers.py",
            content=content
        )


    def update_model(self, full_path, project_name_format, app_main):
        """
        Genera el archivo.
        """

        folder_path = os.path.join(full_path, "apps", "users")

        content = f'''from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    
    email = models.EmailField(unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]
    
    
    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.username
'''

        # Crear el archivo
        HelperFile.write(
            folder_path=folder_path,
            file_name="models.py",
            content=content
        )