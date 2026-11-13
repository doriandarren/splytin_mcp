import os
from helpers.helper_file import HelperFile


class ReactTsModuleHome:
    
    def invoke(self, full_path):
        self.create_home_page_tsx(full_path)
        self.create_public_layout_tsx(full_path)
        

    def create_public_layout_tsx(self, full_path):
        """
        Genera el archivo.
        """

        folder_path = os.path.join(full_path, "src", "modules", "public", "layouts")

        content = r'''// src/modules/public/layouts/PublicLayout.tsx
import { Outlet } from "react-router";
import { CustomFooter } from "../components/CustomFooter";
import CustomHeader from "../components/CustomHeader";

export const PublicLayout = () => {
    return (
        <div className="flex min-h-screen flex-col bg-background">
            <CustomHeader />
            <main className="flex-1">
                <Outlet />
            </main>
            <CustomFooter />
        </div>
    );
};
'''

        # Crear el archivo
        HelperFile.write(
            folder_path=folder_path,
            file_name="PublicLayout.tsx",
            content=content
        )
        
        
        
    
    def create_home_page_tsx(self, full_path):
            """
            Genera el archivo.
            """
    
            folder_path = os.path.join(full_path, "src", "modules", "public", "home", "pages")
    
            content = r'''// src/modules/public/home/pages/HomePage.tsx
import {
    LayoutDashboard,
    Users,
    ShieldCheck,
} from "lucide-react";

import { CustomJumbotron } from "../../components/CustomJumbotron";

// Funcionalidades principales
const features = [
    {
        icon: LayoutDashboard,
        title: "Control centralizado",
        description:
            "Consulta la información de tu empresa desde un único panel de gestión.",
    },
    {
        icon: Users,
        title: "Gestión organizada",
        description:
            "Administra clientes, sistemas y procesos de forma sencilla y eficiente.",
    },
    {
        icon: ShieldCheck,
        title: "Acceso seguro",
        description:
            "Accede a tu espacio de trabajo mediante una cuenta de usuario.",
    },
];

export const HomePage = () => {
    return (
        <main>
            {/* Sección principal */}
            <CustomJumbotron
                title="Todo tu negocio. Un solo lugar."
                subTitle="Organiza tus procesos, centraliza tu información y gestiona tu empresa de forma sencilla y eficiente."
            />

            {/* Funcionalidades */}
            <section className="px-6 pb-20 lg:px-10">
                <div className="mx-auto max-w-6xl">

                    <div className="grid grid-cols-1 gap-5 md:grid-cols-3">

                        {features.map((feature) => {
                            const Icon = feature.icon;

                            return (
                                <div
                                    key={feature.title}
                                    className="
                                        group rounded-xl border border-border
                                        bg-card p-7 shadow-sm
                                        transition-all duration-300
                                        hover:-translate-y-1 hover:shadow-md
                                    "
                                >
                                    {/* Icono */}
                                    <div className="
                                        mb-5 flex size-12 items-center
                                        justify-center rounded-xl
                                        bg-secondary text-primary
                                        transition-transform duration-300
                                        group-hover:scale-105
                                    ">
                                        <Icon className="size-6" />
                                    </div>

                                    {/* Título */}
                                    <h3 className="mb-2 text-lg font-semibold text-foreground">
                                        {feature.title}
                                    </h3>

                                    {/* Descripción */}
                                    <p className="text-sm leading-6 text-muted-foreground">
                                        {feature.description}
                                    </p>

                                </div>
                            );
                        })}

                    </div>
                </div>
            </section>
        </main>
    );
};'''
    
            # Crear el archivo
            HelperFile.write(
                folder_path=folder_path,
                file_name="HomePage.tsx",
                content=content
            )

  
            