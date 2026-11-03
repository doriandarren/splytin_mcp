
class HelperReactTsCreate:

    @staticmethod
    def get_default_value(column):
        """
        Genera el valor inicial de una columna.
        """

        if column.get("is_nullable", False):
            return "null"

        if column.get("type") == "boolean":
            return "false"

        if column.get("type") in (
            "integer", "int", "bigint", "smallint",
            "decimal", "float", "double", "fk"
        ) or column.get("is_fk", False):
            return "0"

        return '""'



    @staticmethod
    def generate_form_initial_values(columns):
        """
        Genera los valores iniciales del formulario.
        """

        result = []
        excluded = {"id", "created_at", "updated_at"}
        existing_names = set()

        for column in columns:
            name = column["name"]

            if name in excluded or name in existing_names:
                continue

            existing_names.add(name)

            result.append(
                f"    {name}: "
                f"{HelperReactTsCreate.get_default_value(column)},"
            )

        return "\n".join(result)



    @staticmethod
    def generate_form_field(column):
        """
        Genera un campo JSX compatible con
        React Hook Form y Zod.
        """

        name = column["name"]
        column_type = column.get("type", "string")
        is_nullable = column.get("is_nullable", False)
        is_unsigned = column.get("is_unsigned", False)
        size = column.get("size")

        # Booleanos
        if column_type == "boolean":
            return f'''          {{/* {name} */}}
            <div className="space-y-2">
                <Label htmlFor="{name}">{name}</Label>

                <Input
                id="{name}"
                type="checkbox"
                {{...register("{name}")}}
                aria-invalid={{!!errors.{name}}}
                className="size-4"
                />

                {{errors.{name} && (
                <p className="text-sm text-destructive">
                    {{errors.{name}.message}}
                </p>
                )}}
            </div>'''

        # Números y claves foráneas
        if column_type in (
            "integer", "int", "bigint", "smallint",
            "decimal", "float", "double", "fk"
        ) or column.get("is_fk", False):

            step = (
                "any"
                if column_type in ("decimal", "float", "double")
                else "1"
            )

            min_attribute = (
                '\n              min="0"'
                if is_unsigned
                else ""
            )

            return f'''          {{/* {name} */}}
            <div className="space-y-2">
                <Label htmlFor="{name}">{name}</Label>

                <Input
                id="{name}"
                type="number"
                step="{step}"{min_attribute}
                {{...register("{name}", {{
                    setValueAs: (value) =>
                    value === ""
                        ? {"null" if is_nullable else "NaN"}
                        : Number(value),
                }})}}
                aria-invalid={{!!errors.{name}}}
                />

                {{errors.{name} && (
                <p className="text-sm text-destructive">
                    {{errors.{name}.message}}
                </p>
                )}}
            </div>'''

        # Textos y fechas
        input_type = "text"

        if column_type == "date":
            input_type = "date"

        elif column_type == "time":
            input_type = "time"

        elif column_type in ("datetime", "timestamp"):
            input_type = "datetime-local"

        max_length = (
            f'\n              maxLength={{{size}}}'
            if size is not None and column_type == "string"
            else ""
        )

        register_options = (
            f'''{{...register("{name}", {{
                    setValueAs: (value) =>
                    value === "" ? null : value,
                }})}}'''
            if is_nullable
            else f'{{...register("{name}")}}'
        )

        return f'''          {{/* {name} */}}
            <div className="space-y-2">
                <Label htmlFor="{name}">{name}</Label>

                <Input
                id="{name}"
                type="{input_type}"
                {register_options}
                aria-invalid={{!!errors.{name}}}{max_length}
                />

                {{errors.{name} && (
                <p className="text-sm text-destructive">
                    {{errors.{name}.message}}
                </p>
                )}}
            </div>'''



    @staticmethod
    def generate_form_fields(columns):
        """
        Genera los campos JSX para React Hook Form.
        """

        result = []
        excluded = {"id", "created_at", "updated_at"}
        existing_names = set()

        for column in columns:
            name = column["name"]

            if name in excluded or name in existing_names:
                continue

            existing_names.add(name)

            result.append(
                HelperReactTsCreate.generate_form_field(column)
            )

        return "\n\n".join(result)



