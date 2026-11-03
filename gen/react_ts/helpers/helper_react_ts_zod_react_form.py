import json


class HelperReactTsZodReactForm:

    @staticmethod
    def get_zod_validation(column):
        """
        Genera la validación Zod según
        el tipo y las propiedades de la columna.
        """

        name = column["name"]
        column_type = column.get("type", "string")
        is_nullable = column.get("is_nullable", False)
        is_unsigned = column.get("is_unsigned", False)
        size = column.get("size")
        precision = column.get("precision")
        scale = column.get("scale")

        # Claves foráneas
        if column.get("is_fk", False) or column_type == "fk":
            validation = (
                f'z.number()'
                f'.int("{name} debe ser un entero")'
                f'.positive("{name} debe ser mayor que 0")'
            )

        # Textos
        elif column_type in (
            "string", "text", "char", "uuid", "enum"
        ):
            validation = "z.string().trim()"

            if not is_nullable:
                validation += (
                    f'.min(1, "{name} es obligatorio")'
                )

            if size is not None:
                validation += (
                    f'.max({size}, '
                    f'"{name} no puede superar {size} caracteres")'
                )

            if column_type == "uuid":
                validation += (
                    f'.uuid("{name} debe ser un UUID válido")'
                )

        # Números enteros
        elif column_type in (
            "integer", "int", "bigint", "smallint",
            "tinyint", "mediumint"
        ):
            validation = (
                f'z.number()'
                f'.int("{name} debe ser un entero")'
            )

            if is_unsigned:
                validation += (
                    f'.min(0, "{name} no puede ser negativo")'
                )

        # Decimales
        elif column_type == "decimal":
            validation = "z.number()"

            if is_unsigned:
                validation += (
                    f'.min(0, "{name} no puede ser negativo")'
                )

            if precision is not None and scale is not None:
                validation += (
                    f'.refine('
                    f'(value) => '
                    f'Math.abs(value) < Math.pow(10, {precision - scale}), '
                    f'{{{{ message: "{name} supera la precisión permitida" }}}}'
                    f')'
                )

            if scale is not None:
                validation += (
                    f'.refine('
                    f'(value) => '
                    f'Math.abs(value * Math.pow(10, {scale}) - '
                    f'Math.round(value * Math.pow(10, {scale}))) < 1e-7, '
                    f'{{{{ message: "{name} admite máximo {scale} decimales" }}}}'
                    f')'
                )

        # Números flotantes
        elif column_type in ("float", "double", "real"):
            validation = "z.number()"

            if is_unsigned:
                validation += (
                    f'.min(0, "{name} no puede ser negativo")'
                )

        # Booleanos
        elif column_type == "boolean":
            validation = "z.boolean()"

        # Fechas
        elif column_type == "date":
            validation = "z.iso.date()"

        elif column_type in ("datetime", "timestamp"):
            validation = "z.iso.datetime({ offset: true })"

        elif column_type == "time":
            validation = "z.iso.time()"

        # JSON
        elif column_type == "json":
            validation = "z.record(z.string(), z.unknown())"

        # Otros tipos
        else:
            validation = "z.string()"

            if not is_nullable:
                validation += (
                    f'.min(1, "{name} es obligatorio")'
                )

        # Permitir null
        if is_nullable:
            validation += ".nullable()"

        return validation

    @staticmethod
    def generate_schema_fields(columns):
        """
        Genera todos los campos del esquema Zod.
        """

        result = []

        excluded = {"id", "created_at", "updated_at"}
        existing_names = set()

        for column in columns:
            name = column["name"]

            if name in excluded or name in existing_names:
                continue

            existing_names.add(name)

            validation = HelperReactTsZodReactForm.get_zod_validation(
                column
            )

            result.append(
                f"  {json.dumps(name, ensure_ascii=False)}: {validation},"
            )

        return "\n".join(result)
