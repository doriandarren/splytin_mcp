import os
import json


class HelperLaravelPostman:

    @staticmethod
    def create_postman_structure(base_ruta: str) -> str:
        """
        Crea la estructura de carpetas 'base_ruta/public/Scripts'
        en la ruta especificada.
        """

        postman_folder_path = os.path.join(
            base_ruta,
            "public",
            "Scripts"
        )

        if not os.path.exists(postman_folder_path):
            os.makedirs(postman_folder_path)

            print(
                f"Estructura de carpetas '{postman_folder_path}' creada."
            )

        return postman_folder_path




    @staticmethod
    def generate_index_query_params(columns: list[dict]) -> list[dict]:
        query_params = [
            {
                "key": "include",
                "value": "",
                "description": "Relationship",
                "disabled": True
            }
        ]

        for column in columns:
            query_params.append({
                "key": f"filter[{column['name']}]",
                "value": "term",
                "description": f"Filter by {column['name']}",
                "disabled": True
            })

        query_params.append({
            "key": "filter[created_at]",
            "value": "2026-08-01,2026-09-20",
            "description": "Range by created_at",
            "disabled": True
        })

        query_params.append({
            "key": "filter[updated_at]",
            "value": "2026-08-01,2026-09-20",
            "description": "Range by updated_at",
            "disabled": True
        })

        for column in columns:
            query_params.append({
                "key": "sort",
                "value": f"{column['name']}",
                "description": f"Sort by {column['name']}",
                "disabled": True
            })

        query_params.append({
            "key": "sort",
            "value": "-created_at",
            "description": "Sort by created_at",
            "disabled": True
        })

        return query_params



    @staticmethod
    def create_store_relationships(
        columns: list[dict],
        plural_name_kebab: str
    ) -> str:

        attributes = {}
        relationships = {}

        data = {
            "type": plural_name_kebab,
            "attributes": attributes
        }

        for column in columns:

            # Attributes
            if column["is_fk"]:
                attributes[column["name"]] = 1

            elif column["type"] == "decimal":
                attributes[column["name"]] = "100.20"

            elif column["type"] == "float":
                attributes[column["name"]] = "26.30"

            elif column["type"] == "integer":
                attributes[column["name"]] = 6

            elif column["type"] == "boolean":
                attributes[column["name"]] = 1

            else:
                attributes[column["name"]] = f"New {column['name']}"

            # Relationships
            if column["is_fk"]:
                relationships[column["relationship_name"]] = {
                    "data": {
                        "type": column["related_table"],
                        "id": "1"
                    }
                }

        if relationships:
            data["relationships"] = relationships

        return json.dumps({
            "data": data
        }, indent=4)



    @staticmethod
    def create_update_relationships(
        columns: list[dict],
        plural_name_kebab: str
    ) -> str:

        attributes = {}
        relationships = {}

        data = {
            "type": plural_name_kebab,
            "id": "1",
            "attributes": attributes
        }

        for column in columns:

            # Attributes
            if column["is_fk"]:
                attributes[column["name"]] = 1

            elif column["type"] == "decimal":
                attributes[column["name"]] = "100.20"

            elif column["type"] == "float":
                attributes[column["name"]] = "26.30"

            elif column["type"] == "integer":
                attributes[column["name"]] = 4

            elif column["type"] == "boolean":
                attributes[column["name"]] = 1

            else:
                attributes[column["name"]] = f"Update {column['name']}"

            # Relationships
            if column["is_fk"]:
                relationships[column["relationship_name"]] = {
                    "data": {
                        "type": column["related_table"],
                        "id": "1"
                    }
                }

        if relationships:
            data["relationships"] = relationships

        return json.dumps({
            "data": data
        }, indent=4)