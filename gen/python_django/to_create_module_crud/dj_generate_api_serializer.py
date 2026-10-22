import os
from gen.helpers.helper_file import HelperFile


class DjGenerateApiSerializer:

    def invoke(
        self,
        full_path,
        project_name,
        singular_name,
        plural_name,
        singular_name_kebab,
        plural_name_kebab,
        singular_name_snake,
        plural_name_snake,
        singular_first_camel,
        plural_first_camel,
        columns,
    ):
        """
        Genera el archivo.
        """

        folder_path = os.path.join(full_path, "apps", plural_name_snake, "api")

        format_cols = ""
        for index, col in enumerate(columns):
            if index == len(columns) - 1:
                format_cols += f"            '{col['name']}',"
            else:
                format_cols += f"            '{col['name']}',\n"
        
        # format_cols = ",\n".join(f"'{col["name"]}'" for col in columns)
        
    
        content = f'''#from rest_framework.serializers import ModelSerializer
from rest_framework_json_api.serializers import ModelSerializer
from apps.{plural_name_snake}.models import {singular_name}


class {singular_name}Serializer(ModelSerializer):

    class Meta:
        model = {singular_name}
        ## fields = "__all__"
        fields = [
            'id', 
{format_cols}
            'created_at',
            'updated_at',
            'created_by',
            'updated_by',
        ]
        
        
        read_only_fields = [
            "id",
            "created_at",
            "updated_at",
            "created_by",
            "updated_by",
        ]
        
'''

        # Crear el archivo
        HelperFile.write(
            folder_path=folder_path,
            file_name="serializers.py",
            content=content
        )
