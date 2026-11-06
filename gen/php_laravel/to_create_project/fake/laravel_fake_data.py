import os
from gen.helpers.helper_columns import HelperColumns
from gen.php_laravel.to_module_crud.standard_module_crud_php import standard_module_crud_php


class LaravelFakeData:

    def invoke(self, full_path):
        
        ## By all:
        input_menu_checkbox = [
            "model",
            "controller_index",
            "controller_show",
            "controller_store",
            "controller_update",
            "controller_destroy",
            "service",
            "routes",
            "resource",
            "seeder",
            "factory",
            "postman",
            "migration",
        ]
        
        
        namespace = "API"
        folder_group = None
        
        
        
        # Systems
        singular_name = "System"
        plural_name = "Systems"
        input_columns = "name status version"
        columns = HelperColumns.parse_columns_input(input_columns)
        
        
        standard_module_crud_php(
            full_path=full_path, 
            namespace=namespace, 
            version_api='V1',
            folder_group=folder_group,
            singular_name=singular_name, 
            plural_name=plural_name, 
            columns=columns, 
            input_menu_checkbox=input_menu_checkbox
        )
        
        
        
        
        # Teams
        singular_name = "Team"
        plural_name = "Teams"
        input_columns = "name description"
        columns = HelperColumns.parse_columns_input(input_columns)
        
        
        standard_module_crud_php(
            full_path=full_path, 
            namespace=namespace, 
            version_api='V1',
            folder_group=folder_group,
            singular_name=singular_name, 
            plural_name=plural_name, 
            columns=columns, 
            input_menu_checkbox=input_menu_checkbox
        )
        
        
        
        # Quotes
        singular_name = "Quote"
        plural_name = "Quotes"
        input_columns = "author feedback title"
        columns = HelperColumns.parse_columns_input(input_columns)
        
        
        standard_module_crud_php(
            full_path=full_path, 
            namespace=namespace, 
            version_api='V1',
            folder_group=folder_group,
            singular_name=singular_name, 
            plural_name=plural_name, 
            columns=columns, 
            input_menu_checkbox=input_menu_checkbox
        )
        