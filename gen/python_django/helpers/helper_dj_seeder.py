class HelperDjSeeder:

    @staticmethod
    def get_fields(columns):
        """
        Genera los campos y valores Faker para el seeder.
        """
        fields = []

        for column in columns:
            name = column["name"]
            field_type = column["type"].lower()

            if column.get("is_fk"):
                relationship_name = column["relationship_name"]
                related_table = column["related_table"]

                variable = f"related_{related_table}"

                value = f"fake.random_element(elements={variable})"

                fields.append(
                    f"                {relationship_name!r}: {value},"
                )
                continue

            # Campos conocidos por nombre
            if name == "name":
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
            elif field_type in ("string", "varchar", "char"):
                value = "fake.word()"

            elif field_type in ("text", "longtext"):
                value = "fake.text(max_nb_chars=200)"

            elif field_type in ("integer", "biginteger", "smallinteger"):
                value = "fake.random_int(min=1, max=100)"

            elif field_type in ("float", "double"):
                value = (
                    "fake.pyfloat("
                    "left_digits=3, right_digits=2, positive=True)"
                )

            elif field_type == "decimal":
                precision = column.get("precision") or 10
                scale = column.get("scale")
                if scale is None:
                    scale = 2

                value = (
                    f"fake.pydecimal("
                    f"left_digits={precision - scale}, "
                    f"right_digits={scale}, positive=True)"
                )

            elif field_type in ("boolean", "bool"):
                value = "fake.pybool()"

            elif field_type == "date":
                value = "fake.date_object()"

            elif field_type in ("datetime", "timestamp"):
                value = "fake.date_time()"

            elif field_type == "uuid":
                value = "fake.uuid4()"

            else:
                raise ValueError(
                    f"Tipo de campo no soportado: {name} ({field_type})"
                )

            fields.append(f"                {name!r}: {value},")

        return "\n".join(fields)



    @staticmethod
    def get_fk_imports(columns):
        """
        Genera los imports de los modelos relacionados.
        """
        imports = set()

        for column in columns:
            if not column.get("is_fk"):
                continue

            name = column["name"]
            related_model = column.get("related_model")

            if not related_model:
                raise ValueError(
                    f"Falta related_model en {name}"
                )

            if related_model == "User":
                imports.add(
                    "from django.contrib.auth import get_user_model"
                )
            else:
                related_table = column.get("related_table")

                if not related_table:
                    raise ValueError(
                        f"Falta related_table en {name}"
                    )

                imports.add(
                    f"from apps.{related_table}.models "
                    f"import {related_model}"
                )

        return "\n".join(sorted(imports))



    @staticmethod
    def get_fk_setup(columns):
        """
        Obtiene todos los registros relacionados para las FK.
        """
        lines = []

        for column in columns:
            if not column.get("is_fk"):
                continue

            name = column["name"]
            related_model = column.get("related_model")
            related_table = column.get("related_table")

            if not related_model or not related_table:
                raise ValueError(
                    f"Faltan datos de relación en {name}"
                )

            variable = f"related_{related_table}"

            if related_model == "User":
                model_expression = "get_user_model()"
            else:
                model_expression = related_model

            lines.append(
                f"        {variable} = list("
                f"{model_expression}.objects.all())"
            )

            lines.append(
                f"        if not {variable}:"
            )

            lines.append(
                f'            raise CommandError('
                f'"No hay registros relacionados para {name}.")'
            )

        return "\n".join(lines)