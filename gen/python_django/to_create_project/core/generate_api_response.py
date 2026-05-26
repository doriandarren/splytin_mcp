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
    """
    Clase base para centralizar las respuestas de la API.

    Esta clase no es una vista por sí sola.
    Solo contiene métodos reutilizables para devolver respuestas
    con una estructura uniforme en toda la aplicación.
    """

    def respond_with_data(self, message=None, data=None, success=True, status_code=200):
        """
        Respuesta correcta de la API.

        Se utiliza cuando la petición se ha procesado correctamente.
        """
        return Response({{
            "data": data,
            "message": message,
            "success": success,
            "status_code": status_code,
        }}, status=status_code)

    def respond_with_error(self, message="", errors=None, status_code=422):
        """
        Respuesta de error de la API.

        Se utiliza cuando ocurre un error de validación,
        autenticación, permisos o cualquier excepción controlada.
        """
        return Response({{
            "data": None,
            "message": message,
            "errors": errors,
            "success": False,
            "status_code": status_code,
        }}, status=status_code)


class BaseAPIView(BaseApiResponse, APIView):
    """
    Vista base para endpoints personalizados.

    Hereda de APIView, por lo tanto se usa cuando queremos definir
    manualmente métodos como get(), post(), put() o delete().

    Ejemplos de uso:
    - Login
    - Logout
    - Usuario actual
    - Endpoints de prueba
    - Acciones personalizadas que no son un CRUD automático
    """
    pass


class BaseModelViewSet(BaseApiResponse, ModelViewSet):
    """
    Vista base para CRUD automático basado en modelos.

    Hereda de ModelViewSet, por lo tanto se usa cuando queremos que
    Django REST Framework genere automáticamente acciones como:

    - list      -> GET listado
    - retrieve  -> GET por id
    - create    -> POST crear
    - update    -> PUT/PATCH actualizar
    - destroy   -> DELETE eliminar

    También permite usar @action para crear rutas adicionales
    dentro del mismo ViewSet.

    Ejemplos de uso:
    - Gestión de usuarios
    - Gestión de productos
    - Gestión de categorías
    - Cualquier modelo con operaciones CRUD
    """
    pass
'''

    try:
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)