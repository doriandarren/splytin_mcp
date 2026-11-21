from gen.php_laravel.to_create_project.helpers.postman.helper_laravel_postman_crud import HelperLaravelPostmanCrud
from gen.php_laravel.to_create_project.helpers.postman.helper_laravel_postman_fixed import HelperLaravelPostmanFixed


class HelperLaravelPostman:

    @staticmethod
    def create_crud(
        name: str,
        endpoint: str,
        attributes: dict,
        relationships: dict | None = None,
        filters: list | None = None
    ) -> dict:
        """
        Genera una carpeta CRUD completa de Postman.
        """

        return {
            "name": name,
            "item": [
                HelperLaravelPostmanCrud.create_index(endpoint, filters),
                HelperLaravelPostmanCrud.create_show(endpoint),
                HelperLaravelPostmanCrud.create_store(
                    endpoint, attributes, relationships
                ),
                HelperLaravelPostmanCrud.create_update(
                    endpoint, attributes, relationships
                ),
                HelperLaravelPostmanCrud.create_delete(endpoint)
            ]
        }

    @staticmethod
    def create_authentication(
        domain_name: str,
        password: str
    ) -> dict:
        """
        Genera la carpeta Authentication de Postman.
        """

        return {
            "name": "Authentication",
            "item": [
                HelperLaravelPostmanFixed.create_auth_reset_password(domain_name),
                HelperLaravelPostmanFixed.create_auth_register(domain_name, password),
                HelperLaravelPostmanFixed.create_auth_login(domain_name, password),
                HelperLaravelPostmanFixed.create_auth_show(),
                HelperLaravelPostmanFixed.create_auth_logout()
            ]
        }
        
        
        
    
    @staticmethod
    def create_shared(domain_name: str, password: str) -> dict:
        """
        Genera la carpeta SHARED con todos los CRUD de Postman.
        """

        return {
            "name": "SHARED",
            "item": [

                # Abilities
                HelperLaravelPostman.create_crud(
                    name="Abilities",
                    endpoint="abilities",
                    attributes={
                        "name": "New name",
                        "label": "New label"
                    },
                    relationships={
                        "ability_group": {
                            "data": {"id": "1"}
                        }
                    },
                    filters=[
                        {
                            "key": "include",
                            "value": "",
                            "disabled": True
                        },
                        {
                            "key": "filter[ability_group_id]",
                            "value": "1",
                            "disabled": True
                        },
                        {
                            "key": "filter[name]",
                            "value": "roles:store",
                            "disabled": True
                        },
                        {
                            "key": "filter[label]",
                            "value": "Edita modulo",
                            "disabled": True
                        },
                        {
                            "key": "filter[created_at]",
                            "value": "2026-08-01,2026-09-20",
                            "disabled": True
                        },
                        {
                            "key": "filter[updated_at]",
                            "value": "2026-08-01,2026-09-20",
                            "disabled": True
                        },
                        *[
                            {"key": "sort", "value": field, "disabled": True}
                            for field in [
                                "ability_group_id", "name", "label",
                                "created_at", "updated_at"
                            ]
                        ]
                    ]
                ),

                # AbilityGroups
                HelperLaravelPostman.create_crud(
                    name="AbilityGroups",
                    endpoint="ability-groups",
                    attributes={
                        "name": "New name"
                    },
                    filters=[
                        {
                            "key": "include",
                            "value": "",
                            "disabled": True
                        },
                        {
                            "key": "filter[name]",
                            "value": "roles",
                            "disabled": True
                        },
                        {
                            "key": "filter[created_at]",
                            "value": "2026-08-01,2026-09-20",
                            "disabled": True
                        },
                        {
                            "key": "filter[updated_at]",
                            "value": "2026-08-01,2026-09-20",
                            "disabled": True
                        },
                        *[
                            {"key": "sort", "value": field, "disabled": True}
                            for field in [
                                "name", "created_at", "updated_at"
                            ]
                        ]
                    ]
                ),

                # AbilityUsers
                HelperLaravelPostman.create_crud(
                    name="AbilityUsers",
                    endpoint="ability-users",
                    attributes={},
                    relationships={
                        "user": {
                            "data": {"id": "1"}
                        },
                        "ability": {
                            "data": {"id": "1"}
                        }
                    },
                    filters=[
                        {
                            "key": "include",
                            "value": "",
                            "disabled": True
                        },
                        {
                            "key": "filter[user_id]",
                            "value": "1",
                            "disabled": True
                        },
                        {
                            "key": "filter[ability_id]",
                            "value": "1",
                            "disabled": True
                        },
                        {
                            "key": "filter[created_at]",
                            "value": "2026-08-01,2026-09-20",
                            "disabled": True
                        },
                        {
                            "key": "filter[updated_at]",
                            "value": "2026-08-01,2026-09-20",
                            "disabled": True
                        },
                        *[
                            {"key": "sort", "value": field, "disabled": True}
                            for field in [
                                "user_id", "ability_id",
                                "created_at", "updated_at"
                            ]
                        ]
                    ]
                ),

                # RoleUsers
                HelperLaravelPostman.create_crud(
                    name="RoleUsers",
                    endpoint="role-users",
                    attributes={},
                    relationships={
                        "role": {
                            "data": {"id": "1"}
                        },
                        "user": {
                            "data": {"id": "1"}
                        }
                    },
                    filters=[
                        {
                            "key": "include",
                            "value": "",
                            "disabled": True
                        },
                        {
                            "key": "filter[role_id]",
                            "value": "1",
                            "disabled": True
                        },
                        {
                            "key": "filter[user_id]",
                            "value": "1",
                            "disabled": True
                        },
                        {
                            "key": "filter[created_at]",
                            "value": "2026-08-01,2026-09-20",
                            "disabled": True
                        },
                        {
                            "key": "filter[updated_at]",
                            "value": "2026-08-01,2026-09-20",
                            "disabled": True
                        },
                        *[
                            {"key": "sort", "value": field, "disabled": True}
                            for field in [
                                "role_id", "user_id",
                                "created_at", "updated_at"
                            ]
                        ]
                    ]
                ),

                # Roles
                HelperLaravelPostman.create_crud(
                    name="Roles",
                    endpoint="roles",
                    attributes={
                        "name": "New name",
                        "description": "New description"
                    },
                    filters=[
                        {
                            "key": "include",
                            "value": "",
                            "disabled": True
                        },
                        {
                            "key": "filter[name]",
                            "value": "",
                            "disabled": True
                        },
                        {
                            "key": "filter[description]",
                            "value": "",
                            "disabled": True
                        },
                        {
                            "key": "filter[created_at]",
                            "value": "2026-08-01,2026-09-20",
                            "disabled": True
                        },
                        {
                            "key": "filter[updated_at]",
                            "value": "2026-08-01,2026-09-20",
                            "disabled": True
                        },
                        *[
                            {"key": "sort", "value": field, "disabled": True}
                            for field in [
                                "name", "description",
                                "created_at", "updated_at"
                            ]
                        ]
                    ]
                ),

                # Users
                HelperLaravelPostman.create_crud(
                    name="Users",
                    endpoint="users",
                    attributes={
                        "user_status_id": 1,
                        "name": "Admin New",
                        "email": f"admin_new@{domain_name}",
                        "email_verified_at": None,
                        "password": password,
                        "image_url": None
                    },
                    filters=[
                        {
                            "key": "include",
                            "value": "",
                            "disabled": True
                        },
                        {
                            "key": "filter[user_status_id]",
                            "value": "1",
                            "disabled": True
                        },
                        {
                            "key": "filter[name]",
                            "value": "",
                            "disabled": True
                        },
                        {
                            "key": "filter[email]",
                            "value": f"admin@{domain_name}",
                            "disabled": True
                        },
                        {
                            "key": "filter[email_verified_at]",
                            "value": "2026-08-01,2026-09-20",
                            "disabled": True
                        },
                        {
                            "key": "filter[created_at]",
                            "value": "2026-08-01,2026-09-20",
                            "disabled": True
                        },
                        {
                            "key": "filter[updated_at]",
                            "value": "2026-08-01,2026-09-20",
                            "disabled": True
                        },
                        *[
                            {"key": "sort", "value": field, "disabled": True}
                            for field in [
                                "name", "email",
                                "created_at", "updated_at"
                            ]
                        ]
                    ]
                ),

                # UserStatuses
                HelperLaravelPostman.create_crud(
                    name="UserStatuses",
                    endpoint="user-statuses",
                    attributes={
                        "name": "New name"
                    },
                    filters=[
                        {
                            "key": "include",
                            "value": "",
                            "disabled": True
                        },
                        {
                            "key": "filter[name]",
                            "value": "",
                            "disabled": True
                        },
                        {
                            "key": "filter[created_at]",
                            "value": "2026-08-01,2026-09-20",
                            "disabled": True
                        },
                        {
                            "key": "filter[updated_at]",
                            "value": "2026-08-01,2026-09-20",
                            "disabled": True
                        },
                        *[
                            {"key": "sort", "value": field, "disabled": True}
                            for field in [
                                "name", "created_at", "updated_at"
                            ]
                        ]
                    ]
                )
            ]
        }
    
    
    

    @staticmethod
    def build_collection(
        project_name: str,
        domain_name: str,
        password: str
    ) -> dict:
        """
        Construye la colección Postman.
        """

        content = {
            "info": HelperLaravelPostmanFixed.create_info(project_name),
            "item": [
                HelperLaravelPostman.create_authentication(
                    domain_name=domain_name,
                    password=password
                ),

                # Aquí añadiremos SHARED con los CRUD
                HelperLaravelPostman.create_shared(
                    domain_name=domain_name,
                    password=password
                ),

                HelperLaravelPostmanFixed.create_dev(),
                HelperLaravelPostmanFixed.create_dashboards()
            ]
        }

        return content