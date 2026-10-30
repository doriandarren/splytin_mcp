import os
from gen.helpers.helper_file import HelperFile


class ReactTsCrudHook:

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

        folder_path = os.path.join(full_path, "src", "modules", namespace, plural_name_snake, "hooks")
                
        content = f'''// src/modules/{namespace}/{plural_name_snake}/hooks/use{plural_name}.ts
import {{ keepPreviousData, useQuery }} from "@tanstack/react-query";

import {{ {plural_name_camel}Query }} from "../queries/{plural_name_camel}Queries";

export const use{plural_name} = (page: number = 1) => {{
  return useQuery({{
    ...{plural_name_camel}Query(page),
    placeholderData: keepPreviousData,
  }});
}};
'''

        # Crear el archivo
        HelperFile.write(
            folder_path=folder_path,
            file_name=f"use{plural_name}.ts",
            content=content
        )