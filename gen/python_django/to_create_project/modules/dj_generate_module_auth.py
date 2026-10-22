import os
from gen.helpers.helper_columns import parse_columns_input
from gen.python_django.helpers.helper_file import (
    helper_append_content, 
    helper_insert_after_line
)
from gen.python_django.to_create_module_crud.standard_module_crud_python_django import standard_module_crud_python_django
from gen.helpers.helper_print import dd, print_message, GREEN, CYAN
from gen.helpers.helper_file import HelperFile


class DjGenerateModuleAuth:
    
    def invoke(self, full_path):
        """
        Genera el archivo
        """
        
        app_main = "main"
        singular_name = "Authentication"
        plural_name = "Authentications"
        columns = parse_columns_input("email password")
        input_menu_checkbox=["api_route", "api_serializer", "api_wiewset", "api_model", "api_service"]
        
        
        standard_module_crud_python_django(full_path, app_main, singular_name, plural_name, columns, input_menu_checkbox)
        
        
        self.update_router(full_path)
        self.update_view(full_path)
        self.update_serializer(full_path)
        self.add_settings(full_path, app_main)
        self.update_setting_auth_token(full_path, app_main)



    def update_router(self, full_path):
        """
        Genera el archivo.
        """

        folder_path = os.path.join(full_path, "apps", "authentications", "api")

        content = f'''from django.urls import path

from apps.authentications.api.views import (
    CurrentUserView,
    LoginView,
    LogoutView,
)


urlpatterns = [
    path(
        "auth/login/",
        LoginView.as_view(),
        name="auth_login"
    ),
    path(
        "auth/user/",
        CurrentUserView.as_view(),
        name="auth_user"
    ),
    path(
        "auth/logout/",
        LogoutView.as_view(),
        name="auth_logout"
    ),
]
'''

        # Crear el archivo
        HelperFile.write(
            folder_path=folder_path,
            file_name="router.py",
            content=content
        )
        
        
        
    def update_view(self, full_path):
        """
        Genera el archivo.
        """

        folder_path = os.path.join(full_path, "apps", "authentications", "api")

        content = f'''
from django.contrib.auth import authenticate

from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import AuthenticationFailed, ValidationError
from rest_framework.parsers import JSONParser
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from core.api import BaseAPIView


# Parser para recibir documentos JSON:API
class JSONAPIDocumentParser(JSONParser):
    media_type = "application/vnd.api+json"


# LOGIN
class LoginView(BaseAPIView):

    permission_classes = [AllowAny]
    authentication_classes = []
    parser_classes = [JSONAPIDocumentParser]
    resource_name = False

    def post(self, request):

        data = request.data.get("data")

        if not isinstance(data, dict) or data.get("type") != "login":
            raise ValidationError("Invalid JSON:API login document")

        attributes = data.get("attributes")

        if not isinstance(attributes, dict):
            raise ValidationError("Invalid attributes")

        email = attributes.get("email")
        password = attributes.get("password")

        if not email or not password:
            raise ValidationError("Email and password are required")

        user = authenticate(
            request,
            username=email,
            password=password
        )

        if user is None:
            raise AuthenticationFailed("Invalid credentials")

        token, _ = Token.objects.get_or_create(user=user)

        return Response({{
            "data": {{
                "type": "auth-tokens",
                "id": token.key,
                "attributes": {{
                    "token": token.key
                }}
            }}
        }}, status=status.HTTP_200_OK)


# USUARIO AUTENTICADO
class CurrentUserView(BaseAPIView):

    permission_classes = [IsAuthenticated]
    resource_name = False

    def get(self, request):

        user = request.user

        return Response({{
            "data": {{
                "type": "users",
                "id": str(user.pk),
                "attributes": {{
                    "email": user.email
                }}
            }}
        }}, status=status.HTTP_200_OK)


# LOGOUT
class LogoutView(BaseAPIView):

    permission_classes = [IsAuthenticated]
    resource_name = False

    def post(self, request):

        Token.objects.filter(user=request.user).delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
        
'''

        # Crear el archivo
        HelperFile.write(
            folder_path=folder_path,
            file_name="views.py",
            content=content
        )
        
        
        
        
    def update_serializer(self, full_path):
        """
        Genera el archivo.
        """

        folder_path = os.path.join(full_path, "apps", "authentications", "api")

        content = f'''#from rest_framework.serializers import ModelSerializer
from rest_framework_json_api.serializers import ModelSerializer
from apps.authentications.models import Authentication


class AuthenticationSerializer(ModelSerializer):

    class Meta:
        model = Authentication
        ## fields = "__all__"
        fields = [
            'id', 
            'email',
            'created_at',
            'updated_at',
            'created_by',
            'updated_by',
        ]

'''

        # Crear el archivo
        HelperFile.write(
            folder_path=folder_path,
            file_name="serializers.py",
            content=content
        )

        


    def add_settings(self, full_path, app_main):
        
        str = f"""\n# Rest Framework
REST_FRAMEWORK = {{
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    ),
    "DEFAULT_RENDERER_CLASSES": [
        "rest_framework.renderers.JSONRenderer",
    ],
}}
"""
        
        helper_append_content(
            full_path, 
            f"{app_main}/settings.py", 
            str
        )
    



    def update_setting_auth_token(self, full_path, app_main):
        """
        Genera el archivo
        """
        
        helper_insert_after_line(
            full_path,
            f"{app_main}/settings.py",
            "    'rest_framework',                   # required for DRF,",
            "    'rest_framework.authtoken',         # required for DRF token authentication,"
        )
        
        
        print_message(f"Se ha actualizado el archivo {app_main}/settings.py", GREEN)
