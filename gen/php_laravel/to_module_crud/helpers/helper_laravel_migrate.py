
class HelperLaravelMigrate:

    @staticmethod
    def php_column_line(col: dict) -> str:
        """
        Traduce un tipo interno a Blueprint de Laravel.

        Soporta:
        - string, email, text
        - integer, float, decimal, boolean
        - fk
        - date, datetime, time, timestamp

        Opciones:
        - size
        - precision
        - scale
        - is_nullable
        - is_unique
        - is_index
        - is_unsigned
        """

        name = col["name"]
        t = (col.get("type") or "string").lower()

        is_fk = col.get("is_fk", False) or t == "fk"
        is_nullable = col.get("is_nullable", False)
        is_unique = col.get("is_unique", False)
        is_index = col.get("is_index", False)
        is_unsigned = col.get("is_unsigned", False)

        size = col.get("size") or 255
        precision = col.get("precision") or 13
        scale = col.get("scale")
        scale = 2 if scale is None else scale

        # ---------------------------------
        # Foreign Key
        # ---------------------------------

        if is_fk:
            line = f"$table->unsignedBigInteger('{name}')"

        # ---------------------------------
        # String / Email
        # ---------------------------------

        elif t in {"string", "email"}:
            line = f"$table->string('{name}', {size})"

        # ---------------------------------
        # Text
        # ---------------------------------

        elif t == "text":
            line = f"$table->text('{name}')"

        # ---------------------------------
        # Integer
        # ---------------------------------

        elif t == "integer":
            line = f"$table->integer('{name}')"

            if is_unsigned:
                line += "->unsigned()"

            line += "->default(0)"

        # ---------------------------------
        # Float
        # ---------------------------------

        elif t == "float":
            line = f"$table->float('{name}')->default(0.0)"

        # ---------------------------------
        # Decimal
        # ---------------------------------

        elif t == "decimal":
            line = f"$table->decimal('{name}', {precision}, {scale})"

            if is_unsigned:
                line += "->unsigned()"

            line += "->default(0)"

        # ---------------------------------
        # Boolean
        # ---------------------------------

        elif t == "boolean":
            line = f"$table->boolean('{name}')->default(false)"

        # ---------------------------------
        # Date / Time
        # ---------------------------------

        elif t == "date":
            line = f"$table->date('{name}')"

        elif t == "datetime":
            line = f"$table->dateTime('{name}')"

        elif t == "time":
            line = f"$table->time('{name}')"

        elif t == "timestamp":
            line = f"$table->timestamp('{name}')"

        # ---------------------------------
        # Fallback
        # ---------------------------------

        else:
            raise ValueError(
                f"Tipo de columna no soportado: '{t}'"
            )

        # ---------------------------------
        # Nullable
        # ---------------------------------

        if is_nullable:
            line += "->nullable()"

        # ---------------------------------
        # Unique
        # ---------------------------------

        if is_unique:
            line += "->unique()"

        # ---------------------------------
        # Index
        # ---------------------------------

        if is_index and not is_unique:
            line += "->index()"

        # ---------------------------------
        # Resultado
        # ---------------------------------

        return f"                {line};\n"
