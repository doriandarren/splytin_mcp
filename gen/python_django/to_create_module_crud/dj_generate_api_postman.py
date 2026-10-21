
import os
import json
import uuid

from gen.helpers.helper_file import HelperFile


class DjGenerateApiPostman:

    def invoke(
        self,
        full_path,
        project_name,
        singular_name,
        plural_name,
        singular_name_kebab,
        plural_name_kebab,
        singular_name_snake,
        plural_name_snake,
        singular_first_camel,
        plural_first_camel,
        columns,
    ):
        """
        Genera la colección Postman del módulo CRUD.
        """

        folder_path = os.path.join(full_path, "SCRIPTS")

        # Obtener los nombres de las columnas dinámicamente
        column_names = [column["name"] for column in columns]

        # Encabezados JSON:API
        headers = [
            {
                "key": "Accept",
                "value": "application/vnd.api+json",
                "type": "text"
            },
            {
                "key": "Content-Type",
                "value": "application/vnd.api+json",
                "type": "text"
            },
            {
                "key": "Authorization",
                "value": "Token {{token_api}}",
                "type": "text"
            }
        ]

        # URL base del módulo
        base_url = f"{{{{base_url}}}}{plural_name_kebab}/"
        detail_url = f"{base_url}1/"

        # Cuerpo de creación JSON:API
        store_body = {
            "data": {
                "type": plural_name_kebab,
                "attributes": {
                    column: f"New {column}"
                    for column in column_names
                }
            }
        }

        # Cuerpo de actualización JSON:API
        update_body = {
            "data": {
                "type": plural_name_kebab,
                "id": "1",
                "attributes": {
                    column: f"Update {column}"
                    for column in column_names
                }
            }
        }

        # Construir la colección
        collection = {
            "info": {
                "_postman_id": str(uuid.uuid4()),
                "name": singular_name,
                "schema": (
                    "https://schema.getpostman.com/json/"
                    "collection/v2.1.0/collection.json"
                ),
            },
            "item": [
                {
                    "name": plural_name,
                    "item": [
                        {
                            "name": "List",
                            "request": {
                                "method": "GET",
                                "header": headers,
                                "url": base_url
                            },
                            "response": []
                        },
                        {
                            "name": "Show",
                            "request": {
                                "method": "GET",
                                "header": headers,
                                "url": detail_url
                            },
                            "response": []
                        },
                        {
                            "name": "Store",
                            "request": {
                                "method": "POST",
                                "header": headers,
                                "body": {
                                    "mode": "raw",
                                    "raw": json.dumps(
                                        store_body,
                                        indent=4,
                                        ensure_ascii=False
                                    ),
                                    "options": {
                                        "raw": {"language": "json"}
                                    }
                                },
                                "url": base_url
                            },
                            "response": []
                        },
                        {
                            "name": "Update",
                            "request": {
                                "method": "PATCH",
                                "header": headers,
                                "body": {
                                    "mode": "raw",
                                    "raw": json.dumps(
                                        update_body,
                                        indent=4,
                                        ensure_ascii=False
                                    ),
                                    "options": {
                                        "raw": {"language": "json"}
                                    }
                                },
                                "url": detail_url
                            },
                            "response": []
                        },
                        {
                            "name": "Delete",
                            "request": {
                                "method": "DELETE",
                                "header": headers,
                                "url": detail_url
                            },
                            "response": []
                        }
                    ]
                }
            ]
        }

        # Convertir el diccionario Python a JSON
        content = json.dumps(
            collection,
            indent=4,
            ensure_ascii=False
        )

        # Crear el archivo
        HelperFile.write(
            folder_path=folder_path,
            file_name=f"{singular_name}Collection.json",
            content=content
        )
