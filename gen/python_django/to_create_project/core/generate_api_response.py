import os
from helpers.helper_print import print_message, GREEN, CYAN


def generate_api_response(full_path):
    create_api_init(full_path)
    create_api_response(full_path)



def create_api_init(full_path):
    """
    Genera el archivo init
    """

    folder_path = os.path.join(full_path, "core", "api")
    file_path = os.path.join(folder_path, "__init__.py")

    os.makedirs(folder_path, exist_ok=True)

    content = f'''# core/api/__init__.py
from .api_response import BaseApiResponse, BaseAPIView, BaseModelViewSet
'''

    try:
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)



def create_api_response(full_path):
    """
    Genera el archivo
    """
    folder_path = os.path.join(full_path, "core", "api")
    file_path = os.path.join(folder_path, "api_response.py")

    os.makedirs(folder_path, exist_ok=True)

    content = f'''# core/api/api_response.py

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet


class BaseApiResponse:

    def respond_with_data(self, message=None, data=None, success=True, status_code=200):
        return Response({{
            "data": data,
            "message": message,
            "success": success,
            "status_code": status_code,
        }}, status=status_code)

    def respond_with_error(self, message="", errors=None, status_code=422):
        return Response({{
            "data": None,
            "message": message,
            "errors": errors,
            "success": False,
            "status_code": status_code,
        }}, status=status_code)


class BaseAPIView(BaseApiResponse, APIView):
    pass


class BaseModelViewSet(BaseApiResponse, ModelViewSet):

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)

        if page is not None:
            serializer = self.get_serializer(page, many=True)

            return self.get_paginated_response({{
                "data": serializer.data,
                "message": "Records retrieved successfully",
                "success": True,
                "status_code": status.HTTP_200_OK,
            }})

        serializer = self.get_serializer(queryset, many=True)

        return self.respond_with_data(
            message="Records retrieved successfully",
            data=serializer.data,
            status_code=status.HTTP_200_OK
        )

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)

        return self.respond_with_data(
            message="Record retrieved successfully",
            data=serializer.data,
            status_code=status.HTTP_200_OK
        )

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        return self.respond_with_data(
            message="Record created successfully",
            data=serializer.data,
            status_code=status.HTTP_201_CREATED
        )

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop("partial", False)
        instance = self.get_object()

        serializer = self.get_serializer(
            instance,
            data=request.data,
            partial=partial
        )

        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return self.respond_with_data(
            message="Record updated successfully",
            data=serializer.data,
            status_code=status.HTTP_200_OK
        )

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)

        return self.respond_with_data(
            message="Record deleted successfully",
            data=None,
            status_code=status.HTTP_200_OK
        )
'''

    try:
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)