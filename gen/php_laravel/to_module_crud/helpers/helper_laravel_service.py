import os


class HelperLaravelService:

    @staticmethod
    def get_folder_path(
        full_path: str,
        version_api: str,
        plural_name: str
    ) -> str:
        return os.path.join(
            full_path,
            "app",
            "Services",
            version_api,
            plural_name
        )

    @staticmethod
    def format_store_columns(columns: list[dict]) -> str:
        content = ""

        for column in columns:
            name = column["name"]
            content += f"        $objNew->{name} = $data->{name};\n"

        return content

    @staticmethod
    def format_update_columns(columns: list[dict]) -> str:
        content = ""

        for column in columns:
            name = column["name"]

            content += f"""        if (isset($obj->{name})) {{
            if ($obj->{name} != '' && !empty($obj->{name})) {{
                $objOld->{name} = $obj->{name};
            }}
        }}

"""

        return content

    @staticmethod
    def format_set_params(columns: list[dict]) -> str:
        content = ""

        for column in columns:
            name = column["name"]
            content += f"        ${name},\n"

        return content

    @staticmethod
    def format_set_doc_params(columns: list[dict]) -> str:
        content = ""

        for column in columns:
            name = column["name"]
            content += f"    * @param ${name}\n"

        return content

    @staticmethod
    def format_set_columns(columns: list[dict]) -> str:
        content = ""

        for column in columns:
            name = column["name"]
            content += f"        $obj->{name} = ${name};\n"

        return content
