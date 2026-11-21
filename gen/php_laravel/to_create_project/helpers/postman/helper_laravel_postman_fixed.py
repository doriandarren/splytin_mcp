import json

from gen.php_laravel.to_create_project.helpers.postman.helper_laravel_postman_crud import HelperLaravelPostmanCrud


class HelperLaravelPostmanFixed:
    
    
    @staticmethod
    def create_info(project_name: str) -> dict:
        """
        Genera la información principal de la colección Postman.
        """

        return {
            "_postman_id": "c45bcd65-d68b-4fbe-a0b6-b87a5632cbff",
            "name": "API",
            "description": (
                "Api Rest Full\n\n"
                f"Api URL:\n\nhttps://{project_name}/api/\n\n"
                "Estructura principales de ENDPOINT para la gestión:\n\n"
                "- GET base_url/resource\n"
                "- GET base_url/resource/id\n"
                "- POST base_url/resource\n"
                "- PATCH base_url/resource/id\n"
                "- DELETE base_url/resource/id"
            ),
            "schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json",
            "_exporter_id": "5599797",
            "_collection_link": (
                "https://warped-satellite-11290.postman.co/"
                f"workspace/{project_name}t~ae865b4b-fd0c-416a-bcd9-0c9108578f23/"
                "collection/5599797-c45bcd65-d68b-4fbe-a0b6-b87a5632cbff"
                "?action=share&source=collection_link&creator=5599797"
            )
        }


    @staticmethod
    def create_auth_reset_password(domain_name: str) -> dict:
        """
        Genera los endpoints de recuperación de contraseña.
        """

        return {
            "name": "Reset Password",
            "item": [
                {
                    "name": "Forgot Password",
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
                            }
                        ],
                        "body": {
                            "mode": "raw",
                            "raw": json.dumps({
                                "data": {
                                    "type": "forgot-password",
                                    "attributes": {
                                        "email": f"admin@{domain_name}"
                                    }
                                }
                            }, indent=4),
                            "options": {
                                "raw": {
                                    "language": "json"
                                }
                            }
                        },
                        "url": "{{base_url}}auth/forgot-password"
                    },
                    "response": []
                },
                {
                    "name": "Reset Password",
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
                            }
                        ],
                        "body": {
                            "mode": "raw",
                            "raw": json.dumps({
                                "data": {
                                    "type": "reset-password",
                                    "attributes": {
                                        "token": "ABCD1234",
                                        "email": f"admin@{domain_name}",
                                        "password": "value1234",
                                        "password_confirmation": "value1234"
                                    }
                                }
                            }, indent=4),
                            "options": {
                                "raw": {
                                    "language": "json"
                                }
                            }
                        },
                        "url": "{{base_url}}auth/reset-password"
                    },
                    "response": []
                }
            ]
        }


    @staticmethod
    def create_auth_register(domain_name: str, password: str) -> dict:
        """
        Genera el endpoint de registro de usuarios.
        """

        return {
            "name": "Register",
            "item": [
                {
                    "name": "Register",
                    "event": [
                        {
                            "listen": "test",
                            "script": {
                                "exec": [
                                    "const response = pm.response.json();",
                                    "const token = response?.data?.attributes?.token ?? response?.data?.token ?? response?.token;",
                                    "if (token) {",
                                    "    pm.collectionVariables.set('token_api', token);",
                                    "}"
                                ],
                                "type": "text/javascript"
                            }
                        }
                    ],
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
                            }
                        ],
                        "body": {
                            "mode": "raw",
                            "raw": json.dumps({
                                "data": {
                                    "type": "register",
                                    "attributes": {
                                        "name": "Test User",
                                        "email": f"test@{domain_name}",
                                        "password": password,
                                        "password_confirmation": password
                                    }
                                }
                            }, indent=4),
                            "options": {
                                "raw": {
                                    "language": "json"
                                }
                            }
                        },
                        "url": "{{base_url}}auth/register",
                        "description": "Registra un usuario y guarda el token recibido en {{token_api}}."
                    },
                    "response": []
                }
            ]
        }


    @staticmethod
    def create_auth_login(domain_name: str, password: str) -> dict:
        """
        Genera el endpoint de inicio de sesión.
        """

        return {
            "name": "Login",
            "event": [
                {
                    "listen": "test",
                    "script": {
                        "exec": [
                            "const response = pm.response.json();",
                            "const token = response?.data?.attributes?.token ?? response?.data?.token ?? response?.token;",
                            "if (token) {",
                            "    pm.collectionVariables.set('token_api', token);",
                            "}"
                        ],
                        "type": "text/javascript"
                    }
                }
            ],
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
                    }
                ],
                "body": {
                    "mode": "raw",
                    "raw": json.dumps({
                        "data": {
                            "type": "login",
                            "attributes": {
                                "email": f"admin@{domain_name}",
                                "password": password
                            }
                        }
                    }, indent=4),
                    "options": {
                        "raw": {
                            "language": "json"
                        }
                    }
                },
                "url": "{{base_url}}auth/login"
            },
            "response": []
        }


    @staticmethod
    def create_auth_show() -> dict:
        """
        Genera el endpoint para consultar el usuario autenticado.
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
                "url": "{{base_url}}auth/user"
            },
            "response": []
        }



    @staticmethod
    def create_auth_logout() -> dict:
        """
        Genera el endpoint de cierre de sesión.
        """

        return {
            "name": "Logout",
            "request": {
                "method": "POST",
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
                "url": "{{base_url}}auth/logout"
            },
            "response": []
        }
        
    
    @staticmethod
    def create_dev() -> dict:
        """
        Genera la carpeta Dev con los endpoints Test y Execute.
        """

        return {
            "name": "Dev",
            "item": [
                {
                    "name": "Test",
                    "request": {
                        "method": "GET",
                        "header": [],
                        "url": "{{base_url}}dev/test"
                    },
                    "response": []
                },
                {
                    "name": "Execute",
                    "request": {
                        "method": "GET",
                        "header": [],
                        "url": "{{base_url}}dev/execute"
                    },
                    "response": []
                }
            ]
        }
        
    
    
    @staticmethod
    def create_dashboards() -> dict:
        """
        Genera la carpeta Dashboards de Postman.
        """

        return {
            "name": "Dashboards",
            "item": [
                HelperLaravelPostmanCrud.create_index(
                    endpoint="dashboards",
                    filters=[]
                )
            ]
        }