import os
from gen.helpers.helper_file import HelperFile


class ReactTsCrudSystemService:

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

        folder_path = os.path.join(full_path, "src", "modules", namespace, plural_name_snake, "services")

        content = f'''// src/modules/{namespace}/{plural_name_snake}/services/{singular_name_snake}Service.ts

import {{ api }} from "@/api/api";
import {{ ApiError }} from "@/api/api-error";

import type {{ {plural_name}Response }} from "../types/{singular_name_snake}.types";

/**
 * Obtiene el listado paginado.
 *
 * GET /api/v1/{plural_name_snake}?page=1
 */
export async function get{plural_name}(
  page: number = 1,
  signal?: AbortSignal
): Promise<{plural_name}Response> {{
  const response = await api<{plural_name}Response>(
    `{plural_name_snake}?page=${{page}}`,
    {{
      method: "GET",
      signal,
    }}
  );

  if (
    !response ||
    !Array.isArray(response.data) ||
    !response.meta ||
    typeof response.meta.total !== "number"
  ) {{
    throw new ApiError(
      "La API no devolvió un listado de sistemas válido.",
      {{
        kind: "invalid-response",
      }}
    );
  }}

  return response;
}}
'''

        # Crear el archivo
        HelperFile.write(
            folder_path=folder_path,
            file_name=f"{plural_name_camel}Service.ts",
            content=content
        )