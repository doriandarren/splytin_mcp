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

        content = r'''import { Outlet, useNavigate } from "react-router";
import { LogOut, PanelsTopLeft } from "lucide-react";

import { Button } from "@/components/ui/button";
import { useAuthStore } from "@/modules/auth/stores/authStore";

const AdminLayout = () => {
  const navigate = useNavigate();

  const logout = useAuthStore((state) => state.logout);

  const handleLogout = () => {
    logout();
    void navigate("/auth/login", { replace: true });
  };

  return (
    <div className="min-h-screen bg-background">
      <header className="flex items-center justify-between border-b px-6 py-4">
        <div className="flex items-center gap-2 font-semibold">
          <PanelsTopLeft className="size-5" />
          Splytin ERP
        </div>

        <Button variant="outline" onClick={handleLogout}>
          <LogOut className="size-4" />
          Cerrar sesión
        </Button>
      </header>

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