import os
from gen.helpers.helper_menu import pause
from gen.helpers.helper_print import camel_to_first_letter_lower, camel_to_kebab, camel_to_snake, dd, print_cyan
from gen.helpers.helper_string import normalize_project_name
from gen.php_laravel.to_module_crud.laravel_crud_filter import LaravelCrudFilter
from gen.php_laravel.to_module_crud.laravel_crud_model import LaravelCrudModel
from gen.php_laravel.to_module_crud.laravel_crud_permissions_abilities import LaravelCrudPermission
from gen.php_laravel.to_module_crud.laravel_crud_policy import LaravelCrudPolicy
from gen.php_laravel.to_module_crud.laravel_crud_request_store import LaravelCrudRequestStore
from gen.php_laravel.to_module_crud.laravel_crud_request_update import LaravelCrudRequestUpdate
from gen.php_laravel.to_module_crud.laravel_crud_resource import LaravelCrudResource
from gen.php_laravel.to_module_crud.laravel_crud_routes import LaravelCrudRoute
from gen.php_laravel.to_module_crud.laravel_crud_controller_show import LaravelCrudControllerShow
from gen.php_laravel.to_module_crud.laravel_crud_controller_store import LaravelCrudControllerStore
from gen.php_laravel.to_module_crud.laravel_crud_controller_update import LaravelCrudControllerUpdate
from gen.php_laravel.to_module_crud.laravel_crud_seeder import LaravelCrudSeeder
from gen.php_laravel.to_module_crud.laravel_crud_factory import LaravelCrudFactory
from gen.php_laravel.to_module_crud.laravel_crud_controller_destroy import LaravelCrudControllerDestroy
from gen.php_laravel.to_module_crud.laravel_crud_controller_index import LaravelCrudControllerIndex
from gen.php_laravel.to_module_crud.laravel_crud_postman import LaravelCrudPostman
from gen.php_laravel.to_module_crud.laravel_crud_service import LaravelCrudService
from gen.php_laravel.to_module_crud.laravel_crud_migration import LaravelCrudMigration


