import os
from gen.helpers.helper_columns import parse_columns_input
from gen.python_django.helpers.helper_file import helper_update_line
from gen.python_django.to_create_module_crud.standard_module_crud_python_django import standard_module_crud_python_django
from helpers.helper_print import print_message, GREEN, CYAN



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
    
    
    ## TODO actualizar el archivo de routes
    
    update_router(full_path)
    update_user_views(full_path)
    update_main_urls(full_path, app_main)


    
    

def update_router(full_path):
    """
    Genera el archivo
    """

    folder_path = os.path.join(full_path, "apps", "authentications", "api")
    file_path = os.path.join(folder_path, "router.py")

    ## os.makedirs(folder_path, exist_ok=True)

    content = f'''from django.urls import path
from rest_framework.routers import DefaultRouter
from apps.authentications.api.views import AuthenticationApiViewSet
from apps.users.api.views import UserView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# Add urls.py:
# from apps.authentications.api.router import router_authentication
# path('api/v1/', include(router_authentication.urls)),


# example
router_authentication = DefaultRouter()

# examples
router_authentication.register(
    prefix='authentications',
    basename='authentications',
    viewset=AuthenticationApiViewSet
)



urlpatterns = [
    path('auth/me/', UserView.as_view()),
    path('auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

'''

    try:
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)
    
    


def update_user_views(full_path):
    """
    Genera el archivo
    """

    folder_path = os.path.join(full_path, "apps", "users", "api")
    file_path = os.path.join(folder_path, "views.py")

    # os.makedirs(folder_path, exist_ok=True)

    content = f'''from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
#from django_filters.rest_framework import DjangoFilterBackend

from apps.users.api.serializers import UserSerializer
from apps.users.models import User


class UserApiViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = UserSerializer
    queryset = User.objects.all()
    # Filtros...
    #filter_backends = [DjangoFilterBackend]
    #filterset_fields = ['category', 'active']



class UserView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        serialize = UserSerializer(request.user)
        return Response(serialize.data)
'''

    try:
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)
        


def update_main_urls(full_path, app_main):
    """
    Genera el archivo
    """

    helper_update_line(
        full_path,
        f"{app_main}/urls.py",
        f"path('api/v1/', include(router_authentication.urls)),",
        f"path('api/v1/', include('apps.authentications.api.router')),"
    )