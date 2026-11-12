from helpers.helper_columns import HelperColumns
from gen.python_django.helpers.helper_dj_data_fake import HelperDjDataFake
from gen.python_django.to_create_module_crud.standard_module_crud_python_django import StandardModuleCrudPythonDjango


class DjModuleDefaults:
    
    def __init__(self) -> None:
        self.module_crud = StandardModuleCrudPythonDjango()
    

    def invoke(self, full_path, app_main):
        """
        Genera el archivo.
        """
        
        
        ## TODO borrar luego solo para PRuebas:
        obj = HelperDjDataFake()
        obj.invoke(full_path, app_main)
        
        
        
        
        ######################
        # Systems
        ######################
        singular_name = "System"
        plural_name = "Systems"
        columns = HelperColumns.parse_columns_input(
            "name status version"
        )
        self.module_crud.invoke(
            full_path,
            app_main,
            singular_name,
            plural_name,
            columns
        )
        
        
        
        
        ######################
        # Teams
        ######################
        singular_name = "Team"
        plural_name = "Teams"
        columns = HelperColumns.parse_columns_input(
            "name description"
        )
        self.module_crud.invoke(
            full_path,
            app_main,
            singular_name,
            plural_name,
            columns
        )
        
        
        
        ######################
        # Quotes
        ######################
        singular_name = "Quote"
        plural_name = "Quotes"
        columns = HelperColumns.parse_columns_input(
            "author feedback title"
        )
        self.module_crud.invoke(
            full_path,
            app_main,
            singular_name,
            plural_name,
            columns
        )
        