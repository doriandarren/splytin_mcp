import os

from helpers.helper_print import print_message, GREEN, CYAN


class HelperLaravelRoute:

    @staticmethod
    def get_folder_path(
        full_path: str,
        namespace: str,
        version_api: str
    ) -> str:
        return os.path.join(
            full_path,
            "routes",
            namespace,
            version_api
        )

    @staticmethod
    def get_controller_imports(
        namespace: str,
        version_api: str,
        folder_group: str | None,
        plural_name: str,
        singular_name: str
    ) -> str:

        parts = [
            "App",
            "Http",
            "Controllers",
            namespace,
            version_api
        ]

        if folder_group:
            parts.append(folder_group)

        parts.append(plural_name)

        controller_path = "\\".join(parts)

        content = f"""use {controller_path}\\{singular_name}IndexController;
use {controller_path}\\{singular_name}ShowController;
use {controller_path}\\{singular_name}StoreController;
use {controller_path}\\{singular_name}UpdateController;
use {controller_path}\\{singular_name}DestroyController;"""

        return content

    @staticmethod
    def update_route_api_php(
        full_path: str,
        namespace: str,
        version_api: str,
        plural_name_snake: str
    ) -> None:
        """
        Actualiza routes/api.php para incluir
        el archivo de rutas del CRUD.
        """

        main_path = os.path.join(
            full_path,
            "routes",
            "api.php"
        )

        # Verificar si el archivo existe
        if not os.path.exists(main_path):
            print_message(
                f"Error: {main_path} no existe.",
                CYAN
            )
            return

        try:
            # Leer el contenido del archivo
            with open(main_path, "r", encoding="utf-8") as f:
                content = f.read()

            marker = "    // ..."

            string_replace = (
                f"require base_path("
                f"'routes/{namespace}/{version_api}/{plural_name_snake}.php'"
                f");"
            )

            if marker not in content:
                print_message(
                    f"No se encontró el marcador en {main_path}",
                    CYAN
                )
                print(repr(marker))
                return

            if string_replace not in content:
                replacement = f"""    // ...
    {string_replace}"""

                content = content.replace(
                    marker,
                    replacement
                )

            # Escribir el contenido actualizado
            with open(main_path, "w", encoding="utf-8") as f:
                f.write(content)

            print_message(
                f"{main_path} actualizado correctamente.",
                GREEN
            )

        except Exception as e:
            print_message(
                f"Error al actualizar {main_path}: {e}",
                CYAN
            )
