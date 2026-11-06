import os


class HelperLaravelResource:

    @staticmethod
    def format_column_attributes(columns: list[dict]) -> str:
        lines = []

        for column in columns:
            lines.append(
                f"                '{column['name']}' => $this->{column['name']},"
            )

        content = "\n".join(lines)

        return content

    @staticmethod
    def format_relationships(
        columns: list[dict],
        singular_name_snake: str,
        plural_name_snake: str
    ) -> str:
        lines = []
        flag = False

        for column in columns:
            if column["is_fk"]:
                flag = True

        if flag:
            lines.append("""            //' relationships' => [""")

            for column in columns:
                if column["is_fk"]:
                    column_kabad_case = column["related_table"].replace("_", "-")

                    lines.append(f"""                //'{column["relationship_name"]}' => [
                    //'data' => [
                    //    'type' => '{column["relationship_name"]}',
                    //    'id' => $this->{column["relationship_column"]}
                    //],
                    //'links' => [
                    //    'self' => route('{column_kabad_case}.show', ['{column["relationship_name"]}' => $this->{column["relationship_column"]}])
                    //]
                //],""")

            lines.append("""            // ],""")

        content = "\n".join(lines)

        return content

    @staticmethod
    def format_includes(columns: list[dict]) -> str:
        lines = []
        flag = False

        for column in columns:
            if column["is_fk"]:
                flag = True

        if flag:
            lines.append("""            // 'includes' => [""")

            for column in columns:
                if column["is_fk"]:
                    lines.append(
                        f"""                // new {column["related_model"]}Resource($this->whenLoaded('{column["relationship_name"]}')),"""
                    )

            lines.append("""            //],""")

        content = "\n".join(lines)

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
            "Resources",
            version_api,
            plural_name
        )
