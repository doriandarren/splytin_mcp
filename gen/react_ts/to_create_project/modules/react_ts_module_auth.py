import os
from gen.helpers.helper_file import HelperFile


class ReactTsModuleAuth:


    def invoke(self, full_path):
        self.create_file_auth_layout_tsx(full_path)
        self.create_file_login_page_tsx(full_path)
        self.create_file_register_page_tsx(full_path)



    def create_file_auth_layout_tsx(self, full_path):
        """
        Genera el archivo.
        """

        folder_path = os.path.join(full_path, "src", "modules", "auth", "layouts")

        content = r'''import { Outlet } from "react-router";

const AuthLayout = () => {
  return (
    <>
      <Outlet />
    </>
  );
};

export default AuthLayout;
'''

        # Crear el archivo
        HelperFile.write(
            folder_path=folder_path,
            file_name="AuthLayout.tsx",
            content=content
        )
        
        
        
    def create_file_login_page_tsx(self, full_path):
        """
        Genera el archivo.
        """
    
        folder_path = os.path.join(full_path, "src", "modules", "auth", "login", "pages")
    
        content = r'''export const LoginPage = () => {
  return (
    <div>LoginPage</div>
  )
}
'''
    
        # Crear el archivo
        HelperFile.write(
            folder_path=folder_path,
            file_name="LoginPage.tsx",
            content=content
        )
    
    
    
    def create_file_register_page_tsx(self, full_path):
        """
        Genera el archivo.
        """
    
        folder_path = os.path.join(full_path, "src", "modules", "auth", "register", "pages")
    
        content = r'''export const RegisterPage = () => {
  return (
    <div>RegisterPage</div>
  )
}
'''
    
        # Crear el archivo
        HelperFile.write(
            folder_path=folder_path,
            file_name="RegisterPage.tsx",
            content=content
        )
    