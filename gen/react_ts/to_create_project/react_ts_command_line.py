import os
from gen.helpers.helper_file import HelperFile
from gen.helpers.helper_print import print_cyan, print_green, print_red, run_command


class ReactTsCommandLine():
    
    def invoke(self, full_path):
        self.create_project(full_path)
        self.create_app_tsx(full_path)
        self.create_index_css(full_path)
        self.update_file_main_tsx(full_path)
        
        
    def create_project(self, full_path):
        """Crea el proyecto React + TypeScript con Vite."""

        project_dir = os.path.dirname(full_path)
        project_name = os.path.basename(full_path)

        if not os.path.exists(project_dir):
            os.makedirs(project_dir)
            print_green(f"Directorio base {project_dir} creado.")

        print_green("Creando el proyecto React + TypeScript con Vite...")

        run_command(
            f"npx --yes create-vite@latest {project_name} "
            f"--template react-compiler-ts "
            f"--no-interactive "
            f"--no-immediate",
            cwd=project_dir
        )
        
        # Comprobar que se creó el proyecto
        if not os.path.isfile(os.path.join(full_path, "package.json")):
            raise RuntimeError("No se pudo crear el proyecto React.")

        # Instalar dependencias
        run_command(
            "npm install",
            cwd=full_path
        )


        print_green("Proyecto creado correctamente.")
    
        
    def create_app_tsx(self, full_path):
        """
        Genera el archivo.
        """
        
        # Delete first:
        folder_path = os.path.join(full_path, "src")
        
        # Delete
        HelperFile.delete(
            folder_path=folder_path,
            file_name="App.css"
        )
        
        # Delete
        HelperFile.delete(
            folder_path=folder_path,
            file_name="App.tsx"
        )
        

        content = r'''import { RouterProvider } from "react-router"
import { appRouter } from "./app.router"

export const App = () => {
  return <RouterProvider router={appRouter} />
}
'''

        # Crear el archivo
        HelperFile.write(
            folder_path=folder_path,
            file_name="App.tsx",
            content=content
        )
    
    
    
    
    def update_file_main_tsx(self, full_path):
        """
        Actualiza el archivo
        """
        main_path = os.path.join(full_path, "src", "main.tsx")
    
        # Verificar si el archivo existe
        if not os.path.exists(main_path):
            print_cyan(f"Error: {main_path} no existe.")
            return False
    
        try:
            # Leer el contenido del archivo
            with open(main_path, "r", encoding="utf-8") as f:
                content = f.read()
    
            # Reemplazos
            replacements = {
                ## New Item -> KEY : VALUE
                """import App from './App.tsx'""":
                """import { App } from './App';""",
            }
    
            # Validar y aplicar los reemplazos
            new_content = content
    
            for old_text, new_text in replacements.items():
                if old_text not in new_content:
                    raise ValueError(f"No se encontró el texto esperado: {old_text}")
    
                new_content = new_content.replace(old_text, new_text, 1)
    
            if new_content == content:
                raise ValueError("No se realizó ningún reemplazo.")
    
            # Escribir el contenido actualizado
            with open(main_path, "w", encoding="utf-8") as f:
                f.write(new_content)
    
            print_green(f"{main_path} actualizado correctamente.",)
    
            return True
    
        except Exception as e:
            print_red(f"Error al actualizar {main_path}: {e}")
            return False
    
        
    
   
    
         
         
    def create_index_css(self, full_path):
        """
        Genera el archivo.
        """

        folder_path = os.path.join(full_path, "src")

        content = r'''/* index.css */'''

        # Crear el archivo
        HelperFile.write(
            folder_path=folder_path,
            file_name="index.css",
            content=content
        )
                