import os
from gen.helpers.helper_file import HelperFile
from gen.helpers.helper_print import print_green, run_command


class ReactTsReactRouter:

    def invoke(self, full_path):
        self.install(full_path)
        self.create_app_router_tsx(full_path)
        


    def install(self, full_path):
        # Instalar dependencias
        run_command(
            "npm install react-router",
            cwd=full_path
        )
        
        print_green("Proyecto creado correctamente.")



    def create_app_router_tsx(self, full_path):
        """
        Genera el archivo.
        """
        
        folder_path = os.path.join(full_path, "src")
    
        content = r'''import { lazy } from "react";
import { createBrowserRouter, Navigate } from "react-router";
import { HomePage } from "./modules/public/home/pages/HomePage";
import { PublicLayout } from "./modules/public/layouts/PublicLayout";
import { LoginPage } from "./modules/auth/login/pages/LoginPage";
import { RegisterPage } from "./modules/auth/register/pages/RegisterPage";
import { DashboardPage } from "./modules/private/dashboard/pages/DashboardPage";
import { ProtectedRoute } from "./modules/auth/components/ProtectedRoute";


const AuthLayout = lazy( () => import('./modules/auth/layouts/AuthLayout'))
const AdminLayout = lazy( () => import('./modules/private/layouts/AdminLayout'))


export const appRouter = createBrowserRouter([
    // Public routes
    {
        path: '/',
        element: <PublicLayout />,
        children: [
            {
                index: true,
                element: <HomePage />
            },
        ]
    },


    // Auth Routes
    {
        path: '/auth',
        element: <AuthLayout />,
        children: [
            {
                path: 'login',
                element: <LoginPage />
            },
            {
                path: 'register',
                element: <RegisterPage />
            }
        ]
    },

    // Private routes
    {
        element: <ProtectedRoute />,
        children: [
        {
            path: "/admin",
            element: <AdminLayout />,
            children: [
            {
                index: true,
                element: <DashboardPage />,
            },
            ],
        },
        ],
    },


    // 
    {
        path: '*',
        element: <Navigate to='/' replace />,
    }

])
'''
    
        # Crear el archivo
        HelperFile.write(
            folder_path=folder_path,
            file_name="app.router.tsx",
            content=content
        )




    

  