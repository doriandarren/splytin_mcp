import json


class HelperLaravelPostmanCrud:

    ## ---------------------------------
    ## CRUD
    ## ---------------------------------

    @staticmethod
    def create_index(endpoint: str, filters: list | None = None) -> dict:
        """
        Genera el endpoint Index con filtros opcionales.
        """

        return {
            "name": "Index",
            "request": {
                "method": "GET",
                "header": [
                    {
                        "key": "Accept",
                        "value": "application/vnd.api+json"
                    },
                    {
                        "key": "Authorization",
                        "value": "Bearer {{token_api}}"
                    }
                ],
                "url": {
                    "raw": f"{{{{base_url}}}}{endpoint}",
                    "host": [f"{{{{base_url}}}}{endpoint}"],
                    "query": filters or []
                }
            },
            "response": []
        }




    @staticmethod
    def create_show(endpoint: str) -> dict:
        """
        Genera el endpoint Show.
        """

        return {
            "name": "Show",
            "request": {
                "method": "GET",
                "header": [
                    {
                        "key": "Accept",
                        "value": "application/vnd.api+json"
                    },
                    {
                        "key": "Authorization",
                        "value": "Bearer {{token_api}}"
                    }
                ],
                "url": f"{{{{base_url}}}}{endpoint}/1"
            },
            "response": []
        }


    @staticmethod
    def create_store(
        endpoint: str,
        attributes: dict,
        relationships: dict | None = None
    ) -> dict:
        """
        Genera el endpoint Store con JSON:API.
        """

        data = {}

        if attributes:
            data["attributes"] = attributes

        if relationships:
            data["relationships"] = relationships

        return {
            "name": "Store",
            "request": {
                "method": "POST",
                "header": [
                    {
                        "key": "Accept",
                        "value": "application/vnd.api+json"
                    },
                    {
                        "key": "Content-Type",
                        "value": "application/vnd.api+json"
                    },
                    {
                        "key": "Authorization",
                        "value": "Bearer {{token_api}}"
                    }
                ],
                "body": {
                    "mode": "raw",
                    "raw": json.dumps(
                        {"data": data},
                        ensure_ascii=False,
                        indent=4
                    ),
                    "options": {
                        "raw": {
                            "language": "json"
                        }
                    }
                },
                "url": f"{{{{base_url}}}}{endpoint}"
            },
            "response": []
        }


    @staticmethod
    def create_update(
        endpoint: str,
        attributes: dict,
        relationships: dict | None = None
    ) -> dict:
        """
        Genera el endpoint Update con JSON:API.
        """

        data = {}

        if attributes:
            data["attributes"] = attributes

        if relationships:
            data["relationships"] = relationships

        return {
            "name": "Update",
            "request": {
                "method": "PATCH",
                "header": [
                    {
                        "key": "Accept",
                        "value": "application/vnd.api+json"
                    },
                    {
                        "key": "Content-Type",
                        "value": "application/vnd.api+json"
                    },
                    {
                        "key": "Authorization",
                        "value": "Bearer {{token_api}}"
                    }
                ],
                "body": {
                    "mode": "raw",
                    "raw": json.dumps(
                        {"data": data},
                        ensure_ascii=False,
                        indent=4
                    ),
                    "options": {
                        "raw": {
                            "language": "json"
                        }
                    }
                },
                "url": f"{{{{base_url}}}}{endpoint}/1"
            },
            "response": []
        }


    @staticmethod
    def create_delete(endpoint: str) -> dict:
        """
        Genera el endpoint Delete.
        """

        return {
            "name": "Delete",
            "request": {
                "method": "DELETE",
                "header": [
                    {
                        "key": "Accept",
                        "value": "application/vnd.api+json"
                    },
                    {
                        "key": "Authorization",
                        "value": "Bearer {{token_api}}"
                    }
                ],
                "url": f"{{{{base_url}}}}{endpoint}/1"
            },
            "response": []
        }