import os
from gen.helpers.helper_file import HelperFile


class ReactTsModuleHome:
    
    def invoke(self, full_path):
        self.create_file_home_page_tsx(full_path)
        self.create_file_public_layout_tsx(full_path)
        
        # Components
        self.create_file_custom_header_tsx(full_path)
        self.create_file_custom_footer_tsx(full_path)
        self.create_file_custom_jumbotron_tsx(full_path)
        
    
    

    def create_file_public_layout_tsx(self, full_path):
        """
        Genera el archivo.
        """

        folder_path = os.path.join(full_path, "src", "modules", "public", "layouts")

        content = r'''import { Outlet } from "react-router";
import CustomHeader from "../components/CustomHeader";
import { CustomFooter } from "../components/CustomFooter";

export const PublicLayout = () => {
  return <div className="min-h-screen bg-background">
    {/* Header */}
    <CustomHeader />

    {/* Content */}
    <Outlet />

    {/* Footer */}
    <CustomFooter />
  </div>
}
'''

        # Crear el archivo
        HelperFile.write(
            folder_path=folder_path,
            file_name="PublicLayout.tsx",
            content=content
        )
        
        
        
    
    def create_file_home_page_tsx(self, full_path):
            """
            Genera el archivo.
            """
    
            folder_path = os.path.join(full_path, "src", "modules", "public", "pages", "home")
    
            content = r'''import { CustomJumbotron } from "../../components/CustomJumbotron";

export const HomePage = () => {
  return (
    <>
      <CustomJumbotron title="Todos los productos" />
    </>
  );
}
'''
    
            # Crear el archivo
            HelperFile.write(
                folder_path=folder_path,
                file_name="HomePage.tsx",
                content=content
            )
            
          
          
    
    def create_file_custom_header_tsx(self, full_path):
        """
        Genera el archivo.
        """

        folder_path = os.path.join(full_path, "src", "modules", "public", "components")

        content = r'''import { useState } from "react";
import { Search, ShoppingBag, Menu } from "lucide-react";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";

const CustomHeader = () => {
  const [cartCount] = useState(3);
  return (
    <header className="sticky top-0 z-50 w-full border-b backdrop-blur bg-slate-50">
      <div className="container mx-auto px-4 lg:px-8">
        <div className="flex h-16 items-center justify-between">
          {/* Logo */}
          <div className="flex items-center space-x-4">
            <Button variant="ghost" size="icon" className="md:hidden">
              <Menu className="h-5 w-5" />
            </Button>
            <h1 className="text-xl font-semibold tracking-tight">
              TESLA STYLE
            </h1>
          </div>

          {/* Navigation - Desktop */}
          <nav className="hidden md:flex items-center space-x-8">
            <a
              href="#"
              className="text-sm font-medium transition-colors hover:text-primary"
            >
              Camisetas
            </a>
            <a
              href="#"
              className="text-sm font-medium transition-colors hover:text-primary"
            >
              Sudaderas
            </a>
            <a
              href="#"
              className="text-sm font-medium transition-colors hover:text-primary"
            >
              Chaquetas
            </a>
            <a
              href="#"
              className="text-sm font-medium transition-colors hover:text-primary"
            >
              Accesorios
            </a>
          </nav>

          {/* Search and Cart */}
          <div className="flex items-center space-x-4">
            <div className="hidden md:flex items-center space-x-2">
              <div className="relative">
                <Search className="absolute left-3 top-1/2 h-4 w-4 -translate-y-1/2 text-muted-foreground" />
                <Input
                  placeholder="Buscar productos..."
                  className="pl-9 w-64 h-9"
                />
              </div>
            </div>

            <Button variant="ghost" size="icon" className="md:hidden">
              <Search className="h-5 w-5" />
            </Button>

            <Button variant="ghost" size="icon" className="relative">
              <ShoppingBag className="h-5 w-5" />
              {cartCount > 0 && (
                <span className="absolute -top-1 -right-1 h-5 w-5 rounded-full bg-primary text-primary-foreground text-xs flex items-center justify-center">
                  {cartCount}
                </span>
              )}
            </Button>
          </div>
        </div>
      </div>
    </header>
  );
};
export default CustomHeader;

'''

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
    
            content = r'''export const CustomFooter = () => {
  return (
    <footer className="border-t py-12 px-4 lg:px-8 mt-16">
      <div className="container mx-auto">
        <div className="grid grid-cols-1 md:grid-cols-4 gap-8">
          <div>
            <h3 className="font-semibold mb-4">TESLA STYLE</h3>
            <p className="text-sm text-muted-foreground">
              Ropa inspirada en el diseño minimalista y la innovación de Tesla.
            </p>
          </div>

          <div>
            <h4 className="font-medium mb-4">Productos</h4>
            <ul className="space-y-2 text-sm text-muted-foreground">
              <li>
                <a href="#" className="hover:text-foreground">
                  Camisetas
                </a>
              </li>
              <li>
                <a href="#" className="hover:text-foreground">
                  Sudaderas
                </a>
              </li>
              <li>
                <a href="#" className="hover:text-foreground">
                  Chaquetas
                </a>
              </li>
              <li>
                <a href="#" className="hover:text-foreground">
                  Accesorios
                </a>
              </li>
            </ul>
          </div>

          <div>
            <h4 className="font-medium mb-4">Ayuda</h4>
            <ul className="space-y-2 text-sm text-muted-foreground">
              <li>
                <a href="#" className="hover:text-foreground">
                  Contacto
                </a>
              </li>
              <li>
                <a href="#" className="hover:text-foreground">
                  Envíos
                </a>
              </li>
              <li>
                <a href="#" className="hover:text-foreground">
                  Devoluciones
                </a>
              </li>
              <li>
                <a href="#" className="hover:text-foreground">
                  Guía de Tallas
                </a>
              </li>
            </ul>
          </div>

          <div>
            <h4 className="font-medium mb-4">Empresa</h4>
            <ul className="space-y-2 text-sm text-muted-foreground">
              <li>
                <a href="#" className="hover:text-foreground">
                  Sobre Nosotros
                </a>
              </li>
              <li>
                <a href="#" className="hover:text-foreground">
                  Sustentabilidad
                </a>
              </li>
              <li>
                <a href="#" className="hover:text-foreground">
                  Carreras
                </a>
              </li>
              <li>
                <a href="#" className="hover:text-foreground">
                  Prensa
                </a>
              </li>
            </ul>
          </div>
        </div>

        <div className="border-t mt-8 pt-8 text-center text-sm text-muted-foreground">
          <p>
            &copy; {new Date().getFullYear()} Teslo Style. Todos los derechos
            reservados.
          </p>
        </div>
      </div>
    </footer>
  );
};
'''
    
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
    
            content = r'''interface Props {
    title: string;
    subTitle?: string;
}

export const CustomJumbotron = ( {title, subTitle}: Props ) => {

  const defaultSubTitle = 'Ropa minimalista y elegante inspirada en el diseño futurista de Tesla. Calidad premium para un estilo atemporal.';

  return (
    <section className="py-16 px-4 lg:px-8 bg-muted/30">
      {/* Hero Section */}
      <div className="container mx-auto text-center">
        <h1 className="font-montserrat text-5xl lg:text-7xl font-light tracking-tight mb-6">
          {title}
        </h1>
        <p className="text-xl text-muted-foreground mb-8 max-w-2xl mx-auto">
          {subTitle || defaultSubTitle}
        </p>
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
    
    
            