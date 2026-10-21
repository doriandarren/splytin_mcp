
import os
import json
import uuid

from gen.helpers.helper_file import HelperFile
from gen.python_django.helpers.helper_postman_json import HelperPostmanJson


class DjGeneratePostman:

    def __init__(self):
        self.helper = HelperPostmanJson

        # Headers para peticiones JSON:API
        self.headers = [
            self.helper.create_header(
                "Accept", "application/vnd.api+json"
            ),
            self.helper.create_header(
                "Content-Type", "application/vnd.api+json"
            )
        ]

        # Headers para peticiones con autenticación
        self.auth_headers = [
            *self.headers,
            self.helper.create_header(
                "Authorization", "Token {{token_api}}"
            )
        ]

        # Headers para formularios
        # Postman establecerá el Content-Type multipart automáticamente
        self.form_headers = [
            self.helper.create_header(
                "Accept", "application/vnd.api+json"
            )
        ]
        
        
        
        
        

    def create_authentication(self, domain_name):
        """
        Genera la carpeta Authentication.
        """

        # Recuperar contraseña
        forgot = self.helper.create_item(
            name="forgot Password",
            method="POST",
            url="{{base_url}}auth/password/email/",
            headers=self.form_headers,
            body=self.helper.create_form_body([
                self.helper.create_form_field(
                    "email", f"admin@{domain_name}"
                )
            ])
        )

        restore = self.helper.create_item(
            name="Restore Password",
            method="POST",
            url="{{base_url}}auth/password/restore/",
            headers=self.form_headers,
            body=self.helper.create_form_body([
                self.helper.create_form_field("token"),
                self.helper.create_form_field(
                    "password", "{{password_api}}"
                )
            ])
        )

        restore_folder = self.helper.create_folder(
            name="Restore Password",
            items=[forgot, restore]
        )

        # Login
        token_script = self.helper.create_test_script([
            "const response = pm.response.json();",
            "const token = response?.data?.attributes?.token "
            "?? response?.data?.token ?? response?.token;",
            "if (token) {",
            '    pm.collectionVariables.set("token_api", token);',
            "}"
        ])

        login = self.helper.create_item(
            name="Login",
            method="POST",
            url="{{base_url}}auth/login/",
            headers=self.form_headers,
            body=self.helper.create_form_body([
                {
                    "key": "email",
                    "value": f"admin@{domain_name}",
                    "type": "text",
                    "disabled": False
                },
                {
                    "key": "password",
                    "value": "{{password_api}}",
                    "type": "text",
                    "disabled": False
                },
                {
                    "key": "email",
                    "value": f"manager@{domain_name}",
                    "type": "text",
                    "disabled": True
                },
                {
                    "key": "email",
                    "value": f"user@{domain_name}",
                    "type": "text",
                    "disabled": True
                }
            ]),
            events=[token_script]
        )

        # Obtener usuario autenticado
        show = self.helper.create_item(
            name="show",
            method="GET",
            url="{{base_url}}auth/user/",
            headers=self.auth_headers
        )

        # Cerrar sesión
        logout = self.helper.create_item(
            name="logout",
            method="GET",
            url="{{base_url}}auth/logout/",
            headers=self.auth_headers
        )

        return self.helper.create_folder(
            name="Authentication",
            items=[
                restore_folder,
                login,
                show,
                logout
            ]
        )








    def create_dev(self):
        """
        Genera la carpeta Dev.
        """

        test = self.helper.create_item(
            name="Test",
            method="GET",
            url="{{base_url}}dev/test/",
            headers=self.headers
        )

        return self.helper.create_folder(
            name="Dev",
            items=[test]
        )

    def create_dashboards(self):
        """
        Genera la carpeta Dashboards.
        """

        list_item = self.helper.create_item(
            name="List",
            method="GET",
            url="{{base_url}}dashboards/list/",
            headers=self.auth_headers
        )

        return self.helper.create_folder(
            name="Dashboards",
            items=[list_item]
        )

    def generate(self, project_name, domain_name, base_url=None):
        """
        Construye la colección Postman.
        """

        if base_url is None:
            base_url = f"http://{project_name}/api/v1/"

        collection = {
            "info": {
                "_postman_id": str(uuid.uuid4()),
                "name": "API",
                "description": f"API REST - {project_name}",
                "schema": (
                    "https://schema.getpostman.com/json/"
                    "collection/v2.1.0/collection.json"
                )
            },
            "item": [
                self.create_authentication(domain_name),
                self.create_dev(),
                self.create_dashboards()
            ],
            "variable": [
                self.helper.create_variable(
                    "base_url", base_url
                ),
                self.helper.create_variable("token_api"),
                self.helper.create_variable("password_api")
            ]
        }

        return collection

    def invoke(
        self,
        full_path,
        project_name,
        domain_name,
        base_url=None
    ):
        """
        Genera y guarda el archivo Postman.
        """

        collection = self.generate(
            project_name=project_name,
            domain_name=domain_name,
            base_url=base_url
        )

        folder_path = os.path.join(full_path, "SCRIPTS")

        content = json.dumps(
            collection,
            indent=4,
            ensure_ascii=False
        )

        # Crear el archivo
        HelperFile.write(
            folder_path=folder_path,
            file_name=f"API-{project_name}.postman.collection.json",
            content=content
        )
