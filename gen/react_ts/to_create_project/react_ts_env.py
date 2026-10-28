import os
from gen.helpers.helper_file import HelperFile


class ReactTsEnv:

    def invoke(self, full_path):
        self.create_env(full_path)
        self.create_env_example(full_path)
        self.create_vite_env(full_path)
        
        
        
    def create_env(self, full_path):
        """
        Genera el archivo.
        """

        folder_path = os.path.join(full_path)

        content = r'''VITE_API_URL=http://api.splytin.test/api/v1/'''

        # Crear el archivo
        HelperFile.write(
            folder_path=folder_path,
            file_name=".env",
            content=content
        )
            
        
    def create_env_example(self, full_path):
        """
        Genera el archivo.
        """

        folder_path = os.path.join(full_path)

        content = r'''VITE_API_URL=http://api.splytin.test/api/v1/'''

        # Crear el archivo
        HelperFile.write(
            folder_path=folder_path,
            file_name=".env.example",
            content=content
        )
        
        
    def create_vite_env(self, full_path):
        """
        Genera el archivo.
        """

        folder_path = os.path.join(full_path)

        content = r'''/// <reference types="vite/client" />

interface ImportMetaEnv {
  readonly VITE_API_URL?: string;
}'''

        # Crear el archivo
        HelperFile.write(
            folder_path=folder_path,
            file_name="vite-env.d.ts",
            content=content
        )