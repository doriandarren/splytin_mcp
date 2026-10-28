import os
from gen.helpers.helper_file import HelperFile
from gen.helpers.helper_json import HelperJson
from gen.helpers.helper_print import print_green, run_command



class ReactTsChadcn:
    
    
    def invoke(self, full_path):
        self.install_tailwind(full_path)
        self.install_types(full_path)
        
        self.update_index_css(full_path)
        self.update_file_ts_config_json(full_path)
        self.update_file_ts_config_app_json(full_path)
        self.update_file_vite_config_ts(full_path)
    
        # Chadcn
        self.install_chadcn_init(full_path)
        self.install_chadcn_component_all(full_path)
        
        
    
    
    def install_tailwind(self, full_path):
        # Instalar dependencias
        run_command(
            "npm install tailwindcss @tailwindcss/vite",
            cwd=full_path
        )
        print_green("tailwindcss creado correctamente.")
        
        
    
    
    def install_types(self, full_path):
        # Instalar dependencias
        run_command(
            "npm install -D @types/node",
            cwd=full_path
        )
        print_green("@types/node creado correctamente.")
        
        
    
    def update_index_css(self, full_path):
        """
        Genera el archivo.
        """

        folder_path = os.path.join(full_path, "src")

        content = r'''/* index.css */
@import "tailwindcss";
'''

        # Crear el archivo
        HelperFile.write(
            folder_path=folder_path,
            file_name="index.css",
            content=content
        )    
    
    
    
        
    def update_file_ts_config_json(self, full_path):
        """Actualiza tsconfig.json."""

        file_path = os.path.join(full_path, "tsconfig.json")

        HelperJson.update(
            file_path=file_path,
            new_data={
                "compilerOptions": {
                    "paths": {
                        "@/*": ["./src/*"]
                    }
                }
            }
        )

        print_green("tsconfig.json actualizado correctamente.")
        
    
        
    def update_file_ts_config_app_json(self, full_path):
        """
        Configura los alias de TypeScript en tsconfig.app.json.
        """

        file_path = os.path.join(full_path, "tsconfig.app.json")

        HelperJson.update(
            file_path=file_path,
            new_data={
                "compilerOptions": {
                    "paths": {
                        "@/*": ["./src/*"]
                    }
                }
            }
        )

        print_green("tsconfig.app.json actualizado correctamente.")

    
    
    
    
    def update_file_vite_config_ts(self, full_path):
        """Configura Tailwind CSS y el alias @ en Vite."""

        folder_path = os.path.join(full_path)
    
        content = r'''import react, { reactCompilerPreset } from '@vitejs/plugin-react'
import babel from '@rolldown/plugin-babel'
import tailwindcss from '@tailwindcss/vite'
import path from 'node:path'
import { defineConfig } from 'vite'

export default defineConfig({
  plugins: [
    react(),
    babel({ presets: [reactCompilerPreset()] }),
    tailwindcss(),
  ],

  resolve: {
    alias: {
      '@': path.resolve(import.meta.dirname, './src'),
    },
  },
})
'''
    
        # Crear el archivo
        HelperFile.write(
            folder_path=folder_path,
            file_name="vite.config.ts",
            content=content
        )

    
    
    
    def install_chadcn_init(self, full_path):
        # Instalar dependencias
        run_command(
            "npx --yes shadcn@latest init --base base --preset nova --yes",
            cwd=full_path
        )
        print_green("tailwindcss creado correctamente.")


    def install_chadcn_component_all(self, full_path):
        # Instalar dependencias
        run_command(
            "npx --yes shadcn@latest add --all --yes",
            cwd=full_path
        )
        print_green("tailwindcss creado correctamente.")

