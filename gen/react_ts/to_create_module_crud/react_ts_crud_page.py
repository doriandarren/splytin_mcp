import os
from gen.helpers.helper_file import HelperFile


class ReactTsCrudPage:

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

        folder_path = os.path.join(full_path, "src", "modules", namespace, plural_name_snake, "pages")
                        
        content = f'''// src/modules/{namespace}/{plural_name_snake}/pages/{singular_name}Page.tsx 

import {{ useState }} from "react";
import {{ ChevronLeft, ChevronRight, RefreshCw }} from "lucide-react";

import {{ Button }} from "@/components/ui/button";
import {{ useSystems }} from "../hooks/useSystems";

export const {singular_name}Page = () => {{
  const [page, setPage] = useState(1);

  const {{
    data,
    isPending,
    isError,
    isFetching,
    isPlaceholderData,
    refetch,
  }} = useSystems(page);

  if (isPending) {{
    return <p className="p-6">Cargando sistemas...</p>;
  }}

  if (isError || !data) {{
    return (
      <div className="space-y-4 p-6">
        <p className="text-destructive">
          No se pudieron obtener los sistemas.
        </p>

        <Button onClick={{() => void refetch()}}>
          Reintentar
        </Button>
      </div>
    );
  }}

  const systems = data.data;
  const meta = data.meta;

  return (
    <div className="space-y-6 p-6">
      <div className="flex flex-wrap items-center justify-between gap-3">
        <div>
          <h1 className="text-3xl font-bold">Sistemas</h1>

          <p className="text-sm text-muted-foreground">
            Total de sistemas: {{meta.total}}
          </p>
        </div>

        <Button
          variant="outline"
          onClick={{() => void refetch()}}
          disabled={{isFetching}}
        >
          <RefreshCw
            className={{`size-4 ${{isFetching ? "animate-spin" : ""}}`}}
          />
          Actualizar
        </Button>
      </div>

      <div className="overflow-x-auto rounded-xl border">
        <table className="w-full text-sm">
          <thead className="border-b bg-muted/50">
            <tr>
              <th className="px-4 py-3 text-left">ID</th>
              <th className="px-4 py-3 text-left">Nombre</th>
              <th className="px-4 py-3 text-left">Estado</th>
              <th className="px-4 py-3 text-left">Versión</th>
              <th className="px-4 py-3 text-left">Creación</th>
            </tr>
          </thead>

          <tbody>
            {{systems.map((system) => (
              <tr
                key={{system.id}}
                className="border-b last:border-0 hover:bg-muted/30"
              >
                <td className="px-4 py-3">{{system.id}}</td>

                <td className="px-4 py-3 font-medium">
                  {{system.attributes.name}}
                </td>

                <td className="px-4 py-3">
                  {{system.attributes.status}}
                </td>

                <td className="px-4 py-3">
                  {{system.attributes.version}}
                </td>

                <td className="px-4 py-3">
                  {{new Date(
                    system.attributes.created_at
                  ).toLocaleDateString("es-ES")}}
                </td>
              </tr>
            ))}}

            {{systems.length === 0 && (
              <tr>
                <td
                  colSpan={{5}}
                  className="px-4 py-10 text-center text-muted-foreground"
                >
                  No hay sistemas registrados.
                </td>
              </tr>
            )}}
          </tbody>
        </table>
      </div>

      <div className="flex items-center justify-between gap-3">
        <p className="text-sm text-muted-foreground">
          Página {{meta.current_page}} de {{meta.last_page}}
        </p>

        <div className="flex gap-2">
          <Button
            variant="outline"
            size="sm"
            disabled={{page <= 1 || isFetching}}
            onClick={{() => setPage((p) => Math.max(1, p - 1))}}
          >
            <ChevronLeft className="size-4" />
            Anterior
          </Button>

          <Button
            variant="outline"
            size="sm"
            disabled={{
              isPlaceholderData ||
              page >= meta.last_page ||
              isFetching
            }}
            onClick={{() => setPage((p) => p + 1)}}
          >
            Siguiente
            <ChevronRight className="size-4" />
          </Button>
        </div>
      </div>
    </div>
  );
}};        
'''

        # Crear el archivo
        HelperFile.write(
            folder_path=folder_path,
            file_name=f"{singular_name}Page.tsx",
            content=content
        )