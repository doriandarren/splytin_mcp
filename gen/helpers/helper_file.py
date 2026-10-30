import os
from gen.helpers.helper_print import print_message, GREEN, CYAN


class HelperFile:
    
    @staticmethod
    def write(folder_path, file_name, content):
        """
        Genera el archivo
        """

         # Crear el directorio si no existe
        os.makedirs(folder_path, exist_ok=True)

        # Construir la ruta completa del archivo
        file_path = os.path.join(folder_path, file_name)

        try:
            # Escribir el contenido del archivo
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(content)

            print_message(f"Archivo generado: {file_path}", GREEN)

            return file_path

        except OSError as error:
            print_message(f"Error al generar el archivo {file_path}: {error}", CYAN)
            return None
        
        
    
    @staticmethod
    def create_init_file(folder_path):
        """
        Crea __init__.py si no existe.
        """

        os.makedirs(folder_path, exist_ok=True)

        file_path = os.path.join(folder_path, "__init__.py")

        if not os.path.exists(file_path):
            return HelperFile.write(
                folder_path=folder_path,
                file_name="__init__.py",
                content=""
            )

        return file_path
    
    
    @staticmethod
    def delete(folder_path, file_name):
        """
        Elimina un archivo si existe.
        """

        file_path = os.path.join(folder_path, file_name)

        try:
            if not os.path.isfile(file_path):
                print_message(f"El archivo no existe: {file_path}", CYAN)
                return False

            os.remove(file_path)

            print_message(f"Archivo eliminado: {file_path}", GREEN)
            return True

        except OSError as error:
            print_message(f"Error al eliminar el archivo {file_path}: {error}", CYAN)
            return False




    @staticmethod
    def append(folder_path, file_name, content):
        """
        Agrega contenido al final de un archivo existente.
        """

        file_path = os.path.join(folder_path, file_name)

        try:
            if not os.path.isfile(file_path):
                print_message(f"El archivo no existe: {file_path}", CYAN)
                return False

            # Agregar contenido al final del archivo
            with open(file_path, "a", encoding="utf-8") as file:
                file.write(content)

            print_message(f"Contenido agregado: {file_path}", GREEN)
            return True

        except OSError as error:
            print_message(f"Error al modificar el archivo {file_path}: {error}", CYAN)
            return False



    @staticmethod
    def replace(folder_path, file_name, old_content, new_content):
        """
        Busca un texto dentro de un archivo y lo reemplaza.

        Retorna True si se reemplazó correctamente.
        Retorna False si ocurre un error.
        """

        file_path = os.path.join(folder_path, file_name)

        try:
            if not os.path.isfile(file_path):
                print_message(f"El archivo no existe: {file_path}", CYAN)
                return False

            # Leer el archivo
            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read()

            # Comprobar si existe el texto
            if old_content not in content:
                print_message(
                    f"No se encontró el texto en: {file_path}",
                    CYAN
                )
                return False

            # Reemplazar solamente la primera coincidencia
            new_file_content = content.replace(
                old_content,
                new_content,
                1
            )

            # Guardar el archivo actualizado
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(new_file_content)

            print_message(f"Archivo actualizado: {file_path}", GREEN)
            return True

        except OSError as error:
            print_message(
                f"Error al modificar el archivo {file_path}: {error}",
                CYAN
            )
            return False
