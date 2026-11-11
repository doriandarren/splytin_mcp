import os
from gen.helpers.helper_columns import HelperColumns
from gen.helpers.helper_file import HelperFile
from gen.python_django.to_create_module_crud.standard_module_crud_python_django import StandardModuleCrudPythonDjango


class DjModuleCountry:


    def invoke(self, full_path, app_main):
        self.create_module(full_path, app_main)
        
        
     
    def create_module(self, full_path, app_main):
        
        ######################
        # Country
        ######################
        singular_name = "Country"
        plural_name = "Countries"
        columns = HelperColumns.parse_columns_input(
            "common_name iso_name code_alpha_2 code_alpha_3 numerical_code phone_code"
        )
        
        obj = StandardModuleCrudPythonDjango()
        obj.invoke(
            full_path,
            app_main,
            singular_name,
            plural_name,
            columns
        )
        
        
        
        
    def create_(self, full_path):
        """
        Genera el archivo.
        """

        folder_path = os.path.join(full_path, "core")

        content = r'''# '''

        # Crear el archivo
        HelperFile.write(
            folder_path=folder_path,
            file_name="X.py",
            content=content
        )