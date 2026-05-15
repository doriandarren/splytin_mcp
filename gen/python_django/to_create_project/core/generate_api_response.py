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
    pass
'''

    try:
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)