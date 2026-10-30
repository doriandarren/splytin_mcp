import os
from gen.helpers.helper_file import HelperFile


class ReactTsModuleDashboard:
    
    def invoke(self, full_path):
        self.create_file_layout_tsx(full_path)
        self.create_file_dashboard_page_tsx(full_path)
        
        # Header
        self.create_file_custom_admin_header(full_path)
        
        
        # Components Menu
        self.create_user_menu_tsx(full_path)
        
    
    

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

    
        
    def create_file_custom_admin_header(self, full_path):
        """
        Genera el archivo.
        """

    
        folder_path = os.path.join(full_path, "src", "modules", "private", "components")
    
        content = r'''// src/modules/private/components/CustomAdminHeader.tsx
import { PanelsTopLeft } from "lucide-react";
import { Link } from "react-router";

import { UserMenu } from "@/modules/private/components/UserMenu";

export const CustomAdminHeader = () => {
  return (
    <header className="flex items-center justify-between border-b px-6 py-4">

      {/* Logo y nombre de la aplicación */}
      <Link
        to="/admin"
        className="flex items-center gap-2 font-semibold"
      >
        <PanelsTopLeft className="size-5" />
        <span>Splytin ERP</span>
      </Link>

      {/* Menú del usuario */}
      <div className="flex items-center justify-end">
        <UserMenu />
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
        
    
    def create_user_menu_tsx(self, full_path):
        """
        Genera el archivo.
        """
    
        folder_path = os.path.join(full_path, "src", "modules", "private", "components")
    
        content = r'''// src/modules/private/components/UserMenu.tsx
import { Link, useNavigate } from "react-router";

import {
  ChevronDown,
  LogOut,
  Settings,
  UserRound,
} from "lucide-react";

import { Button } from "@/components/ui/button";

import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuGroup,
  DropdownMenuItem,
  DropdownMenuLabel,
  DropdownMenuSeparator,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu";

import { useAuthStore } from "@/modules/auth/stores/authStore";

// Opciones del menú
const menuItems = [
  {
    label: "Mi perfil",
    path: "/admin/profile",
    icon: UserRound,
  },
  {
    label: "Sistemas",
    path: "/admin/systems",
    icon: Settings,
  },
];

export const UserMenu = () => {
  const navigate = useNavigate();

  const user = useAuthStore((state) => state.user);
  const logout = useAuthStore((state) => state.logout);

  const handleLogout = () => {
    logout();
    void navigate("/auth/login", { replace: true });
  };

  return (
    <DropdownMenu>
      <DropdownMenuTrigger
        render={
          <Button variant="ghost" className="gap-2" />
        }
      >
        <UserRound className="size-5" />

        <span className="hidden sm:inline">
          {user?.attributes.name ?? "Mi cuenta"}
        </span>

        <ChevronDown className="size-4" />
      </DropdownMenuTrigger>

      <DropdownMenuContent align="end" className="w-56">

        {/* Grupo de información del usuario */}
        <DropdownMenuGroup>
          <DropdownMenuLabel>
            <div className="flex flex-col gap-1">
              <span>
                {user?.attributes.name ?? "Mi cuenta"}
              </span>

              {user?.attributes.email && (
                <span className="truncate text-xs font-normal text-muted-foreground">
                  {user.attributes.email}
                </span>
              )}
            </div>
          </DropdownMenuLabel>
        </DropdownMenuGroup>

        <DropdownMenuSeparator />

        {/* Grupo de navegación */}
        <DropdownMenuGroup>
          {menuItems.map((item) => {
            const Icon = item.icon;

            return (
              <DropdownMenuItem
                key={item.path}
                render={<Link to={item.path} />}
              >
                <Icon className="size-4" />
                <span>{item.label}</span>
              </DropdownMenuItem>
            );
          })}
        </DropdownMenuGroup>

        <DropdownMenuSeparator />

        {/* Grupo de sesión */}
        <DropdownMenuGroup>
          <DropdownMenuItem
            variant="destructive"
            onClick={handleLogout}
          >
            <LogOut className="size-4" />
            Cerrar sesión
          </DropdownMenuItem>
        </DropdownMenuGroup>

      </DropdownMenuContent>
    </DropdownMenu>
  );
};
'''
    
        # Crear el archivo
        HelperFile.write(
            folder_path=folder_path,
            file_name="UserMenu.tsx",
            content=content
        )