def standard_module_crud_php(
    full_path,
    namespace,
    version_api,
    folder_group,
    singular_name, 
    plural_name, 
    columns, 
    input_menu_checkbox=None,
):

    # Input Default
    if input_menu_checkbox is None:
        input_menu_checkbox = [
            "controller_index", 
            "controller_show", 
            "controller_store", 
            "controller_update",
            "controller_destroy",
            "model", 
            "service", 
            "resource", 
            "routes",
            "migration", 
            "seeder", 
            "factory", 
            "postman"
        ]

    # Convertir singular_name y plural_name a kebab-case para las URLs
    singular_name_kebab = camel_to_kebab(singular_name)
    plural_name_kebab = camel_to_kebab(plural_name)
    singular_name_snake = camel_to_snake(singular_name)
    plural_name_snake = camel_to_snake(plural_name)
    singular_name_camel = camel_to_first_letter_lower(singular_name)
    plural_name_camel = camel_to_first_letter_lower(plural_name)
    
    
    
    ## Project Name
    temp_name = os.path.basename(full_path.rstrip(os.sep))
    project_name = normalize_project_name(temp_name)
    
    
    ##dd(singular_name + " / " + plural_name + " / " + singular_name_kebab + " / " + plural_name_kebab + " / " + singular_name_snake + " / " + plural_name_snake)
    
    
    print_cyan("-" * 20)
    print_cyan(f"Instalando APP: {singular_name}")
    

        
    #--------------------------
    # Model
    #--------------------------
    if "model" in input_menu_checkbox:
        obj = LaravelCrudModel()
        obj.invoke(
            full_path, 
            namespace,
            singular_name, 
            plural_name, 
            plural_name_snake,
            columns
        )

    #--------------------------
    # Controller - Index
    #--------------------------
    if "controller_index" in input_menu_checkbox:
        
        obj = LaravelCrudControllerIndex()
        obj.invoke(
            full_path,
            namespace,
            version_api,
            folder_group,
            project_name,
            singular_name,
            plural_name,
            singular_name_camel,
            plural_name_camel,
            singular_name_kebab,
            plural_name_kebab,
            singular_name_snake,
            plural_name_snake,
            columns
        )
        
        obj = LaravelCrudFilter()
        obj.invoke(
            full_path,
            namespace,
            version_api,
            folder_group,
            project_name,
            singular_name,
            plural_name,
            singular_name_camel,
            plural_name_camel,
            singular_name_kebab,
            plural_name_kebab,
            singular_name_snake,
            plural_name_snake,
            columns
        )
        
        
    #--------------------------
    # Controller - Show
    #--------------------------
    if "controller_show" in input_menu_checkbox:
        obj = LaravelCrudControllerShow()
        obj.invoke(
            full_path,
            namespace,
            version_api,
            folder_group,
            project_name,
            singular_name,
            plural_name,
            singular_name_camel,
            plural_name_camel,
            singular_name_kebab,
            plural_name_kebab,
            singular_name_snake,
            plural_name_snake,
            columns
        )


    #--------------------------
    # Controller - Store
    #--------------------------
    if "controller_store" in input_menu_checkbox:
        ## Create Controller
        obj = LaravelCrudControllerStore()
        obj.invoke(
            full_path,
            namespace,
            version_api,
            folder_group,
            project_name,
            singular_name,
            plural_name,
            singular_name_camel,
            plural_name_camel,
            singular_name_kebab,
            plural_name_kebab,
            singular_name_snake,
            plural_name_snake,
            columns
        )
        
        ## Create Request
        obj = LaravelCrudRequestStore()
        obj.invoke(
            full_path,
            namespace,
            version_api,
            folder_group,
            project_name,
            singular_name,
            plural_name,
            singular_name_camel,
            plural_name_camel,
            singular_name_kebab,
            plural_name_kebab,
            singular_name_snake,
            plural_name_snake,
            columns
        )
        

    #--------------------------
    # Controller - Update
    #--------------------------
    if "controller_update" in input_menu_checkbox:
        ## Create Controller 
        obj = LaravelCrudControllerUpdate()
        obj.invoke(
            full_path,
            namespace,
            version_api,
            folder_group,
            project_name,
            singular_name,
            plural_name,
            singular_name_camel,
            plural_name_camel,
            singular_name_kebab,
            plural_name_kebab,
            singular_name_snake,
            plural_name_snake,
            columns
        )
        
        
        
        ## Generate Request
        obj = LaravelCrudRequestUpdate()
        obj.invoke(
            full_path,
            namespace,
            version_api,
            folder_group,
            project_name,
            singular_name,
            plural_name,
            singular_name_camel,
            plural_name_camel,
            singular_name_kebab,
            plural_name_kebab,
            singular_name_snake,
            plural_name_snake,
            columns
        )
        
        
    #--------------------------
    # Controller - Destroy
    #--------------------------
    if "controller_destroy" in input_menu_checkbox:
        obj = LaravelCrudControllerDestroy()
        obj.invoke(
            full_path,
            namespace,
            version_api,
            folder_group,
            project_name,
            singular_name,
            plural_name,
            singular_name_camel,
            plural_name_camel,
            singular_name_kebab,
            plural_name_kebab,
            singular_name_snake,
            plural_name_snake,
            columns
        )
    
    
    #--------------------------
    # Service
    #--------------------------
    if "service" in input_menu_checkbox:
        obj = LaravelCrudService()
        obj.invoke(
            full_path,
            namespace,
            version_api,
            folder_group,
            singular_name,
            plural_name,
            singular_name_camel,
            plural_name_camel,
            singular_name_kebab,
            plural_name_kebab,
            singular_name_snake,
            plural_name_snake,
            columns
        )


    #--------------------------
    # Route
    #--------------------------
    if "routes" in input_menu_checkbox:
        obj = LaravelCrudRoute()
        obj.invoke(
            full_path,
            namespace,
            version_api,
            folder_group,
            singular_name,
            plural_name,
            singular_name_camel,
            plural_name_camel,
            singular_name_kebab,
            plural_name_kebab,
            singular_name_snake,
            plural_name_snake,
            columns
        )
        

    #--------------------------
    # Migration
    #--------------------------
    if "migration" in input_menu_checkbox:
        obj = LaravelCrudMigration()
        obj.invoke(
            full_path,
            namespace,
            version_api,
            folder_group,
            singular_name,
            plural_name,
            singular_name_camel,
            plural_name_camel,
            singular_name_kebab,
            plural_name_kebab,
            singular_name_snake,
            plural_name_snake,
            columns
        )


    #--------------------------
    # Seeder
    #--------------------------
    if "seeder" in input_menu_checkbox:
        obj = LaravelCrudSeeder()
        obj.invoke(
            full_path,
            namespace,
            version_api,
            project_name,
            singular_name,
            plural_name,
            singular_name_camel,
            plural_name_camel,
            singular_name_kebab,
            plural_name_kebab,
            singular_name_snake,
            plural_name_snake,
            columns
        )


    #--------------------------
    # Factory
    #--------------------------
    if "factory" in input_menu_checkbox:
        obj = LaravelCrudFactory()
        obj.invoke(
            full_path,
            namespace,
            version_api,
            project_name,
            singular_name,
            plural_name,
            singular_name_camel,
            plural_name_camel,
            singular_name_kebab,
            plural_name_kebab,
            singular_name_snake,
            plural_name_snake,
            columns
        )


    #--------------------------
    # Postman
    #--------------------------
    if "postman" in input_menu_checkbox:
        obj = LaravelCrudPostman()
        obj.invoke(
            full_path, 
            singular_name, 
            plural_name,
            singular_name_kebab, 
            plural_name_kebab, 
            columns
        )
    
    #--------------------------
    # Resource
    #--------------------------
    if "resource" in input_menu_checkbox:
        obj = LaravelCrudResource()
        obj.invoke(
            full_path,
            namespace,
            version_api,
            project_name,
            singular_name,
            plural_name,
            singular_name_camel,
            plural_name_camel,
            singular_name_kebab,
            plural_name_kebab,
            singular_name_snake,
            plural_name_snake,
            columns
        )


    
    #--------------------------
    # Policy
    #--------------------------
    obj = LaravelCrudPolicy()
    obj.invoke(
        full_path,
        namespace,
        version_api,
        folder_group,
        project_name,
        singular_name,
        plural_name,
        singular_name_camel,
        plural_name_camel,
        singular_name_kebab,
        plural_name_kebab,
        singular_name_snake,
        plural_name_snake,
        columns
    )



    
    #--------------------------
    # Permissions
    #--------------------------
    obj = LaravelCrudPermission()
    obj.invoke(
        full_path,
        namespace,
        version_api,
        folder_group,
        project_name,
        singular_name,
        plural_name,
        singular_name_camel,
        plural_name_camel,
        singular_name_kebab,
        plural_name_kebab,
        singular_name_snake,
        plural_name_snake,
        columns
    )
        
        
    print_cyan("-" * 20)

