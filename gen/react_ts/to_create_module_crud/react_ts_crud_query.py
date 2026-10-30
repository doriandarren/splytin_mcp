import os
from gen.helpers.helper_file import HelperFile


class ReactTsCrudQuery:

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
        columns,
    ):
        """
        Genera el archivo.
        """

        folder_path = os.path.join(full_path, "src", "modules", namespace, plural_name_snake, "queries")
        
        content = f'''// src/modules/{namespace}/{plural_name_snake}/queries/{singular_name_snake}Queries.ts

import {{ queryOptions }} from "@tanstack/react-query";

import {{ get{plural_name} }} from "../services/{plural_name_camel}Service";

/**
 * Claves de caché
 */
export const {plural_name_camel}Keys = {{
  all: ["{plural_name_camel}"] as const,

  lists: () => [...{plural_name_camel}Keys.all, "list"] as const,

  list: (page: number) =>
    [...{plural_name_camel}Keys.lists(), page] as const,
}};

/**
 * Configuración de consulta paginada.
 */
export const {plural_name_camel}Query = (page: number) =>
  queryOptions({{
    queryKey: {plural_name_camel}Keys.list(page),

    queryFn: ({{ signal }}) => get{plural_name}(page, signal),

    staleTime: 60 * 1000,
}});
'''

        # Crear el archivo
        HelperFile.write(
            folder_path=folder_path,
            file_name=f"{plural_name_camel}Queries.ts",
            content=content
        )