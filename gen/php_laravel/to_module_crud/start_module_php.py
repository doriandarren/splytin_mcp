import os
from dotenv import load_dotenv
from gen.helpers.helper_columns import parse_columns_input
from gen.helpers.helper_menu import menu_checkbox, pause
from gen.helpers.helper_print import dd, input_with_validation
from gen.php_laravel.to_module_crud.standard_module_crud_php import standard_module_crud_php


load_dotenv()


def start_module_php():

    opt = [
        ("Modelo", "model"),
        ("Controlador - Index", "controller_index"),
        ("Controlador - Show", "controller_show"),
        ("Controlador - Store", "controller_store"),
        ("Controlador - Update", "controller_update"),
        ("Controlador - Destroy", "controller_destroy"),
        ("Servicio", "service"),
        ("Resource", "resource"),
        ("Rutas", "routes"),
        ("Migración", "migration"),
        ("Seeder", "seeder"),
        ("Factory", "factory"),
        ("Archivo Postman", "postman"),
    ]
    
    #default_path = "/Users/dorian/PhpstormProjects81/api.app1.com"
    #default_path = "/Users/dorian/PHPProjects/docker-laravel-84/projects/api-integrations.transportuarios.com"
    
    default_path = os.getenv("DEFAULT_PATH_CRUD_PHP")
    default_namespace = "API"
    default_api = 'V1'
    
    input_menu_checkbox = menu_checkbox("Componentes: ", opt)


    full_path = input_with_validation("Proyecto", default_path)
    namespace = input_with_validation("Namespace (ERP / API / INVOICES)", default_namespace)
    version_api = input_with_validation("Version API", default_api)
    singular_name = input_with_validation("Nombre singular", "AgendaUnloading")
    plural_name = input_with_validation("Nombre plural", "AgendaUnloadings")
    input_columns = input_with_validation(
        "Columnas (separdo por espacio)", 
        "user_id:fk name:string(30)|unique amount:decimal(10,2) amount_with_tax:float description:varchar(10) note has_active:boolean"
    )
    
    columns = parse_columns_input(input_columns)
    
    ## dd(columns)
    
    
    
    standard_module_crud_php(
        full_path, 
        namespace, 
        version_api, 
        singular_name, 
        plural_name, 
        columns, 
        input_menu_checkbox
    )
    
    pause()
