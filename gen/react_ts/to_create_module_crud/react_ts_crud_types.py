import os
from gen.helpers.helper_file import HelperFile


class ReactTsCrudTypes:

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

        folder_path = os.path.join(full_path, "src", "modules", namespace, plural_name_snake, "types")

        content = f'''// src/modules/{namespace}/{plural_name_snake}/types/{singular_name_snake}.types.ts

/**
 * Estados posibles de un sistema.
 */
export type {singular_name}Status =
  | "activo"
  | "inactivo"
  | "en mantenimiento";

/**
 * Atributos de un sistema.
 */
export interface {singular_name}Attributes {{
  name: string;
  status: {singular_name}Status;
  version: string;
  created_at: string;
  updated_at: string;
}}

/**
 * Recurso {singular_name} devuelto por Laravel.
 */
export interface {singular_name}Resource {{
  type: "{singular_name_snake}";
  id: number;
  attributes: {singular_name}Attributes;
  links: {{
    self: string;
  }};
}}

/**
 * Metadatos de paginación.
 */
export interface {singular_name}PaginationMeta {{
  current_page: number;
  per_page: number;
  last_page: number;
  total: number;
  from: number | null;
  to: number | null;
}}

/**
 * Enlaces de paginación.
 */
export interface {singular_name}PaginationLinks {{
  first: string;
  last: string;
  prev: string | null;
  next: string | null;
}}

/**
 * Respuesta del listado de sistemas.
 */
export interface {plural_name}Response {{
  data: {singular_name}Resource[];
  meta: {singular_name}PaginationMeta;
  links: {singular_name}PaginationLinks;
  message?: string;
  status_code?: number;
  success?: boolean;
}}

'''

        # Crear el archivo
        HelperFile.write(
            folder_path=folder_path,
            file_name=f"{singular_name_snake}.types.ts",
            content=content
        )