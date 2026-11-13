import os
from helpers.helper_file import HelperFile


class ReactTsComponentPublic:

    def invoke(self, full_path):
        # Components
        self.create_file_custom_header_tsx(full_path)
        self.create_file_custom_footer_tsx(full_path)
        self.create_file_custom_jumbotron_tsx(full_path)
        



    def create_file_custom_header_tsx(self, full_path):
        """
        Genera el archivo.
        """

        folder_path = os.path.join(full_path, "src", "modules", "public", "components")

        content = r'''// src/modules/public/components/CustomHeader.tsx
import { Link } from "react-router";
import { ArrowRight, PanelsTopLeft } from "lucide-react";

import { Button } from "@/components/ui/button";

const CustomHeader = () => {
    return (
        <header className="sticky top-0 z-50 w-full border-b border-border bg-background/95 backdrop-blur-md">
            <div className="mx-auto flex h-18 w-full max-w-7xl items-center justify-between px-6 lg:px-10">

                {/* Logo y nombre */}
                <Link
                    to="/"
                    className="flex items-center gap-3 text-foreground"
                >
                    <div className="flex size-9 items-center justify-center rounded-lg bg-primary text-primary-foreground">
                        <PanelsTopLeft className="size-5" />
                    </div>

                    <span className="text-lg font-semibold tracking-tight">
                        Splytin ERP
                    </span>
                </Link>

                {/* Acceso */}
                <Button
                    nativeButton={false}
                    render={<Link to="/auth/login" />}
                    className="gap-2"
                >
                    Iniciar sesión
                    <ArrowRight className="size-4" />
                </Button>

            </div>
        </header>
    );
};

export default CustomHeader;'''

        # Crear el archivo
        HelperFile.write(
            folder_path=folder_path,
            file_name="CustomHeader.tsx",
            content=content
        )  


    
    def create_file_custom_footer_tsx(self, full_path):
            """
            Genera el archivo.
            """
    
            folder_path = os.path.join(full_path, "src", "modules", "public", "components")
    
            content = r'''// src/modules/public/components/CustomFooter.tsx
import { PanelsTopLeft } from "lucide-react";

export const CustomFooter = () => {
    return (
        <footer className="border-t border-border bg-background">
            <div className="mx-auto max-w-7xl px-6 py-8 lg:px-10">

                <div className="flex flex-col items-center justify-between gap-4 md:flex-row">

                    {/* Marca */}
                    <div className="flex items-center gap-3">
                        <PanelsTopLeft className="size-5 text-primary" />

                        <div>
                            <h3 className="text-sm font-semibold text-foreground">
                                Splytin ERP
                            </h3>

                            <p className="text-xs text-muted-foreground">
                                Gestión empresarial inteligente
                            </p>
                        </div>
                    </div>

                    {/* Copyright */}
                    <p className="text-center text-xs text-muted-foreground">
                        © {new Date().getFullYear()} Splytin ERP.
                        Todos los derechos reservados.
                    </p>

                </div>
            </div>
        </footer>
    );
};'''
    
            # Crear el archivo
            HelperFile.write(
                folder_path=folder_path,
                file_name="CustomFooter.tsx",
                content=content
            )  
            
    
    
    def create_file_custom_jumbotron_tsx(self, full_path):
            """
            Genera el archivo.
            """
    
            folder_path = os.path.join(full_path, "src", "modules", "public", "components")
    
            content = r'''// src/modules/public/components/CustomJumbotron.tsx
import { Link } from "react-router";
import { ArrowRight } from "lucide-react";

import { Button } from "@/components/ui/button";

interface Props {
    title?: string;
    subTitle?: string;
}

export const CustomJumbotron = ({
    title = "Todo tu negocio. Un solo lugar.",
    subTitle = "Organiza tus procesos, centraliza tu información y gestiona tu empresa de forma sencilla y eficiente.",
}: Props) => {
    return (
        <section className="relative overflow-hidden bg-background px-6 py-20 md:py-28 lg:px-10">

            {/* Fondo decorativo suave */}
            <div
                aria-hidden="true"
                className="pointer-events-none absolute inset-0 bg-linear-to-b from-secondary/60 via-background to-background"
            />

            <div className="relative mx-auto flex max-w-4xl flex-col items-center text-center">

                {/* Etiqueta superior */}
                <span className="mb-7 rounded-full border border-primary/15 bg-secondary px-4 py-2 text-xs font-semibold tracking-widest text-secondary-foreground">
                    GESTIÓN EMPRESARIAL INTELIGENTE
                </span>

                {/* Título */}
                <h1 className="max-w-3xl text-4xl font-semibold tracking-tight text-foreground sm:text-5xl lg:text-6xl">
                    {title}
                </h1>

                {/* Subtítulo */}
                <p className="mt-7 max-w-2xl text-base leading-8 text-muted-foreground md:text-lg">
                    {subTitle}
                </p>

                {/* Botón principal */}
                <div className="mt-9">
                    <Button
                        nativeButton={false}
                        render={<Link to="/auth/login" />}
                        size="lg"
                        className="gap-2 px-7"
                    >
                        Acceder a Splytin ERP
                        <ArrowRight className="size-4" />
                    </Button>
                </div>

            </div>
        </section>
    );
};
'''
    
            # Crear el archivo
            HelperFile.write(
                folder_path=folder_path,
                file_name="CustomJumbotron.tsx",
                content=content
            )  
    