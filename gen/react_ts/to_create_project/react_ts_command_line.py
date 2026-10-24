import os
from gen.helpers.helper_file import HelperFile
from gen.helpers.helper_print import print_green, run_command


class ReactTsCommandLine:
    
    def invoke(self, full_path):
        self.create_project(full_path)    
        
        
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
            f"--template react-ts "
            f"--eslint "
            f"--no-interactive "
            f"--no-immediate",
            cwd=project_dir
        )

        print_green("Proyecto creado correctamente.")
        
        
    
        
    def ccc(self, full_path):
            """
            Genera el archivo.
            """
    
            folder_path = os.path.join(full_path, "core")
    
            content = r'''# '''
    
            # Crear el archivo
            HelperFile.write(
                folder_path=folder_path,
                file_name="X.py",
                content=content
            )
            