import os
from gen.helpers.helper_file import HelperFile


class DjGenerateApiSeeder:

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
        columns
    ):
        """
        Genera el archivo.
        """

        folder_path = os.path.join(full_path, "apps", plural_name_snake, "management")
        HelperFile.create_init_file(folder_path)
        
        
        folder_path = os.path.join(full_path, "apps", plural_name_snake, "management", "commands")
        HelperFile.create_init_file(folder_path)
        

        # Generar campos dinámicamente
        fields = []

        for column in columns:
            name = column["name"]
            field_type = column["type"]

            if column.get("is_fk"):
                value = "None"
            elif field_type in ["string", "text"]:
                value = repr(f"Ejemplo {name}")
            elif field_type in ["integer", "bigInteger"]:
                value = "1"
            elif field_type in ["float", "double", "decimal"]:
                value = "1.0"
            elif field_type == "boolean":
                value = "True"
            else:
                value = "None"

            fields.append(f"                {name!r}: {value},")

        fields_content = "\n".join(fields)

        content = f'''from django.core.management.base import BaseCommand
from apps.{plural_name_snake}.models import {singular_name}


class Command(BaseCommand):
    help = "Crea registros de ejemplo para {plural_name}"

    def handle(self, *args, **kwargs):
        data = [
            {{
{fields_content}
            }}
        ]

        for item in data:
            obj = {singular_name}.objects.create(**item)

            self.stdout.write(
                self.style.SUCCESS(
                    f"Registro creado [{singular_name}]: {{obj.pk}}"
                )
            )
'''

        print(full_path)
        

        # Crear el archivo
        HelperFile.write(
            folder_path=folder_path,
            file_name=f"seed_{plural_name_snake}.py",
            content=content
        )