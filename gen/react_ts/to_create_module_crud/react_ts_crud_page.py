
import os
import json
from gen.helpers.helper_file import HelperFile


class ReactTsCrudPage:

    @staticmethod
    def get_column_render(column):
        """
        Genera el render de una columna
        según su tipo de dato.
        """

        name = column["name"]
        column_type = column.get("type", "string")
        value = f"item.attributes.{name}"

        if column.get("is_fk", False):
            column_type = "fk"

        if column_type == "boolean":
            return (
                f'{value} == null ? "-" : '
                f'{value} ? "Sí" : "No"'
            )

        if column_type in ("date", "datetime", "timestamp"):
            return (
                f'{value} ? '
                f'new Date({value}).toLocaleDateString("es-ES") '
                f': "-"'
            )

        if column_type in ("decimal", "float", "double"):
            return (
                f'{value} == null ? "-" : '
                f'Number({value}).toLocaleString("es-ES")'
            )

        if column_type == "json":
            return f'{value} == null ? "-" : JSON.stringify({value})'

        return f'{value} ?? "-"'

    @staticmethod
    def generate_columns(columns):
        """
        Genera las columnas dinámicas para CustomTable.

        Los nombres de key y header se mantienen
        exactamente como aparecen en columns.
        """

        result = [
            '  {',
            '    key: "id",',
            '    header: "id",',
            '    render: (item) => item.id,',
            '  },'
        ]

        existing_names = {"id"}

        for column in columns:
            name = column["name"]

            if name in existing_names:
                continue

            existing_names.add(name)

            render = ReactTsCrudPage.get_column_render(column)

            result.extend([
                '  {',
                f'    key: {json.dumps(name, ensure_ascii=False)},',
                f'    header: {json.dumps(name, ensure_ascii=False)},',
                f'    render: (item) => {render},',
                '  },'
            ])

        # Añadir created_at si no está en columns
        if "created_at" not in existing_names:
            result.extend([
                '  {',
                '    key: "created_at",',
                '    header: "created_at",',
                '    render: (item) =>',
                '      item.attributes.created_at',
                '        ? new Date(item.attributes.created_at).toLocaleDateString("es-ES")',
                '        : "-",',
                '  },'
            ])

        return "\n".join(result)

    
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
        Genera una página CRUD React + TypeScript
        utilizando el componente CustomTable.
        """

        folder_path = os.path.join(
            full_path,
            "src",
            "modules",
            namespace,
            plural_name_snake,
            "pages"
        )

        component_name = f"{singular_name}Page"
        resource_name = f"{singular_name}Resource"
        hook_name = f"use{plural_name}"

        table_columns = self.generate_columns(columns)

        content = f'''// src/modules/{namespace}/{plural_name_snake}/pages/{component_name}.tsx
import {{ Link, useSearchParams }} from "react-router";
import {{ Plus }} from "lucide-react";
import {{ CustomTable }} from "@/components/table/CustomTable";
import type {{ TableColumn }} from "@/components/table/table.types";
import type {{ {resource_name} }} from "../types/{singular_name_snake}.types";
import {{ {hook_name} }} from "../hooks/{hook_name}";


const columns: TableColumn<{resource_name}>[] = [
{table_columns}
];


export const {component_name} = () => {{
    const [searchParams] = useSearchParams();

    const rawPage = Number(searchParams.get("page") ?? "1");

    const page =
        Number.isSafeInteger(rawPage) && rawPage > 0
        ? rawPage
        : 1;

    const query = {hook_name}(page);

    return (
        <CustomTable<{resource_name}>
            title="{plural_name}"
            description={{`Total de {plural_name_snake}: ${{query.data?.meta?.total ?? 0}}`}}
            columns={{columns}}
            data={{query.data?.data ?? []}}
            getRowKey={{(item) => item.id}}
            meta={{query.data?.meta}}
            isLoading={{query.isPending}}
            isFetching={{query.isFetching}}
            isPlaceholderData={{query.isPlaceholderData}}
            isError={{query.isError || (!query.isPending && !query.data)}}
            onRefresh={{() => void query.refetch()}}
            emptyMessage="No hay registros."
            
            // Botones personalizados del encabezado
            headerActions={{
            <Button
                render={{<Link to="/admin/systems/create" />}}
            >
                <Plus className="size-4" />
                Nuevo sistema
            </Button>
        }}
        />
    );
}};
    '''

        return HelperFile.write(
            folder_path=folder_path,
            file_name=f"{component_name}.tsx",
            content=content
        )
