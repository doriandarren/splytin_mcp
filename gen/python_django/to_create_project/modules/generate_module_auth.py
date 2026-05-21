import os
from gen.helpers.helper_columns import parse_columns_input
from gen.python_django.helpers.helper_file import helper_update_line
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
    
    update_main_urls(full_path, app_main)
    update_router(full_path)
    update_view(full_path)
    update_serializer(full_path)
    
    


def update_main_urls(full_path, app_main):
    """
    Genera el archivo
    """
    helper_update_line(
        full_path,
        f"{app_main}/urls.py",
        f"    path('api/v1/', include(router_authentication.urls)),",
        f"    path('api/v1/', include('apps.authentications.api.router')),"
    )
    
    print_message(f"Se ha actualizado el archivo {app_main}/urls.py", GREEN)




def update_router(full_path):
    """
    Genera el archivo
    """

    folder_path = os.path.join(full_path, "apps", "authentications", "api")
    file_path = os.path.join(folder_path, "router.py")

    ## os.makedirs(folder_path, exist_ok=True)

    content = f'''from django.urls import path
from rest_framework.routers import DefaultRouter
from apps.authentications.api.views import AuthenticationApiViewSet, CurrentUserView, LoginView, LogoutView
from rest_framework_simplejwt.views import TokenRefreshView

# example
router_authentication = DefaultRouter()

# examples
router_authentication.register(
    prefix='authentications',
    basename='authentications',
    viewset=AuthenticationApiViewSet
)

# URLS
urlpatterns = [
    path('auth/login/', LoginView.as_view(), name='token_obtain_pair'),
    path('auth/login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/user/', CurrentUserView.as_view()),
    path('auth/logout/', LogoutView.as_view()),
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

    content = f'''from core.api import BaseAPIView, BaseModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from apps.authentications.models import Authentication
from apps.users.api.serializers import UserSerializer

from apps.authentications.api.serializers import (
    AuthenticationSerializer,
    EmailTokenObtainPairSerializer,
)



class AuthenticationApiViewSet(BaseModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = AuthenticationSerializer
    queryset = Authentication.objects.all()


class LoginView(TokenObtainPairView):
    serializer_class = EmailTokenObtainPairSerializer


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
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import get_user_model
from rest_framework.exceptions import AuthenticationFailed


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


class EmailTokenObtainPairSerializer(TokenObtainPairSerializer):
    username_field = "email"

    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")

        User = get_user_model()

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise AuthenticationFailed("No active account found with the given credentials")

        if not user.is_active or not user.check_password(password):
            raise AuthenticationFailed("No active account found with the given credentials")

        refresh = self.get_token(user)

        return {{
            "refresh": str(refresh),
            "token": str(refresh.access_token),
            "user": {{
                "id": user.id,
                "username": user.username,
                "email": user.email,
                "first_name": user.first_name,
                "last_name": user.last_name,
            }}
        }}
    
'''

    try:
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)
    







    
    