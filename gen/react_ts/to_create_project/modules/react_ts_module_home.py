import os
from gen.helpers.helper_file import HelperFile


class ReactTsModuleHome:
    
    def invoke(self, full_path):
        self.create_file_public_layout_tsx(full_path)
        self.create_file_home_page_tsx(full_path)
    
    

    def create_file_public_layout_tsx(self, full_path):
        """
        Genera el archivo.
        """

        folder_path = os.path.join(full_path, "src", "modules", "public", "layouts")

        content = r'''import { Outlet } from "react-router"

export const PublicLayout = () => {
  return <div>
    PublicLayout
    <Outlet />
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
    
            content = r'''import { Button } from "@/components/ui/button"

export const HomePage = () => {
  return <div>
    HomePage
    <Button>Button</Button>
  </div>
}
'''
    
            # Crear el archivo
            HelperFile.write(
                folder_path=folder_path,
                file_name="HomePage.tsx",
                content=content
            )