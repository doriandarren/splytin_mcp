import os


class HelperLaravelRequest:


    ##############################
    ## Para el Store  ############
    ##############################

    @staticmethod
    def create_request_validation_rules(
        columns: list[dict],
        singular_name: str,
        singular_name_camel: str,
        singular_name_snake: str,
        plural_name_snake: str
    ) -> str:

        validation_rules = ""

        rules_by_type = {
            "string": ["required", "string"],
            "text": ["required", "string"],
            "integer": ["required", "integer"],
            "float": ["required", "numeric"],
            "decimal": ["required", "numeric"],
            "boolean": ["required", "boolean"],
            "date": ["required", "date"],
            "datetime": ["required", "date"],
            "timestamp": ["required", "date"],
            "email": ["required", "email"],
        }

        for index, column in enumerate(columns):

            column_type = column["type"]

            # ---------------------------------
            # Reglas base
            # ---------------------------------

            if column_type == "fk":
                rules = [
                    "required",
                    "integer",
                    f"exists:{column['related_table']},id",
                ]

            else:
                rules = rules_by_type.get(
                    column_type,
                    ["required"]
                ).copy()

                # Tamaño
                if (
                    column_type in {"string", "email"}
                    and column.get("size")
                ):
                    rules.append(
                        f"max:{column['size']}"
                    )

            # ---------------------------------
            # Nullable
            # ---------------------------------

            if column.get("is_nullable"):
                rules[0] = "nullable"

            # ---------------------------------
            # Generar array PHP
            # ---------------------------------

            if column_type == "fk":
                validation_rules += (
                    f"            'data.relationships.{column['relationship_name']}.data.id' => [\n"
                )
            else:
                validation_rules += (
                    f"            'data.attributes.{column['name']}' => [\n"
                )

            for rule in rules:
                validation_rules += (
                    f"                '{rule}',\n"
                )

            # ---------------------------------
            # Unique
            # ---------------------------------

            if column.get("is_unique"):
                validation_rules += (
                    f"                'unique:{plural_name_snake},{column['name']}',\n"
                )

            validation_rules += "            ],"

            # Salto de línea excepto último
            if index != len(columns) - 1:
                validation_rules += "\n"

        return validation_rules

    @staticmethod
    def create_attribute_map(columns: list[dict]) -> str:

        lines = []

        for column in columns:
            name = column["name"]

            if column["type"] == "fk":
                lines.append(
                    f"        'data.relationships.{column['relationship_name']}.data.id' => '{name}',"
                )
            else:
                lines.append(
                    f"        'data.attributes.{name}' => '{name}',"
                )

        content = """    protected array $attributeMap = [
"""
        content += "\n".join(lines)
        content += """
    ];"""

        return content

    @staticmethod
    def get_folder_path(
        full_path: str,
        version_api: str,
        plural_name: str
    ) -> str:

        return os.path.join(
            full_path,
            "app",
            "Http",
            "Requests",
            version_api,
            plural_name
        )



    ##############################
    ## Para el Update ############
    ##############################
    
    @staticmethod
    def generate_update_validation_rules(
        columns: list[dict],
        singular_name: str,
        singular_name_camel: str,
        singular_name_snake: str,
        plural_name_snake: str
    ) -> str:

        validation_rules = ""

        rules_by_type = {
            "string": ["sometimes", "string"],
            "text": ["sometimes", "string"],
            "integer": ["sometimes", "integer"],
            "float": ["sometimes", "numeric"],
            "decimal": ["sometimes", "numeric"],
            "boolean": ["sometimes", "boolean"],
            "date": ["sometimes", "date"],
            "datetime": ["sometimes", "date"],
            "timestamp": ["sometimes", "date"],
            "email": ["sometimes", "email"],
        }

        for index, column in enumerate(columns):

            column_type = column["type"]

            # ---------------------------------
            # Reglas base
            # ---------------------------------

            if column_type == "fk":
                rules = [
                    "sometimes",
                    "integer",
                    f"exists:{column['related_table']},id",
                ]

            else:
                rules = rules_by_type.get(
                    column_type,
                    ["sometimes"]
                ).copy()

                # Tamaño
                if (
                    column_type in {"string", "email"}
                    and column.get("size")
                ):
                    rules.append(
                        f"max:{column['size']}"
                    )

            # ---------------------------------
            # Nullable
            # ---------------------------------

            if column.get("is_nullable"):
                rules[0] = "nullable"

            # ---------------------------------
            # Generar array PHP
            # ---------------------------------

            if column_type == "fk":
                validation_rules += (
                    f"            'data.relationships.{column['relationship_name']}.data.id' => [\n"
                )
            else:
                validation_rules += (
                    f"            'data.attributes.{column['name']}' => [\n"
                )

            for rule in rules:
                validation_rules += (
                    f"                '{rule}',\n"
                )

            # ---------------------------------
            # Unique
            # ---------------------------------

            if column.get("is_unique"):
                validation_rules += (
                    f"                Rule::unique("
                    f"'{plural_name_snake}', "
                    f"'{column['name']}'"
                    f")->ignore("
                    f"$this->route('{singular_name_snake}')"
                    f"),\n"
                )

            validation_rules += "            ],"

            # Salto de línea excepto último
            if index != len(columns) - 1:
                validation_rules += "\n"

        return validation_rules
