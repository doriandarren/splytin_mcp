import os
from gen.helpers.helper_file import HelperFile
from gen.helpers.helper_print import print_cyan, print_green, print_red


class ReactTsCrudRoute:

    def invoke(
        self,
        full_path,
        namespace,
        version_api,
        folder_group,
        project_name,
        singular_name,
        plural_name,
        singular_name_camel,
        plural_name_camel,
        singular_name_kebab,
        plural_name_kebab,
        singular_name_snake,
        plural_name_snake,
        columns
    ):
        """
        Genera el archivo.
        """
        
        self.update_app_router_tsx(
            full_path,
            namespace,
            version_api,
            folder_group,
            project_name,
            singular_name,
            plural_name,
            singular_name_camel,
            plural_name_camel,
            singular_name_kebab,
            plural_name_kebab,
            singular_name_snake,
            plural_name_snake,
            columns
        )
        
        
        
        

    def update_app_router_tsx(
        self,
        full_path,
        namespace,
        version_api,
        folder_group,
        project_name,
        singular_name,
        plural_name,
        singular_name_camel,
        plural_name_camel,
        singular_name_kebab,
        plural_name_kebab,
        singular_name_snake,
        plural_name_snake,
        columns
    ):
        """
        Actualiza app.router.tsx agregando:
        - Import del componente CRUD.
        - Ruta dentro de children de /admin.
        - Evita duplicados.
        """

        folder_path = os.path.join(full_path, "src")
        file_name = "app.router.tsx"
        file_path = os.path.join(folder_path, file_name)

        if not os.path.isfile(file_path):
            print_cyan(f"Error: {file_path} no existe.")
            return False

        try:
            # Leer archivo actual
            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read()

            # Configuración
            component_name = f"{singular_name}Page"
            route_path = plural_name_kebab

            import_marker = "// CRUD IMPORTS"
            route_marker = "// CRUD ROUTES"

            # Import del componente
            import_line = (
                f'import {{ {component_name} }} from '
                f'"@/modules/private/{route_path}/pages/{component_name}";'
            )

            # Bloque de la ruta
            route_block = (
                "{\n"
                f'            path: "{route_path}",\n'
                f"            element: <{component_name} />,\n"
                "          },\n"
            )

            # Verificar marcadores antes de modificar
            if import_marker not in content:
                print_red(f"No se encontró: {import_marker}")
                return False

            if route_marker not in content:
                print_red(f"No se encontró: {route_marker}")
                return False

            # 1. Agregar import si no existe
            if import_line not in content:
                result = HelperFile.replace(
                    folder_path=folder_path,
                    file_name=file_name,
                    old_content=import_marker,
                    new_content=f"{import_line}\n{import_marker}"
                )

                if not result:
                    return False

            # 2. Agregar ruta si no existe
            if route_block.strip() not in content:
                result = HelperFile.replace(
                    folder_path=folder_path,
                    file_name=file_name,
                    old_content=route_marker,
                    new_content=f"{route_block}        {route_marker}"
                )

                if not result:
                    return False

            print_green(
                f"CRUD '{singular_name}' registrado correctamente en {file_name}."
            )

            return True

        except OSError as error:
            print_red(f"Error al actualizar {file_path}: {error}")
            return False

    

    