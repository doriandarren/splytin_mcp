import os
from helpers.helper_columns import HelperColumns
from gen.react_ts.to_create_module_crud.standard_module_crud_react_ts import StandardModuleCrudReactTs


class ReactTsModuleFake:
    
    def invoke(self, full_path):
        # System
        self.create_crud_system(full_path)
        
        # Quote
        self.create_crud_quote(full_path)
        
        # Teams
        self.create_crud_teams(full_path)
        
        

    def create_crud_system(self, full_path):
        """
        Genera CRUD
        """
        columns = HelperColumns.parse_columns_input("name status version")

        obj = StandardModuleCrudReactTs()
        obj.invoke(
            full_path=full_path,
            namespace="private",
            singular_name="System",
            plural_name="Systems",
            columns=columns,
            input_menu_checkbox=None,
            version_api="V1",
            folder_group="api"
        )
        
        
    def create_crud_quote(self, full_path):
        """
        Genera CRUD
        """
        columns = HelperColumns.parse_columns_input("author feedback title")

        obj = StandardModuleCrudReactTs()
        obj.invoke(
            full_path=full_path,
            namespace="private",
            singular_name="Quote",
            plural_name="Quotes",
            columns=columns,
            input_menu_checkbox=None,
            version_api="V1",
            folder_group="api"
        )
        
        
    def create_crud_teams(self, full_path):
        """
        Genera CRUD
        """
        columns = HelperColumns.parse_columns_input("name description")

        obj = StandardModuleCrudReactTs()
        obj.invoke(
            full_path=full_path,
            namespace="private",
            singular_name="Team",
            plural_name="Teams",
            columns=columns,
            input_menu_checkbox=None,
            version_api="V1",
            folder_group="api"
        )