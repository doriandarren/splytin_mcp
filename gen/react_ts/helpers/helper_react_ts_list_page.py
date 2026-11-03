
import json


class HelperReactTsListPage:

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
            return (
                f'{value} == null ? "-" : '
                f'JSON.stringify({value})'
            )

        return f'{value} ?? "-"'

    
    
    @staticmethod
    def generate_actions_column(plural_name_kebab):
        """
        Genera las acciones Editar y Eliminar.
        """

        return f'''  {{
    key: "actions",
    header: "actions",
    render: (item) => (
        <div className="flex items-center gap-2">
            <Button
                nativeButton={{false}}
                variant="outline"
                size="sm"
                render={{
                    <Link to={{`/admin/{plural_name_kebab}/${{item.id}}/edit`}} />
                }}
            >
                <Pencil className="size-4" />
                Editar
            </Button>

            <Button
                variant="destructive"
                size="sm"
                onClick={{() => onDelete(item.id)}}
                disabled={{isDeleting}}
            >
                <Trash2 className="size-4" />
                Eliminar
            </Button>
        </div>
    ),
}},'''




    @staticmethod
    def generate_columns(columns, plural_name_kebab):
        """
        Genera todas las columnas de CustomTable:
        - id
        - Columnas dinámicas
        - created_at
        - actions
        """

        result = [
            '  {',
            '    key: "id",',
            '    header: "id",',
            '    render: (item) => item.id,',
            '  },'
        ]

        existing_names = {"id", "actions"}

        for column in columns:
            name = column["name"]

            if name in existing_names:
                continue

            existing_names.add(name)

            result.extend([
                '  {',
                f'    key: {json.dumps(name, ensure_ascii=False)},',
                f'    header: {json.dumps(name, ensure_ascii=False)},',
                f'    render: (item) => {HelperReactTsListPage.get_column_render(column)},',
                '  },'
            ])

        # Añadir created_at si no existe
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

        # Añadir columna actions
        result.append(
            HelperReactTsListPage.generate_actions_column(
                plural_name_kebab
            )
        )

        return "\n".join(result)


