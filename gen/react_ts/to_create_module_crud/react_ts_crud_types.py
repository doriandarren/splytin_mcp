
import os
from gen.helpers.helper_file import HelperFile


class ReactTsCrudTypes:

    @staticmethod
    def get_ts_type(column):
        """
        Convierte los tipos de la base de datos
        a tipos TypeScript.
        """

        column_type = column.get("type", "string")

        type_mapping = {
            "string": "string",
            "text": "string",
            "char": "string",
            "uuid": "string",
            "enum": "string",
            "integer": "number",
            "int": "number",
            "bigint": "number",
            "smallint": "number",
            "decimal": "number",
            "float": "number",
            "double": "number",
            "boolean": "boolean",
            "date": "string",
            "datetime": "string",
            "timestamp": "string",
            "time": "string",
            "json": "Record<string, unknown>",
            "fk": "number",
        }

        ts_type = type_mapping.get(column_type, "unknown")

        if column.get("is_nullable", False):
            ts_type += " | null"

        return ts_type

    @staticmethod
    def generate_attributes(columns):
        """
        Genera los atributos TypeScript
        a partir de las columnas.
        """

        attributes = []

        for column in columns:
            column_name = column["name"]
            ts_type = ReactTsCrudTypes.get_ts_type(column)

            attributes.append(
                f"  {column_name}: {ts_type};"
            )

        # Campos automáticos de Laravel
        existing_names = {column["name"] for column in columns}

        if "created_at" not in existing_names:
            attributes.append("  created_at: string;")

        if "updated_at" not in existing_names:
            attributes.append("  updated_at: string;")

        return "\n".join(attributes)

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
        Genera el archivo de tipos TypeScript
        para un recurso CRUD.
        """

        folder_path = os.path.join(
            full_path,
            "src",
            "modules",
            namespace,
            plural_name_snake,
            "types"
        )

        attributes = self.generate_attributes(columns)

        content = f'''// src/modules/{namespace}/{plural_name_snake}/types/{singular_name_snake}.types.ts
import type {{ PaginatedResponse }} from "@/components/pagination/pagination.types";

/**
 * Atributos del recurso {singular_name}.
 */
export interface {singular_name}Attributes {{
{attributes}
}}

/**
 * Recurso {singular_name} devuelto por la API.
 */
export interface {singular_name}Resource {{
  type: "{plural_name_kebab}";
  id: string;
  attributes: {singular_name}Attributes;
  links?: {{
    self: string;
  }};
}}


/**
 * Respuesta paginada del listado de sistemas.
 */
export type {plural_name}Response = PaginatedResponse<{singular_name}Resource>;

/**
 * Datos para crear un recurso.
 */
export type Create{singular_name}Input = Omit<
  {singular_name}Attributes,
  "created_at" | "updated_at"
>;

/**
 * Datos para actualizar un recurso.
 */
export type Update{singular_name}Input = Partial<Create{singular_name}Input>;



'''

        return HelperFile.write(
            folder_path=folder_path,
            file_name=f"{singular_name_snake}.types.ts",
            content=content
        )
