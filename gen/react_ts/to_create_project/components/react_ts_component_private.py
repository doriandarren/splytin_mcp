import os
from helpers.helper_file import HelperFile


class ReactTsComponentPrivate:

    def invoke(self, full_path):
        # Admin Layout
        self.create_admin_layout_tsx(full_path)

        #--------  Components -------------
        # Header
        self.create_file_custom_admin_header(full_path)
        
        # Menu
        self.create_user_menu_tsx(full_path)
        
        # SideBar
        self.create_custom_admin_sidebar_tsx(full_path)
        
        
        

    def create_admin_layout_tsx(self, full_path):
        """
        Genera el archivo.
        """

        folder_path = os.path.join(full_path, "src", "modules", "private", "layouts")

        content = r'''// src/modules/private/layouts/AdminLayout.tsx
import { Outlet } from "react-router";
import { CustomAdminHeader } from "../components/CustomAdminHeader";
import { CustomAdminSidebar } from "../components/CustomAdminSidebar";

import {
    SidebarProvider,
    SidebarInset,
} from "@/components/ui/sidebar";

const AdminLayout = () => {

    return (

        <SidebarProvider defaultOpen={true}>

            {/* Sidebar izquierdo */}
            <CustomAdminSidebar />

            {/* Contenido principal */}
            <SidebarInset className="min-w-0 bg-background">

                {/* Header */}
                <CustomAdminHeader />

                {/* Content */}
                <main className="flex flex-1 flex-col p-6">
                    <Outlet />
                </main>

            </SidebarInset>

        </SidebarProvider>

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


    def create_file_custom_admin_header(self, full_path):
        """
        Genera el archivo.
        """


        folder_path = os.path.join(full_path, "src", "modules", "private", "components")

        content = r'''// src/modules/private/components/CustomAdminHeader.tsx
import { PanelsTopLeft } from "lucide-react";
import { Link } from "react-router";
import { LanguageSelector } from "@/components/languages/LanguageSelector";
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
                <div className="mr-5">
                    <LanguageSelector />
                </div>
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
import { useTranslation } from "react-i18next";
import {
    ChevronDown,
    LogOut,
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
        key: "auth.profile",
        path: "/admin/profiles",
        icon: UserRound,
    }
];

export const UserMenu = () => {
    const navigate = useNavigate();
    const { t } = useTranslation("common");

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
                    {user?.attributes.name ?? t("auth.account")}
                </span>

                <ChevronDown className="size-4" />
            </DropdownMenuTrigger>

            <DropdownMenuContent align="end" className="w-56">

                {/* Grupo de información del usuario */}
                <DropdownMenuGroup>
                    <DropdownMenuLabel>
                        <div className="flex flex-col gap-1">
                            <span>
                                {user?.attributes.name ?? t("auth.account")}
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
                                <span>{t(item.key)}</span>
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
                        {t("auth.logout")}
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
    
    

    def create_custom_admin_sidebar_tsx(self, full_path):
        """
        Genera el archivo.
        """

        folder_path = os.path.join(full_path, "src", "modules", "private", "components")

        content = r'''// src/modules/private/components/CustomAdminSidebar.tsx
import { Link, useLocation } from "react-router";
import { useTranslation } from "react-i18next";
import {
    LayoutDashboard,
    Server,
    Users,
    Droplets,
    Settings,
    PanelsTopLeft,
} from "lucide-react";

import {
    Sidebar,
    SidebarHeader,
    SidebarContent,
    SidebarFooter,
    SidebarGroup,
    SidebarGroupLabel,
    SidebarGroupContent,
    SidebarMenu,
    SidebarMenuItem,
    SidebarMenuButton,
    SidebarRail,
} from "@/components/ui/sidebar";

const menuItems = [
    {
        key: "dashboard",
        path: "/admin",
        icon: LayoutDashboard,
    },
    {
        key: "systems",
        path: "/admin/systems",
        icon: Server,
    },
    {
        key: "teams",
        path: "/admin/teams",
        icon: Users,
    },
    {
        key: "quotes",
        path: "/admin/quotes",
        icon: Droplets,
    },
    {
        key: "settings",
        path: "/admin/settings",
        icon: Settings,
    },
] as const;

export const CustomAdminSidebar = () => {
    const { t } = useTranslation("common");
    const { pathname } = useLocation();

    const isActive = (path: string) => {
        if (path === "/admin") {
            return pathname === "/admin" || pathname === "/admin/";
        }

        return pathname === path || pathname.startsWith(`${path}/`);
    };

    return (
        <Sidebar collapsible="icon" variant="sidebar">
            {/* Logo */}
            <SidebarHeader>
                <SidebarMenu>
                    <SidebarMenuItem>
                        <SidebarMenuButton
                            render={<Link to="/admin" />}
                            tooltip="Splytin ERP"
                            size="lg"
                        >
                            <PanelsTopLeft className="size-5" />
                            <span className="font-semibold">
                                Splytin ERP
                            </span>
                        </SidebarMenuButton>
                    </SidebarMenuItem>
                </SidebarMenu>
            </SidebarHeader>

            {/* Navegación */}
            <SidebarContent>
                <SidebarGroup>
                    <SidebarGroupLabel>
                        {t("navigation")}
                    </SidebarGroupLabel>

                    <SidebarGroupContent>
                        <SidebarMenu>
                            {menuItems.map((item) => {
                                const Icon = item.icon;

                                return (
                                    <SidebarMenuItem key={item.key}>
                                        <SidebarMenuButton
                                            render={<Link to={item.path} />}
                                            isActive={isActive(item.path)}
                                            tooltip={t(item.key)}
                                        >
                                            <Icon className="size-4" />
                                            <span>{t(item.key)}</span>
                                        </SidebarMenuButton>
                                    </SidebarMenuItem>
                                );
                            })}
                        </SidebarMenu>
                    </SidebarGroupContent>
                </SidebarGroup>
            </SidebarContent>

            {/* Pie */}
            <SidebarFooter>
                <div className="px-2 py-2 text-xs text-muted-foreground group-data-[collapsible=icon]:hidden">
                    ERP Edition
                </div>
            </SidebarFooter>

            <SidebarRail />
        </Sidebar>
    );
};
'''

        # Crear el archivo
        HelperFile.write(
            folder_path=folder_path,
            file_name="CustomAdminSidebar.tsx",
            content=content
        )

    
    