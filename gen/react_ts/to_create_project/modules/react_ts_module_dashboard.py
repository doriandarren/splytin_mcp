import os
from gen.helpers.helper_file import HelperFile


class ReactTsModuleDashboard:
    
    def invoke(self, full_path):
        self.create_file_layout_tsx(full_path)
        self.create_file_dashboard_page_tsx(full_path)
        
        # Header
        self.create_file_custom_admin_hader(full_path)
        
    
    

    def create_file_layout_tsx(self, full_path):
        """
        Genera el archivo.
        """

        folder_path = os.path.join(full_path, "src", "modules", "private", "layouts")

        content = r'''import { Outlet } from "react-router";
import { CustomAdminHeader } from "../components/CustomAdminHeader";


const AdminLayout = () => {
  
  return (

    <div className="min-h-screen bg-background">
      
      {/* Header */}
      <CustomAdminHeader />

      {/* Content */}
      <main className="p-6">
        <Outlet />
      </main>

    </div>

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

    
        
    def create_file_custom_admin_hader(self, full_path):
        """
        Genera el archivo.
        """

    
        folder_path = os.path.join(full_path, "src", "modules", "private", "components")
    
        content = r'''import { Button } from "@/components/ui/button";
import { useAuthUser } from "@/modules/auth/hooks/useAuthUser";
import { useAuthStore } from "@/modules/auth/stores/authStore";
import { PanelsTopLeft, LogOut, UserCheck2Icon } from "lucide-react";
import { useNavigate } from "react-router";

export const CustomAdminHeader = () => {
  const navigate = useNavigate();

  const logout = useAuthStore((state) => state.logout);

  const { data } = useAuthUser();
  const user = data?.data;

  const handleLogout = () => {
    logout();
    void navigate("/auth/login", { replace: true });
  };

  return (
    <header className="flex items-center justify-between border-b px-6 py-4">
      <div className="flex items-center gap-2 font-semibold">
        <PanelsTopLeft className="size-5" />
        Splytin ERP
      </div>

      <div className="flex items-end justify-end">
        <div className="flex mr-5 text-l">
          <span className="mr-2"><UserCheck2Icon className="size-5" /></span>
          {user?.attributes.name}
        </div>
        <Button variant="outline" onClick={handleLogout}>
          <LogOut className="size-4" />
          Cerrar sesión
        </Button>
      </div>
    </header>
  );
};

'''
    
        # Crear el archivo
        HelperFile.write(
            folder_path=folder_path,
            file_name="CustomAdminHeader.tsx",
            content=content
        )