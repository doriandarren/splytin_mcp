import os
from gen.helpers.helper_file import HelperFile
from gen.helpers.helper_print import print_red


class HelperReactTsRouter:

    @staticmethod
    def validate(full_path):
        """
        Valida que app.router.tsx exista
        y contenga los marcadores necesarios.
        """

        file_path = os.path.join(
            full_path,
            "src",
            "app.router.tsx"
        )

        if not os.path.isfile(file_path):
            print_red(f"El archivo no existe: {file_path}")
            return False

        try:
            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read()

            if "// CRUD IMPORTS" not in content:
                print_red("No se encontró: // CRUD IMPORTS")
                return False

            if "// CRUD ROUTES" not in content:
                print_red("No se encontró: // CRUD ROUTES")
                return False

            return True

        except OSError as error:
            print_red(f"Error al leer {file_path}: {error}")
            return False

    @staticmethod
    def add_import(
        full_path,
        namespace,
        plural_name_snake,
        component_name
    ):
        """
        Agrega el import de un componente
        evitando duplicados.
        """

        file_path = os.path.join(
            full_path,
            "src",
            "app.router.tsx"
        )

        try:
            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read()

            import_line = (
                f'import {{ {component_name} }} from '
                f'"@/modules/{namespace}/{plural_name_snake}/pages/{component_name}";'
            )

            if import_line in content:
                return True

            return HelperFile.replace(
                folder_path=os.path.join(full_path, "src"),
                file_name="app.router.tsx",
                old_content="// CRUD IMPORTS",
                new_content=f'''{import_line}
// CRUD IMPORTS'''
            )

        except OSError as error:
            print_red(f"Error al agregar import: {error}")
            return False

    @staticmethod
    def add_route(
        full_path,
        route_path,
        component_name
    ):
        """
        Agrega una ruta a los children de /admin
        evitando duplicados.
        """

        file_path = os.path.join(
            full_path,
            "src",
            "app.router.tsx"
        )

        try:
            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read()

            if f'path: "{route_path}",' in content:
                return True

            return HelperFile.replace(
                folder_path=os.path.join(full_path, "src"),
                file_name="app.router.tsx",
                old_content="// CRUD ROUTES",
                new_content=f'''{{
            path: "{route_path}",
            element: <{component_name} />,
          }},
          // CRUD ROUTES'''
            )

        except OSError as error:
            print_red(f"Error al agregar ruta: {error}")
            return False
