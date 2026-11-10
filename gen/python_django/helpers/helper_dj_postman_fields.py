
class HelperDjPostmanFields:

    @staticmethod
    def store(columns):
        """
        Genera los atributos JSON:API para crear un registro.
        """
        attributes = {}

        for column in columns:
            name = column["name"]
            column_type = column.get("type") or column.get("raw_type")
            is_fk = column.get("is_fk", False)

            if is_fk:
                value = 1

            elif column_type in ("string", "text", "varchar"):
                value = f"New {name}"

                size = column.get("size")
                if size is not None:
                    value = value[:size]

            elif column_type in ("integer", "bigint", "smallint"):
                value = 1

            elif column_type in ("decimal", "float", "double"):
                value = 10.5

            elif column_type == "boolean":
                value = True

            elif column_type == "date":
                value = "2026-01-01"

            elif column_type == "datetime":
                value = "2026-01-01T12:00:00Z"

            elif column_type == "json":
                value = {}

            else:
                value = None if column.get("is_nullable") else f"New {name}"

            attributes[name] = value

        return attributes

    @staticmethod
    def update(columns):
        """
        Genera los atributos JSON:API para actualizar un registro.
        """
        attributes = {}

        for column in columns:
            name = column["name"]
            column_type = column.get("type") or column.get("raw_type")
            is_fk = column.get("is_fk", False)

            if is_fk:
                value = 1

            elif column_type in ("string", "text", "varchar"):
                value = f"Update {name}"

                size = column.get("size")
                if size is not None:
                    value = value[:size]

            elif column_type in ("integer", "bigint", "smallint"):
                value = 1

            elif column_type in ("decimal", "float", "double"):
                value = 10.5

            elif column_type == "boolean":
                value = True

            elif column_type == "date":
                value = "2026-01-01"

            elif column_type == "datetime":
                value = "2026-01-01T12:00:00Z"

            elif column_type == "json":
                value = {}

            else:
                value = None if column.get("is_nullable") else f"Update {name}"

            attributes[name] = value

        return attributes
