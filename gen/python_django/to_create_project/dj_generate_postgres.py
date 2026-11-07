import os
from gen.helpers.helper_print import print_message, GREEN, CYAN, run_command
from gen.python_django.helpers.helper_file import helper_add_import, helper_append_content, helper_replace_block



class DjGeneratePostgre:
    
    def invoke(self, full_path, project_name_format, app_main, venv_python):
        """
        Genera el archivo
        """
        self.install_dependencies(full_path, venv_python)
        self.generate_docker_file(full_path, project_name_format)
        


    def install_dependencies(self,full_path, venv_python):
        print_message("Instalando dependencias en el venv...", CYAN)
        run_command(f'"{venv_python}" -m pip install "psycopg[binary]"', cwd=full_path)
        print_message("Dependencias instaladas correctamente.", GREEN)
        
        
        

    def generate_docker_file(self,full_path, project_name_format):
        """
        Genera el archivo
        """

        folder_path = os.path.join(full_path, "docker")
        file_path = os.path.join(folder_path, "docker-compose.yml")

        os.makedirs(folder_path, exist_ok=True)

        content = f'''## docker compose down    --> Eliminar los contenedores
## docker compose up -d   --> Levantar los contenedores
name: {project_name_format}_posgrest
services:
postgres:
    image: postgres:16
    container_name: {project_name_format}_postgres
    restart: on-failure
    environment:
    POSTGRES_DB: {project_name_format}_db
    POSTGRES_USER: {project_name_format}_user
    POSTGRES_PASSWORD: {project_name_format}_pass
    ports:
    - "5432:5432"
    volumes:
    - pgdata:/var/lib/postgresql/data

volumes:
pgdata:
    '''

        try:
            with open(file_path, "w") as f:
                f.write(content)
            print_message(f"Archivo generado: {file_path}", GREEN)
        except Exception as e:
            print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)

