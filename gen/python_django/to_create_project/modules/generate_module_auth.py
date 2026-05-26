import os
from gen.helpers.helper_columns import parse_columns_input
from gen.python_django.helpers.helper_file import helper_add_import, helper_append_content, helper_insert_after_line, helper_update_line
from gen.python_django.to_create_module_crud.standard_module_crud_python_django import standard_module_crud_python_django
from helpers.helper_print import dd, print_message, GREEN, CYAN



def generate_module_auth(full_path):
    """
    Genera el archivo
    
    EX:
    - full_path: /Users/dorian/PythonProjects/python.splytin.com
    - app_main: main 
    - singular_name: AgendaUnloading 
    - plural_name: AgendaUnloadings 
    - columns: [{'name': 'user_id', 'type': 'fk', 'raw_type': 'fk', 'is_fk': True, 'related_table': 'users', 'related_model': 'User'}, {'name': 'name', 'type': 'string', 'raw_type': 'string', 'is_fk': False}, {'name': 'age', 'type': 'integer', 'raw_type': 'integer', 'is_fk': False}, {'name': 'description', 'type': 'string', 'raw_type': 'string', 'is_fk': False}] 
    - input_menu_checkbox: ['api_route', 'api_serializer', 'api_wiewset', 'api_model', 'api_service']
    
    """
    
    
    app_main = "main"
    singular_name = "Authentication"
    plural_name = "Authentications"
    columns = parse_columns_input("email password")
    input_menu_checkbox=["api_route", "api_serializer", "api_wiewset", "api_model", "api_service"]
    
    
    standard_module_crud_python_django(full_path, app_main, singular_name, plural_name, columns, input_menu_checkbox)
    
    update_router(full_path)
    update_view(full_path)
    update_serializer(full_path)
    
    add_settings(full_path, app_main)
    
    update_setting_auth_token(full_path, app_main)
    



def update_router(full_path):
    """
    Genera el archivo
    """

    folder_path = os.path.join(full_path, "apps", "authentications", "api")
    file_path = os.path.join(folder_path, "router.py")

    ## os.makedirs(folder_path, exist_ok=True)

    content = f'''from django.urls import path
from rest_framework.routers import DefaultRouter
from apps.authentications.api.views import (
    AuthenticationApiViewSet,
    CurrentUserView,
    LoginView,
    LogoutView
)

router_authentication = DefaultRouter()

router_authentication.register(
    prefix='authentications',
    basename='authentications',
    viewset=AuthenticationApiViewSet
)

urlpatterns = [
    path('auth/login/', LoginView.as_view(), name='auth_login'),
    path('auth/user/', CurrentUserView.as_view(), name='auth_user'),
    path('auth/logout/', LogoutView.as_view(), name='auth_logout'),
]
'''

    try:
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)
    


def update_view(full_path):
    """
    Genera el archivo
    """

    folder_path = os.path.join(full_path, "apps", "authentications", "api")
    file_path = os.path.join(folder_path, "views.py")

    ## os.makedirs(folder_path, exist_ok=True)

    content = f'''from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from core.api import BaseAPIView, BaseModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, AllowAny
from apps.authentications.models import Authentication
from apps.users.api.serializers import UserSerializer
from apps.authentications.api.serializers import AuthenticationSerializer


class AuthenticationApiViewSet(BaseModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = AuthenticationSerializer
    queryset = Authentication.objects.all()


class LoginView(BaseAPIView):
    permission_classes = [AllowAny]


    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")

        user = authenticate(
            request,
            username=email,
            password=password
        )

        if user is None:
            return self.respond_with_error(
                message="Invalid credentials",
                status_code=401
            )

        token, created = Token.objects.get_or_create(user=user)

        serialize = UserSerializer(user)

        return self.respond_with_data(
            message="Login successfully",
            data={{
                "token": token.key,
                "user": serialize.data
            }}
        )


class CurrentUserView(BaseAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serialize = UserSerializer(request.user)

        return self.respond_with_data(
            message="Current user retrieved successfully",
            data=serialize.data
        )


class LogoutView(BaseAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        request.user.auth_token.delete()

        return self.respond_with_data(
            message="Logout successfully"
        )

'''

    try:
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)
        


def update_serializer(full_path):
    """
    Genera el archivo
    """

    folder_path = os.path.join(full_path, "apps", "authentications", "api")
    file_path = os.path.join(folder_path, "serializers.py")

    ## os.makedirs(folder_path, exist_ok=True)

    content = f'''from rest_framework.serializers import ModelSerializer
from apps.authentications.models import Authentication


class AuthenticationSerializer(ModelSerializer):

    class Meta:
        model = Authentication
        ## fields = "__all__"
        fields = [
            'id', 
            'email',
            'password',
            'created_at',
            'updated_at',
            'created_by',
            'updated_by',
        ]

'''

    try:
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)
    


def add_settings(full_path, app_main):
    
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
    



def update_setting_auth_token(full_path, app_main):
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
