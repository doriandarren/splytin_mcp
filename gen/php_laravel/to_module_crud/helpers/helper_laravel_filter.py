import os


class HelperLaravelFilter:

    @staticmethod
    def format_columns_function(columns: list[dict]) -> str:

        content = ""

        for column in columns:
            column_name = column["name"]

            content += f"""
        public function {column_name}($value)
        {{
            $likeStr = str_replace('*', '%', $value);
            return $this->builder->where('{column_name}', 'like', $likeStr);
        }}
        """

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
            "Filters",
            version_api,
            plural_name
        )
