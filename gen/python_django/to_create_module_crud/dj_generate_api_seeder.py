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
        Genera un seeder Django utilizando Faker.
        """

        folder_path = os.path.join(
            full_path, "apps", plural_name_snake, "management"
        )
        HelperFile.create_init_file(folder_path)

        folder_path = os.path.join(
            full_path, "apps", plural_name_snake,
            "management", "commands"
        )
        HelperFile.create_init_file(folder_path)

        # Generar valores Faker para cada columna
        fields = []
        fk_imports = set()
        fk_setup = []
        fk_variables = {}

        for column in columns:
            name = column["name"]
            field_type = column["type"].lower()

            # Relaciones ForeignKey
            if column.get("is_fk"):
                related_model = column.get("related_model")

                if not related_model:
                    raise ValueError(
                        f"Falta related_model en {name}"
                    )

                if related_model == "User":
                    fk_imports.add(
                        "from django.contrib.auth import get_user_model"
                    )
                    model_expression = "get_user_model()"
                else:
                    related_plural = column.get(
                        "related_table"
                    )

                    if not related_plural:
                        raise ValueError(
                            f"Falta related_model_plural en {name}"
                        )

                    fk_imports.add(
                        f"from apps.{related_plural.lower()}.models "
                        f"import {related_model}"
                    )
                    model_expression = related_model

                variable = f"related_{name}"

                fk_setup.append(
                    f"        {variable} = "
                    f"{model_expression}.objects.order_by('pk').first()"
                )

                fk_setup.append(
                    f"        if {variable} is None:"
                )

                fk_setup.append(
                    f"            raise CommandError("
                    f"'No hay registros relacionados para {name}')"
                )

                fk_variables[name] = variable
                value = f"{variable}.pk"

            # Campos conocidos por nombre
            elif name == "name":
                value = "fake.name()"

            elif name == "email":
                value = "fake.unique.email()"

            elif name == "slug":
                value = "fake.unique.slug()"

            elif name == "description":
                value = "fake.text(max_nb_chars=200)"

            elif name == "phone":
                value = "fake.phone_number()"

            elif name == "address":
                value = "fake.address()"

            elif name == "title":
                value = "fake.sentence(nb_words=5)"

            # Campos según tipo
            elif field_type in ["string", "varchar", "char"]:
                value = "fake.word()"

            elif field_type in ["text", "longtext"]:
                value = "fake.text(max_nb_chars=200)"

            elif field_type in ["integer", "biginteger", "smallinteger"]:
                value = "fake.random_int(min=1, max=100)"

            elif field_type in ["float", "double", "decimal"]:
                value = (
                    "fake.pyfloat("
                    "left_digits=3, right_digits=2, positive=True)"
                )

            elif field_type in ["boolean", "bool"]:
                value = "fake.pybool()"

            elif field_type == "date":
                value = "fake.date_object()"

            elif field_type in ["datetime", "timestamp"]:
                value = "fake.date_time()"

            elif field_type in ["uuid"]:
                value = "fake.uuid4()"

            else:
                raise ValueError(
                    f"Tipo de campo no soportado: {name} ({field_type})"
                )

            fields.append(f"                {name!r}: {value},")

        fields_content = "\n".join(fields)

        ## Agregar en los imports: 
        imports_content = "\n".join(sorted(fk_imports))
        setup_content = "\n".join(fk_setup)
        

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

            obj = {singular_name}.objects.create(**data)

            self.stdout.write(
                self.style.SUCCESS(
                    f"{singular_name} creado: {{obj.pk}}"
                )
            )
'''

        HelperFile.write(
            folder_path=folder_path,
            file_name=f"seed_{plural_name_snake}.py",
            content=content
        )