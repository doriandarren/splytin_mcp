import os

class HelperLaravelModel:

    @staticmethod
    def format_relation_fields(columns: list[dict]) -> str:
        content = ''

        for column in columns:
            if column["is_fk"]:
                content += f"""    public function {column["relationship_name"]}(): BelongsTo
    {{\n"""
                content += f"""        return $this->belongsTo({column["related_model"]}::class, '{column["relationship_column"]}', 'id');"""
                content += f"""
    }}\n\n"""

        return content

    @staticmethod
    def format_relation_uses(
        namespace: str,
        columns: list[dict]
    ) -> str:
        content = ''
        flag = False

        for column in columns:
            if column["is_fk"]:
                flag = True
                namespace_format = ''

                if column["related_model"] == 'User':
                    namespace_format += '\\User'
                else:
                    namespace_format += (
                        f'\\{namespace}\\{column["related_model_plural"]}'
                        f'\\{column["related_model"]}'
                    )

                content += f"""use App\\Models{namespace_format};\n"""

        if flag:
            content += "use Illuminate\\Database\\Eloquent\\Relations\\BelongsTo; \n"

        return content

    @staticmethod
    def get_folder_path(
        full_path: str,
        namespace: str,
        plural_name: str
    ) -> str:
        return os.path.join(
            full_path,
            "app",
            "Models",
            namespace,
            plural_name
        )
