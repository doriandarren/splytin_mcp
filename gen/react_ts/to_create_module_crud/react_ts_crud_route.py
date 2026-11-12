import os 
from gen.helpers.helper_print import dd, print_green, print_red
from gen.react_ts.helpers.helper_react_ts_router import HelperReactTsRouter
from gen.helpers.helper_file import HelperFile



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
        ## Create file Routes
        self.create_routes(
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
        
        ## Update Route main
        self.update_app_route_tsx(
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
        
        


    def create_routes(
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

        folder_path = os.path.join(full_path, "src", "modules", namespace, plural_name_snake, "routes")

        content = f'''// src/modules/{namespace}/{plural_name_snake}/routes/{plural_name_camel}.routes.tsx
import type {{ RouteObject }} from "react-router";

import {{ {singular_name}Page }} from "../pages/{singular_name}Page";
import {{ {singular_name}CreatePage }} from "../pages/{singular_name}CreatePage";
import {{ {singular_name}UpdatePage }} from "../pages/{singular_name}UpdatePage";

export const {singular_name_camel}Routes: RouteObject[] = [
    {{
        path: "{plural_name_kebab}",
        element: <{singular_name}Page />,
    }},
    {{
        path: "{plural_name_kebab}/create",
        element: <{singular_name}CreatePage />,
    }},
    {{
        path: "{plural_name_kebab}/:id/edit",
        element: <{singular_name}UpdatePage />,
    }},
];
'''

        # Crear el archivo
        HelperFile.write(
            folder_path=folder_path,
            file_name=f"{plural_name_camel}.routes.tsx",
            content=content
        )

    
    def update_app_route_tsx(
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
        Actualiza el archivo
        """
        main_path = os.path.join(full_path, "src", "app.router.tsx")

        # Verificar si el archivo existe
        if not os.path.exists(main_path):
            print_red(f"Error: {main_path} no existe.")
            dd(f"Error: {main_path} no existe.")
            return False

        try:
            # Leer el contenido del archivo
            with open(main_path, "r", encoding="utf-8") as f:
                content = f.read()

            # Imports y rutas
            import_line = (
                f'import {{ {singular_name_camel}Routes }} from '
                f'"./modules/{namespace}/{plural_name_snake}/routes/{plural_name_camel}.routes";'
            )

            route_line = f"...{singular_name_camel}Routes,"

            # Evitar duplicados
            if import_line in content and route_line in content:
                print_green(
                    f"CRUD '{singular_name}' ya está registrado."
                )
                return True

            # Reemplazos
            replacements = {}

            if import_line not in content:
                replacements["// CRUD IMPORTS"] = f"""{import_line}
// CRUD IMPORTS"""

            if route_line not in content:
                replacements["// CRUD ROUTES"] = f"""        {route_line}
// CRUD ROUTES"""

                # Validar y aplicar los reemplazos
            new_content = content

            for old_text, new_text in replacements.items():
                if old_text not in new_content:
                    raise ValueError(
                        f"No se encontró el texto esperado: {old_text}"
                    )

                new_content = new_content.replace(
                    old_text,
                    new_text,
                    1
                )

            if new_content == content:
                raise ValueError("No se realizó ningún reemplazo.")

            # Escribir el contenido actualizado
            with open(main_path, "w", encoding="utf-8") as f:
                f.write(new_content)

            print_green(f"{main_path} actualizado correctamente.")
            return True

        except Exception as e:
            print_red(f"Error al actualizar {main_path}: {e}")