import os
from gen.helpers.helper_columns import parse_columns_input
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
    singular_name = "Auth"
    plural_name = "Auths"
    columns = parse_columns_input( "email password")
    
    standard_module_crud_python_django(full_path, app_main, singular_name, plural_name, columns)
    
    