def snake_to_pascal(value: str) -> str:
    return "".join(word.capitalize() for word in value.split("_"))


def pluralize(word: str) -> str:
    if word.endswith("y") and len(word) > 1 and word[-2].lower() not in "aeiou":
        return word[:-1] + "ies"

    if word.endswith(("s", "x", "z", "ch", "sh")):
        return word + "es"

    return word + "s"


def normalize_column_type(col_type: str):
    col_type = col_type.lower().strip()

    if col_type.startswith("varchar"):
        return "string"

    if col_type.startswith("char"):
        return "string"

    if col_type in {"int", "integer"} or col_type.startswith("int"):
        return "integer"

    if col_type.startswith("bigint"):
        return "integer"

    if col_type.startswith("tinyint(1)"):
        return "boolean"

    if col_type.startswith("tinyint"):
        return "integer"

    if col_type.startswith("decimal"):
        return "decimal"

    if col_type.startswith("float"):
        return "float"

    if col_type.startswith("double"):
        return "float"

    if col_type in {"text", "tinytext", "mediumtext", "longtext"}:
        return "text"

    if col_type == "date":
        return "date"

    if col_type == "datetime":
        return "datetime"

    if col_type == "timestamp":
        return "timestamp"

    return col_type


def parse_columns_input(input_columns: str):
    """
    Convierte un string tipo:

    customer_id:fk
    name:string(255)|unique
    amount:decimal(10,2)|nullable
    country_id:fk|unique|string(255)
    description
    has_active:boolean

    en una lista de diccionarios.
    """

    allowed_types = {
        "string",
        "text",
        "integer",
        "float",
        "decimal",
        "boolean",
        "fk",
        "date",
        "datetime",
        "email",
        "timestamp"
    }

    allowed_options = {
        "fk",
        "unique",
        "nullable",
        "index",
        "unsigned"
    }

    columns = []

    for token in input_columns.split():

        # ---------------------------------
        # Separar nombre de configuración
        # ---------------------------------

        parts = token.split(":", 1)

        name = parts[0].strip()

        raw_options = (
            parts[1].strip()
            if len(parts) > 1
            else "string"
        )

        # ---------------------------------
        # Separar opciones por |
        # ---------------------------------

        options = [
            option.strip()
            for option in raw_options.split("|")
            if option.strip()
        ]

        # ---------------------------------
        # Valores por defecto
        # ---------------------------------

        col_type = None
        raw_col_type = None

        size = None
        precision = None
        scale = None

        is_fk = False
        is_unique = False
        is_nullable = False
        is_index = False
        is_unsigned = False

        # ---------------------------------
        # Procesar cada opción
        # ---------------------------------

        for option in options:

            option_lower = option.lower().strip()

            # -----------------------------
            # Modificadores
            # -----------------------------

            if option_lower in allowed_options:

                if option_lower == "fk":
                    is_fk = True

                elif option_lower == "unique":
                    is_unique = True

                elif option_lower == "nullable":
                    is_nullable = True

                elif option_lower == "index":
                    is_index = True

                elif option_lower == "unsigned":
                    is_unsigned = True

                continue

            # -----------------------------
            # Detectar tipo y parámetros
            # -----------------------------

            type_without_size = option
            params = None

            if "(" in option and ")" in option:

                type_without_size = option.split("(", 1)[0]

                params = (
                    option
                    .split("(", 1)[1]
                    .split(")", 1)[0]
                )

            normalized_type = normalize_column_type(
                type_without_size
            )

            # -----------------------------
            # Validar tipo
            # -----------------------------

            if normalized_type not in allowed_types:
                raise ValueError(
                    f"Tipo u opción no soportado: "
                    f"'{option}' en '{token}'"
                )

            col_type = normalized_type
            raw_col_type = option

            # -----------------------------
            # string(255)
            # -----------------------------

            if col_type in {"string", "email"}:

                if params and params.isdigit():
                    size = int(params)

            # -----------------------------
            # decimal(10,2)
            # -----------------------------

            elif col_type == "decimal":

                if params:

                    decimal_parts = [
                        value.strip()
                        for value in params.split(",")
                    ]

                    if (
                        len(decimal_parts) >= 1
                        and decimal_parts[0].isdigit()
                    ):
                        precision = int(decimal_parts[0])

                    if (
                        len(decimal_parts) >= 2
                        and decimal_parts[1].isdigit()
                    ):
                        scale = int(decimal_parts[1])

        # ---------------------------------
        # Si solamente viene fk
        # ---------------------------------

        if col_type is None:

            if is_fk:
                col_type = "fk"
                raw_col_type = "fk"

            else:
                col_type = "string"
                raw_col_type = "string"

        # ---------------------------------
        # Tamaño por defecto
        # ---------------------------------

        if size is None and col_type in {"string", "email"}:
            size = 255

        # ---------------------------------
        # Create Object
        # ---------------------------------

        col = {
            "name": name,

            "type": col_type,
            "raw_type": raw_col_type,

            "size": size,
            "precision": precision,
            "scale": scale,

            "is_fk": is_fk,
            "is_unique": is_unique,
            "is_nullable": is_nullable,
            "is_index": is_index,
            "is_unsigned": is_unsigned,

            "options": options,
        }

        # ---------------------------------
        # Foreign Key
        # ---------------------------------

        if col["is_fk"]:

            base = name

            if base.endswith("_id"):
                base = base[:-3]

            col["related_table"] = pluralize(base)
            col["related_model"] = snake_to_pascal(base)
            col["relationship_name"] = base

        columns.append(col)

    return columns