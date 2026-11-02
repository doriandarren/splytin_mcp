import os
from gen.helpers.helper_file import HelperFile


class ReactTsCrudCreate:

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

        folder_path = os.path.join(
            full_path,
            "src",
            "modules",
            namespace,
            plural_name_snake,
            "hooks"
        )

        content = f'''// src/modules/{namespace}/{plural_name_snake}/hooks/use{plural_name}.ts
import {{ useMutation, useQueryClient }} from "@tanstack/react-query";

import {{ create{singular_name} }} from "../{plural_name_camel}/{plural_name_camel}Service";
import {{ {plural_name_camel}Keys }} from "../queries/{plural_name_camel}Queries";

export const useCreate{singular_name} = () => {{
  const queryClient = useQueryClient();

  return useMutation({{
    mutationFn: create{singular_name},

    onSuccess: async () => {{
      await queryClient.invalidateQueries({{
        queryKey: {plural_name_camel}Keys.lists(),
      }});
    }},
  }});
}};        
'''

        # Crear el archivo
        HelperFile.write(
            folder_path=folder_path,
            file_name=f"useCreate{singular_name}.ts",
            content=content
        )