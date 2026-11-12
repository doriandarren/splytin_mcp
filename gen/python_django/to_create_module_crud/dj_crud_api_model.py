
from gen.python_django.helpers.helper_dj_file import helper_append_content
from gen.python_django.helpers.helper_dj_model_fields import HelperDjModelFields
from helpers.helper_print import print_green 


class DjCrudApiModel:

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

        fields = []

        for column in columns:
            field_name, field_definition = HelperDjModelFields.map_column_type(
                column,
                plural_name_snake
            )
            fields.append(f"    {field_name} = {field_definition}")

        fields_str = "\n".join(fields)

        print_green(f"Creating model {singular_name}")

        content = f"""from django.db import models
from core.models.models import BaseModel


class {singular_name}(BaseModel):

    # Class Relations
    # Add to field: Ex. class_relations
    # class_relations = ClassRelationSerializer(
    #     many=True,
    #     read_only=True
    # )

{fields_str if fields else "    pass"}


    class Meta:
        verbose_name = "{singular_name}"
        verbose_name_plural = "{plural_name}"

    class JSONAPIMeta:
        resource_name = "{plural_name_kebab}"

    def __str__(self):
        return f"{{self.pk}}"
"""

        helper_append_content(
            full_path,
            f"apps/{plural_name_snake}/models.py",
            content
        )
