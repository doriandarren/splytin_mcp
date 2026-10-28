import os
from gen.helpers.helper_file import HelperFile


class ReactTsModuleDashboard:
    
    def invoke(self, full_path):
        self.create_file_layout_tsx(full_path)
        self.create_file_dashboard_page_tsx(full_path)
        
    
    

    def create_file_layout_tsx(self, full_path):
        """
        Genera el archivo.
        """

        folder_path = os.path.join(full_path, "src", "modules", "private", "layouts")

        content = r'''import { Outlet } from "react-router";

const AdminLayout = () => {
  return (
    <>
      <Outlet />
    </>
  );
};


export default AdminLayout;
'''

        # Crear el archivo
        HelperFile.write(
            folder_path=folder_path,
            file_name="AdminLayout.tsx",
            content=content
        )
        
        
        
    def create_file_dashboard_page_tsx(self, full_path):
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