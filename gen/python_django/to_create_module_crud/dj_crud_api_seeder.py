import os
from gen.helpers.helper_file import HelperFile
from gen.python_django.helpers.helper_dj_seeder import HelperDjSeeder


class DjCrudApiSeeder:


    def invoke(
        self,
        full_path,
        project_name,
        singular_name,
        plural_name,
        singular_name_kebab,
        plural_name_kebab,
        singular_name_snake,
        plural_name_snake,
        singular_first_camel,
        plural_first_camel,
        columns,
    ):
        """
        Genera un seeder Django utilizando Faker.
        """

        # Crear carpeta management
        folder_path = os.path.join(
            full_path,
            "apps",
            plural_name_snake,
            "management"
        )
        HelperFile.create_init_file(folder_path)

        # Crear carpeta commands
        folder_path = os.path.join(
            full_path,
            "apps",
            plural_name_snake,
            "management",
            "commands"
        )
        HelperFile.create_init_file(folder_path)

        # Generar campos Faker
        fields_content = HelperDjSeeder.get_fields(columns)

        # Generar imports de relaciones
        imports_content = HelperDjSeeder.get_fk_imports(columns)

        # Preparar claves foráneas
        setup_content = HelperDjSeeder.get_fk_setup(columns)

        # Generar contenido del seeder
        content = f'''from faker import Faker
from django.core.management.base import BaseCommand, CommandError
from apps.{plural_name_snake}.models import {singular_name}
{imports_content}


class Command(BaseCommand):
    help = "Genera registros falsos para {plural_name}"

    def add_arguments(self, parser):
        parser.add_argument(
            "--count",
            type=int,
            default=10,
            help="Cantidad de registros a generar"
        )

    def handle(self, *args, **kwargs):
        fake = Faker("es_ES")
        count = kwargs["count"]

        if count < 1:
            raise CommandError("El número de registros debe ser mayor que cero.")

{setup_content}

        for _ in range(count):
            data = {{
{fields_content}
            }}

            {singular_name}.objects.create(**data)
            
            
        self.stdout.write(
            self.style.SUCCESS(
                f"Seed seed_{plural_name_snake}. Total: {{count}}"
            )
        )    
'''

        # Crear el archivo
        HelperFile.write(
            folder_path=folder_path,
            file_name=f"seed_{plural_name_snake}.py",
            content=content
        )