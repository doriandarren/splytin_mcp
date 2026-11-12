import os
from helpers.helper_columns import HelperColumns
from helpers.helper_file import HelperFile
from gen.react_ts.to_create_module_crud.standard_module_crud_react_ts import StandardModuleCrudReactTs


class ReactTsModuleDashboard:
    
    def invoke(self, full_path):
        self.create_module(full_path)
        self.update_page_tsx(full_path)    
    
    
    
    def create_module(self, full_path):
        columns = HelperColumns.parse_columns_input("name")

        obj = StandardModuleCrudReactTs()
        obj.invoke(
            full_path=full_path,
            namespace="private",
            singular_name="Dashboard",
            plural_name="Dashboards",
            columns=columns,
            input_menu_checkbox=None,
            version_api="V1",
            folder_group="api"
        )
        
        
    
    
    
    def update_page_tsx(self, full_path):
        """
        Genera el archivo.
        """

        folder_path = os.path.join(full_path, "src", "modules", "private", "dashboard", "pages")

        content = r'''export const DashboardPage = () => {
    return (
        <div>DashboardPage</div>
    )
    }
    '''

        # Crear el archivo
        HelperFile.write(
            folder_path=folder_path,
            file_name="DashboardPage.tsx",
            content=content
        )

    
    
