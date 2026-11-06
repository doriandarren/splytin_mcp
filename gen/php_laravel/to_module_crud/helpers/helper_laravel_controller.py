import os


class HelperLaravelController:

    @staticmethod
    def get_namespace(
        namespace: str,
        version_api: str,
        folder_group: str | None,
        plural_name: str
    ) -> str:

        parts = [
            "App",
            "Http",
            "Controllers",
            namespace,
            version_api
        ]

        if folder_group:
            parts.append(folder_group)

        parts.append(plural_name)

        namespace_path = "\\".join(parts)

        return f"namespace {namespace_path};"




    @staticmethod
    def get_folder_path(
        full_path: str,
        namespace: str,
        version_api: str,
        folder_group: str | None,
        plural_name: str
    ) -> str:

        parts = [
            full_path,
            "app",
            "Http",
            "Controllers",
            namespace,
            version_api
        ]

        if folder_group:
            parts.append(folder_group)

        parts.append(plural_name)

        return os.path.join(*parts)
    
    
    
    @staticmethod
    def get_model_import(
        namespace: str,
        plural_name: str,
        singular_name: str
    ) -> str:

        if singular_name == "User":
            return "use App\\Models\\User;"

        parts = [
            "App",
            "Models",
            namespace,
            plural_name,
            singular_name
        ]

        model_path = "\\".join(parts)

        return f"use {model_path};"
    
    
    
    
    @staticmethod
    def first_letter_lower(name: str) -> str:
        """Convierte la primera letra de un string a minúscula."""
        return name[0].lower() + name[1:]

    @staticmethod
    def format_attributes(
        columns: list[dict],
        singular_name: str,
        singular_name_camel: str
    ) -> str:
        lines = []

        for column in columns:
            lines.append(
                f"""            $attributes['{column["name"]}'],"""
            )

        content = f"""        ${singular_name_camel} = $this->service->set{singular_name}(
"""
        content += "\n".join(lines)
        content += """
        );"""

        return content

    @staticmethod
    def create_body_param_comments(columns: list[dict]) -> str:
        # Construir los comentarios dinámicos para @bodyParam usando las columnas
        body_param_comments = ""

        for i, column in enumerate(columns):
            body_param_comments += (
                f"    * @bodyParam {column['name']} "
                f"{column['type']} required"
            )

            if i < len(columns) - 1:
                body_param_comments += "\n"

        return body_param_comments

    