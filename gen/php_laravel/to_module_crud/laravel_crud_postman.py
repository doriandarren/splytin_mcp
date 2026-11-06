
import os
import json

from gen.helpers.helper_file import HelperFile
from gen.php_laravel.to_module_crud.helpers.helper_laravel_postman import HelperLaravelPostman


class LaravelCrudPostman:

    def invoke(
        self,
        full_path: str,
        singular_name: str,
        plural_name: str,
        singular_name_kebab: str,
        plural_name_kebab: str,
        columns: list[dict]
    ) -> None:
        """
        Genera una colección Postman para un CRUD de Laravel
        utilizando el formato JSON:API.
        """

        # ---------------------------------
        # Ruta y nombre del archivo
        # ---------------------------------

        folder_path = os.path.join(full_path)

        plural_name_kebab = plural_name_kebab.rstrip("/")

        file_name = f"{singular_name}Collection.json"

        # ---------------------------------
        # Helpers
        # ---------------------------------

        query_params = HelperLaravelPostman.generate_index_query_params(
            columns
        )

        store_body_params = HelperLaravelPostman.create_store_relationships(
            columns,
            plural_name_kebab
        )

        update_body_params = HelperLaravelPostman.create_update_relationships(
            columns,
            plural_name_kebab
        )

        # ---------------------------------
        # Headers JSON:API
        # ---------------------------------

        headers = [
            {
                "key": "Accept",
                "value": "application/vnd.api+json",
                "type": "text"
            },
            {
                "key": "Authorization",
                "value": "Bearer {{token_api}}",
                "type": "text"
            }
        ]

        headers_with_body = [
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
                "value": "Bearer {{token_api}}",
                "type": "text"
            }
        ]

        # ---------------------------------
        # Base URL
        # ---------------------------------

        base_url = f"{{{{base_url}}}}{plural_name_kebab}"

        # ---------------------------------
        # Crear estructura Postman
        # ---------------------------------

        postman_content = {
            "info": {
                "_postman_id": "1e8ef847-456f-4806-9ab0-c4b861fe675d",
                "name": singular_name,
                "schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json",
                "_exporter_id": "5599797"
            },

            "item": [
                {
                    "name": plural_name,

                    "item": [

                        # =========================
                        # INDEX
                        # =========================

                        {
                            "name": "Index",

                            "protocolProfileBehavior": {
                                "disableBodyPruning": True
                            },

                            "request": {
                                "method": "GET",

                                "header": headers,

                                "url": {
                                    "raw": base_url,
                                    "host": [
                                        base_url
                                    ],
                                    "query": query_params
                                }
                            },

                            "response": []
                        },

                        # =========================
                        # SHOW
                        # =========================

                        {
                            "name": "Show",

                            "protocolProfileBehavior": {
                                "disableBodyPruning": True
                            },

                            "request": {
                                "method": "GET",

                                "header": headers,

                                "url": {
                                    "raw": f"{base_url}/1",
                                    "host": [
                                        base_url
                                    ],
                                    "path": [
                                        "1"
                                    ]
                                }
                            },

                            "response": []
                        },

                        # =========================
                        # STORE
                        # =========================

                        {
                            "name": "Store",

                            "request": {
                                "method": "POST",

                                "header": headers_with_body,

                                "body": {
                                    "mode": "raw",
                                    "raw": store_body_params,

                                    "options": {
                                        "raw": {
                                            "language": "json"
                                        }
                                    }
                                },

                                "url": {
                                    "raw": base_url,
                                    "host": [
                                        base_url
                                    ]
                                }
                            },

                            "response": []
                        },

                        # =========================
                        # UPDATE
                        # =========================

                        {
                            "name": "Update",

                            "request": {
                                "method": "PATCH",

                                "header": headers_with_body,

                                "body": {
                                    "mode": "raw",
                                    "raw": update_body_params,

                                    "options": {
                                        "raw": {
                                            "language": "json"
                                        }
                                    }
                                },

                                "url": {
                                    "raw": f"{base_url}/1",
                                    "host": [
                                        base_url
                                    ],
                                    "path": [
                                        "1"
                                    ]
                                }
                            },

                            "response": []
                        },

                        # =========================
                        # DELETE
                        # =========================

                        {
                            "name": "Delete",

                            "request": {
                                "method": "DELETE",

                                "header": headers,

                                "url": {
                                    "raw": f"{base_url}/1",
                                    "host": [
                                        base_url
                                    ],
                                    "path": [
                                        "1"
                                    ]
                                }
                            },

                            "response": []
                        }

                    ]
                }
            ]
        }

        # ---------------------------------
        # Convertir a JSON
        # ---------------------------------

        content = json.dumps(
            postman_content,
            indent=4,
            ensure_ascii=False
        )

        # ---------------------------------
        # Crear archivo
        # ---------------------------------

        HelperFile.write(
            folder_path=folder_path,
            file_name=file_name,
            content=content
        )
