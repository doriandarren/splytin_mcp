
import os

from helpers.helper_file import HelperFile
from gen.react_ts.helpers.helper_react_ts_list_page import HelperReactTsListPage


class ReactTsCrudList:

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
        Genera la página de listado y el hook Delete.
        """

        self.create_pages_tsx(
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
        )

        self.create_hook_use_ts(
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
        )

    def create_hook_use_ts(
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
        Genera el hook para eliminar registros.
        """

        folder_path = os.path.join(
            full_path,
            "src",
            "modules",
            namespace,
            plural_name_snake,
            "hooks"
        )

        content = f'''// src/modules/{namespace}/{plural_name_snake}/hooks/useDelete{singular_name}.ts

import {{ useMutation, useQueryClient }} from "@tanstack/react-query";

import {{ delete{singular_name} }} from "../services/{plural_name_camel}Service";
import {{ {plural_name_camel}Keys }} from "../queries/{plural_name_camel}Queries";

export const useDelete{singular_name} = () => {{
  const queryClient = useQueryClient();

  return useMutation({{
    mutationFn: delete{singular_name},

    onSuccess: async () => {{
      await queryClient.invalidateQueries({{
        queryKey: {plural_name_camel}Keys.lists(),
      }});
    }},
  }});
}};
'''

        HelperFile.write(
            folder_path=folder_path,
            file_name=f"useDelete{singular_name}.ts",
            content=content
        )

    def create_pages_tsx(
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
        Genera la página de listado CRUD
        con CustomTable, Create, Edit y Delete.
        """

        folder_path = os.path.join(
            full_path,
            "src",
            "modules",
            namespace,
            plural_name_snake,
            "pages"
        )

        content = f'''// src/modules/{namespace}/{plural_name_snake}/pages/{singular_name}Page.tsx
import {{ Link, useSearchParams }} from "react-router";
import {{ Plus, Pencil, Trash2 }} from "lucide-react";
import {{ alerta }} from "@/components/alerts/alerta";
import {{ Button }} from "@/components/ui/button";
import {{ CustomTable }} from "@/components/table/CustomTable";
import type {{ TableColumn }} from "@/components/table/table.types";
import type {{ {singular_name}Resource }} from "../types/{singular_name_snake}.types";
import {{ use{plural_name} }} from "../hooks/use{plural_name}";
import {{ useDelete{singular_name} }} from "../hooks/useDelete{singular_name}";



const columns = (
  onDelete: (id: string) => void,
  isDeleting: boolean
): TableColumn<{singular_name}Resource>[] => [
{HelperReactTsListPage.generate_columns(columns, plural_name_kebab)}
];

export const {singular_name}Page = () => {{
  const [searchParams] = useSearchParams();

  const rawPage = Number(searchParams.get("page") ?? "1");

  const page =
    Number.isSafeInteger(rawPage) && rawPage > 0
      ? rawPage
      : 1;

  // Listado
  const query = use{plural_name}(page);

  // Eliminar
  const deleteItem = useDelete{singular_name}();

  const handleDelete = async (id: string) => {{
    if (!window.confirm("¿Seguro que deseas eliminar este registro?")) {{
      return;
    }}

    try {{
      await deleteItem.mutateAsync(id);
      alerta.success("Registro eliminado correctamente");
    }} catch (error) {{
      console.error("Error al eliminar el registro:", error);
    }}
  }};

  return (
    <CustomTable<{singular_name}Resource>
      title="{plural_name}"
      description={{`Total de {plural_name_snake}: ${{query.data?.meta?.total ?? 0}}`}}
      columns={{columns(handleDelete, deleteItem.isPending)}}
      data={{query.data?.data ?? []}}
      getRowKey={{(item) => item.id}}
      meta={{query.data?.meta}}
      isLoading={{query.isPending}}
      isFetching={{query.isFetching}}
      isPlaceholderData={{query.isPlaceholderData}}
      isError={{query.isError || (!query.isPending && !query.data)}}
      onRefresh={{() => void query.refetch()}}
      emptyMessage="No hay registros."
      headerActions={{
        <Button
          nativeButton={{false}}
          render={{<Link to="/admin/{plural_name_kebab}/create" />}}
        >
          <Plus className="size-4" />
          Nuevo {singular_name}
        </Button>
      }}
    />
  );
}};
'''

        HelperFile.write(
            folder_path=folder_path,
            file_name=f"{singular_name}Page.tsx",
            content=content
        )
