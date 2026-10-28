import os
from gen.helpers.helper_file import HelperFile


class ReactTsModuleHome:
    
    def invoke(self, full_path):
        self.create_file_home_page_tsx(full_path)
        self.create_file_public_layout_tsx(full_path)
        

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
    
            folder_path = os.path.join(full_path, "src", "modules", "public", "home", "pages")
    
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

  
            