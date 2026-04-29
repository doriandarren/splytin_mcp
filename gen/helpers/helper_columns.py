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

    if col_type.startswith("text"):
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
    'customer_id:fk name:string amount:float description has_active:boolean'
    en una lista de diccionarios bien formados.
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

    columns = []

    for token in input_columns.split():
        parts = token.split(":")

        name = parts[0].strip()
        raw_col_type = parts[1].strip() if len(parts) > 1 else "string"

        col_type = normalize_column_type(raw_col_type)

        if col_type not in allowed_types:
            raise ValueError(f"Tipo de columna no soportado: '{raw_col_type}' en '{token}'")

        col = {
            "name": name,
            "type": col_type,
            "raw_type": raw_col_type,
            "is_fk": col_type == "fk",
        }

        if col["is_fk"]:
            base = name
            if base.endswith("_id"):
                base = base[:-3]

            col["related_table"] = pluralize(base)
            col["related_model"] = snake_to_pascal(base)

        columns.append(col)

    return columns