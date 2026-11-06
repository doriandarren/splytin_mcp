import os
from gen.helpers.helper_print import camel_to_kebab, camel_to_snake, print_cyan, print_message
from gen.helpers.helper_string import normalize_project_name
from gen.helpers.helpers import dd
from gen.python_django.helpers.helper_virtual_env import get_venv_python
from gen.python_django.to_create_module_crud.dj_crud_api_model import DjCrudApiModel
from gen.python_django.to_create_module_crud.dj_crud_api_postman import DjCrudApiPostman
from gen.python_django.to_create_module_crud.dj_crud_api_route import DjCrudApiRoute
from gen.python_django.to_create_module_crud.dj_crud_api_seeder import DjCrudApiSeeder
from gen.python_django.to_create_module_crud.dj_crud_api_serializer import DjCrudApiSerializer
from gen.python_django.to_create_module_crud.dj_crud_api_service import DjCrudApiService
from gen.python_django.to_create_module_crud.dj_crud_api_viewset import DjCrudApiViewset
from gen.python_django.to_create_module_crud.dj_crud_app import DjCrudApp
from gen.python_django.to_create_module_crud.dj_crud_update_installed_apps import DjCrudUpdateInstalledApps


def standard_module_crud_python_django(
    full_path, 
    app_main, 
    singular_name, 
    plural_name, 
    columns, 
    input_menu_checkbox=None
):
    """
    Crea el modulo
    
    EX:
    - full_path: /Users/dorian/PythonProjects/python.splytin.com
    - app_main: main 
    - singular_name: AgendaUnloading 
    - plural_name: AgendaUnloadings 
    - columns: [{'name': 'user_id', 'type': 'fk', 'raw_type': 'fk', 'is_fk': True, 'related_table': 'users', 'related_model': 'User'}, {'name': 'name', 'type': 'string', 'raw_type': 'string', 'is_fk': False}, {'name': 'age', 'type': 'integer', 'raw_type': 'integer', 'is_fk': False}, {'name': 'description', 'type': 'string', 'raw_type': 'string', 'is_fk': False}] 
    - input_menu_checkbox: ['api_route', 'api_serializer', 'api_wiewset', 'api_model', 'api_service']
    
    """

    # Input Default
    if input_menu_checkbox is None:
        input_menu_checkbox = [
            "api_route", 
            "api_serializer", 
            "api_wiewset", 
            "api_model", 
            "api_service",
            "api_postman"
        ]

    # Convertir nombres
    singular_name_kebab = camel_to_kebab(singular_name)
    plural_name_kebab = camel_to_kebab(plural_name)
    singular_name_snake = camel_to_snake(singular_name)
    plural_name_snake = camel_to_snake(plural_name)
    
    ## Project Name
    temp_name = os.path.basename(full_path.rstrip(os.sep))
    project_name = normalize_project_name(temp_name)
    

    # Camel (para services)
    singular_first_camel = singular_name[:1].lower() + singular_name[1:]
    plural_first_camel = plural_name[:1].lower() + plural_name[1:]
    
    
    # Load virtualenv
    venv_python = get_venv_python(full_path)
    manage_py_path = os.path.join(full_path, "manage.py")
    
    
    
    print_cyan("-" * 20)
    print_cyan(f"Instalando MODULE: {singular_name}")
    
    # Update installed apps
    obj = DjCrudUpdateInstalledApps()
    obj.invoke(
        full_path, 
        app_main, 
        singular_name,
        plural_name_snake,
        manage_py_path, 
        venv_python
    )
    
    
    # Generate app
    obj = DjCrudApp()
    obj.invoke(
        full_path,
        plural_name_snake,
        venv_python,
        manage_py_path
    )
    
    
    
    ## Generate Route
    if "api_route" in input_menu_checkbox:
        obj = DjCrudApiRoute()
        obj.invoke(
            full_path,
            project_name,
            app_main,
            singular_name,
            plural_name,
            singular_name_kebab,
            plural_name_kebab,
            singular_name_snake,
            plural_name_snake,
            singular_first_camel,
            plural_first_camel,
            columns
        )
        
    
    ## Generate Serializer 
    if "api_serializer" in input_menu_checkbox:
        obj = DjCrudApiSerializer()
        obj.invoke(
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
            columns
        )
        
    
    ## Generate Viewset
    if "api_wiewset" in input_menu_checkbox:
        obj = DjCrudApiViewset()
        obj.invoke(
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
            columns
        )
    
    ## Generate Model
    if "api_model" in input_menu_checkbox:
        ## Model
        obj = DjCrudApiModel()
        obj.invoke(
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
            columns
        )
         
        
        ## Seeder
        obj = DjCrudApiSeeder()
        obj.invoke(
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
            columns
        )
        
        
        
        
    ## Generate Service
    if "api_service" in input_menu_checkbox:
        obj = DjCrudApiService()
        obj.invoke(
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
        )
    
    
    
    ## Generate Postman
    if "api_postman" in input_menu_checkbox:
        obj = DjCrudApiPostman()
        obj.invoke(
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
            columns
        )
    
    print_cyan("-" * 20)