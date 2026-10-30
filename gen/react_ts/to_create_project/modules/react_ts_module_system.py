import os
from gen.helpers.helper_columns import parse_columns_input
from gen.react_ts.to_create_module_crud.standard_module_crud_react_ts import StandardModuleCrudReactTs


class ReactTsModuleSystem:
    
    def invoke(self, full_path):
        self.create_crud(full_path)
        
        

    def create_crud(self, full_path):
        """
        Genera CRUD
        """
        
        columns = parse_columns_input("name status version")

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