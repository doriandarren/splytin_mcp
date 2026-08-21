import os
from gen.helpers.helper_menu import pause
from gen.helpers.helper_print import camel_to_kebab, camel_to_snake
from gen.php_laravel.to_module_crud.generate_model_file import generate_model_file
from gen.php_laravel.to_module_crud.generate_request_store import generate_request_store
from gen.php_laravel.to_module_crud.generate_routes_file import generate_routes_file
from gen.php_laravel.to_module_crud.generate_migration_file import generate_migration_file
from gen.php_laravel.to_module_crud.generate_controller_list_file import generate_controller_list_file
from gen.php_laravel.to_module_crud.generate_controller_show_file import generate_controller_show_file
from gen.php_laravel.to_module_crud.generate_controller_store_file import generate_controller_store_file
from gen.php_laravel.to_module_crud.generate_controller_update_file import generate_controller_update_file
from gen.php_laravel.to_module_crud.generate_controller_destroy_file import generate_controller_destroy_file
from gen.php_laravel.to_module_crud.generate_seeder_file import generate_seeder_file
from gen.php_laravel.to_module_crud.generate_factory_file import generate_factory_file
from gen.php_laravel.to_module_crud.generate_postman_file import generate_postman_file
from gen.php_laravel.to_module_crud.generate_service_file import generate_service_file


def standard_module_crud_php(
    full_path,
    namespace,
    singular_name, 
    plural_name, 
    columns, 
    input_menu_checkbox=None
):

    # Input Default
    if input_menu_checkbox is None:
        input_menu_checkbox = [
            "model", 
            "controller_list", 
            "controller_show", 
            "controller_store", 
            "controller_update",
            "controller_destroy",
            "service", "routes",
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
    

    if os.path.isdir(full_path):
        
        if "model" in input_menu_checkbox:
            generate_model_file(
                full_path, 
                namespace,
                singular_name, 
                plural_name, 
                plural_name_snake
            )

        if "controller_list" in input_menu_checkbox:
            generate_controller_list_file(
                full_path, 
                namespace, 
                singular_name, 
                plural_name,
                singular_name_kebab, 
                plural_name_kebab, 
                singular_name_snake, 
                plural_name_snake, 
                columns
            )

        if "controller_show" in input_menu_checkbox:
            generate_controller_show_file(
                full_path,
                namespace, 
                singular_name, 
                plural_name, 
                singular_name_snake, 
                plural_name_snake
            )

        if "controller_store" in input_menu_checkbox:
            
            # Generate Controller
            generate_controller_store_file(
                full_path, 
                namespace, 
                singular_name, 
                plural_name,
                singular_name_kebab, 
                plural_name_kebab, 
                singular_name_snake, 
                plural_name_snake, 
                columns
            )
            
            ## Generate Request
            # generate_request_store(
            #     full_path, 
            #     namespace,
            #     singular_name, 
            #     plural_name,
            #     singular_name_kebab, 
            #     plural_name_kebab, 
            #     singular_name_snake, 
            #     plural_name_snake,
            #     columns
            # )
            

        if "controller_update" in input_menu_checkbox:
            
            ## Controller 
            generate_controller_update_file(
                full_path, 
                namespace, 
                singular_name, 
                plural_name,
                singular_name_kebab, 
                plural_name_kebab, 
                singular_name_snake, 
                plural_name_snake, 
                columns
            )
            
            ## TODO agregar 
            ## generate_request_update(
            
            

        if "controller_destroy" in input_menu_checkbox:
            generate_controller_destroy_file(
                full_path, 
                namespace, 
                singular_name, 
                plural_name,
                singular_name_kebab, 
                plural_name_kebab, 
                singular_name_snake, 
                plural_name_snake, 
                columns
            )
        

        if "service" in input_menu_checkbox:
            generate_service_file(
                full_path, 
                namespace, 
                singular_name,
                plural_name, 
                singular_name_snake, 
                plural_name_snake, 
                columns
            )

        if "routes" in input_menu_checkbox:
            generate_routes_file(
                full_path, 
                namespace,
                plural_name, 
                singular_name,
                singular_name_kebab, 
                plural_name_kebab, 
                singular_name_snake, 
                plural_name_snake
            )

        if "migration" in input_menu_checkbox:
            generate_migration_file(
                full_path, 
                namespace, 
                singular_name, 
                plural_name,
                singular_name_kebab, 
                plural_name_kebab, 
                singular_name_snake, 
                plural_name_snake, 
                columns
            )

        if "seeder" in input_menu_checkbox:
            generate_seeder_file(
                full_path, 
                namespace,
                singular_name, 
                plural_name,
                singular_name_snake, 
                plural_name_snake, 
                columns
            )

        if "factory" in input_menu_checkbox:
            generate_factory_file(
                full_path, 
                namespace,
                singular_name,
                plural_name, 
                singular_name_snake, 
                plural_name_snake, 
                columns
            )

        if "postman" in input_menu_checkbox:
            generate_postman_file(
                full_path, 
                singular_name, 
                plural_name,
                singular_name_kebab, 
                plural_name_kebab, 
                columns
            )

    else:
        print("La ruta proporcionada no es válida o no existe. Por favor, verifica y vuelve a intentarlo.")
