import os
from gen.helpers.helper_file import HelperFile


class DjGenerateApiResponse:

    def invoke(self, full_path):
        self.create_api_init(full_path)
        self.create_api_response(full_path)
        

        
    def create_api_init(self, full_path):
        """
        Genera el archivo.
        """

        folder_path = os.path.join(full_path, "core", "api")

        content = f'''# core/api/__init__.py
from .api_response import BaseApiResponse, BaseAPIView, BaseModelViewSet
'''

        # Crear el archivo
        HelperFile.write(
            folder_path=folder_path,
            file_name="__init__.py",
            content=content
        )
        
        
        
    def create_api_response(self, full_path):
        """
        Genera el archivo.
        """

        folder_path = os.path.join(full_path, "core", "api")

        content = r'''
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet


# Respuestas personalizadas (compatibilidad con APIs existentes)
class BaseApiResponse:

    def respond_with_data(
        self,
        message=None,
        data=None,
        success=True,
        status_code=200
    ):
        return Response({
            "data": data,
            "message": message,
            "success": success,
            "status_code": status_code,
        }, status=status_code)

    def respond_with_error(
        self,
        message="",
        errors=None,
        status_code=422
    ):
        return Response({
            "data": None,
            "message": message,
            "errors": errors,
            "success": False,
            "status_code": status_code,
        }, status=status_code)


# APIView para endpoints existentes
class BaseAPIView(BaseApiResponse, APIView):
    pass


# ViewSet para modelos con auditoría y Soft Delete
class BaseModelViewSet(BaseApiResponse, ModelViewSet):

    def perform_create(self, serializer):
        serializer.save(
            created_by=self.request.user,
            updated_by=self.request.user
        )

    def perform_update(self, serializer):
        serializer.save(
            updated_by=self.request.user
        )

    def perform_destroy(self, instance):
        instance.soft_delete(
            user=self.request.user
        )
'''

        # Crear el archivo
        HelperFile.write(
            folder_path=folder_path,
            file_name="api_response.py",
            content=content
        )

