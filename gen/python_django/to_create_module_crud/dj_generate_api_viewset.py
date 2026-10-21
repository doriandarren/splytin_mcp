import os
from gen.helpers.helper_file import HelperFile


class DjGenerateApiViewset:

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

        content = f'''from core.api.api_response import BaseModelViewSet
from rest_framework.permissions import IsAuthenticated
#from django_filters.rest_framework import DjangoFilterBackend

from apps.{plural_name_snake}.api.serializers import {singular_name}Serializer
from apps.{plural_name_snake}.models import {singular_name}


class {singular_name}ApiViewSet(BaseModelViewSet):
    permission_classes = [IsAuthenticated] # sin login: [IsAuthenticatedOrReadOnly]
    serializer_class = {singular_name}Serializer
    queryset = {singular_name}.objects.all()
    # Filtros...
    #filter_backends = [DjangoFilterBackend]
    #filterset_fields = ['category', 'active']
'''

        # Crear el archivo
        HelperFile.write(
            folder_path=folder_path,
            file_name="views.py",
            content=content
        )

