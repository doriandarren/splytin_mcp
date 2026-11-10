
class HelperDjSerializerFields:

    @staticmethod
    def get_columns(columns):
        """
        Genera los campos del serializer.
        """
        return "\n".join(
            f"            '{column['name']}',"
            for column in columns
        )

    @staticmethod
    def get_extra_kwargs(columns):
        """
        Genera las validaciones extra_kwargs del serializer.
        """
        lines = []

        for column in columns:
            name = column["name"]
            column_type = column.get("type") or column.get("raw_type")
            is_nullable = column.get("is_nullable", False)
            size = column.get("size")
            min_length = column.get("min_length")

            lines.append(f'            "{name}": {{')

            # Required
            lines.append(
                f'                "required": {not is_nullable},'
            )

            # Nullable
            if is_nullable:
                lines.append(
                    '                "allow_null": True,'
                )

            # String validations
            if column_type in ("string", "text", "varchar"):

                if min_length is not None:
                    lines.append(
                        f'                "min_length": {min_length},'
                    )

                if size is not None:
                    lines.append(
                        f'                "max_length": {size},'
                    )

                lines.append(
                    '                "allow_blank": False,'
                )

            lines.append("            },")

        return "\n".join(lines)
