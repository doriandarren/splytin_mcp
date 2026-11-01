import os
from gen.helpers.helper_file import HelperFile


class ReactTsTableComponent:
    
    def invoke(self, full_path):
        self.create_custom_table_tsx(full_path)
        self.create_table_types_ts(full_path)
        
        
    

    def create_custom_table_tsx(self, full_path):
        """
        Genera el archivo.
        """

        folder_path = os.path.join(full_path, "src", "components", "table")

        content = r'''// src/components/table/CustomTable.tsx
import { RefreshCw } from "lucide-react";

import { Button } from "@/components/ui/button";
import { CustomPagination } from "@/components/pagination/CustomPagination";

import type { CustomTableProps } from "./table.types";

export function CustomTable<T>({
  title,
  description,
  data,
  columns,
  getRowKey,
  meta,
  isLoading = false,
  isFetching = false,
  isPlaceholderData = false,
  isError = false,
  onRefresh,
  emptyMessage = "No hay registros.",
}: CustomTableProps<T>) {
  if (isError) {
    return (
      <div className="space-y-4 p-6">
        <p className="text-destructive">
          No se pudieron cargar los registros.
        </p>

        {onRefresh && (
          <Button onClick={onRefresh}>
            Reintentar
          </Button>
        )}
      </div>
    );
  }

  return (
    <div className="space-y-6 p-6">
      {/* Cabecera */}
      <div className="flex flex-wrap items-center justify-between gap-4">
        <div>
          <h1 className="text-3xl font-bold">
            {title}
          </h1>

          {description && (
            <p className="text-sm text-muted-foreground">
              {description}
            </p>
          )}
        </div>

        {onRefresh && (
          <Button
            variant="outline"
            onClick={onRefresh}
            disabled={isFetching}
          >
            <RefreshCw
              className={
                isFetching
                  ? "size-4 animate-spin"
                  : "size-4"
              }
            />
            Actualizar
          </Button>
        )}
      </div>

      {/* Tabla */}
      <div
        className={`overflow-hidden rounded-md border ${
          isPlaceholderData ? "opacity-60" : ""
        }`}
      >
        <div className="overflow-x-auto">
          <table className="w-full caption-bottom text-sm">
            <thead className="border-b bg-muted/50">
              <tr>
                {columns.map((column) => (
                  <th
                    key={column.key}
                    className="h-12 px-4 text-left font-medium"
                  >
                    {column.header}
                  </th>
                ))}
              </tr>
            </thead>

            <tbody>
              {isLoading ? (
                <tr>
                  <td
                    colSpan={columns.length}
                    className="h-24 text-center"
                  >
                    Cargando registros...
                  </td>
                </tr>
              ) : data.length === 0 ? (
                <tr>
                  <td
                    colSpan={columns.length}
                    className="h-24 text-center text-muted-foreground"
                  >
                    {emptyMessage}
                  </td>
                </tr>
              ) : (
                data.map((item) => (
                  <tr
                    key={getRowKey(item)}
                    className="border-b transition-colors hover:bg-muted/50 last:border-0"
                  >
                    {columns.map((column) => (
                      <td
                        key={column.key}
                        className="p-4 align-middle"
                      >
                        {column.render(item)}
                      </td>
                    ))}
                  </tr>
                ))
              )}
            </tbody>
          </table>
        </div>
      </div>

      {/* Paginación */}
      {meta && (
        <div className="flex flex-wrap items-center justify-between gap-4">
          <p className="text-sm text-muted-foreground">
            Página {meta.current_page} de {meta.last_page}
          </p>

          <CustomPagination
            totalPages={meta.last_page}
          />
        </div>
      )}

      {/* Cambio de página */}
      {isPlaceholderData && (
        <p className="text-center text-xs text-muted-foreground">
          Cargando la nueva página...
        </p>
      )}
    </div>
  );
}
'''

        # Crear el archivo
        HelperFile.write(
            folder_path=folder_path,
            file_name="CustomTable.tsx",
            content=content
        )
        
        
        
        
    def create_table_types_ts(self, full_path):
            """
            Genera el archivo.
            """
    
            folder_path = os.path.join(full_path, "src", "components", "table")
    
            content = r'''// src/components/table/table.types.ts
import type { ReactNode, Key } from "react";

export interface TableColumn<T> {
  key: string;
  header: string;
  render: (item: T) => ReactNode;
}

export interface TablePaginationMeta {
  total: number;
  current_page: number;
  last_page: number;
}

export interface CustomTableProps<T> {
  title: string;
  description?: string;

  data: T[];
  columns: TableColumn<T>[];
  getRowKey: (item: T) => Key;

  meta?: TablePaginationMeta;

  isLoading?: boolean;
  isFetching?: boolean;
  isPlaceholderData?: boolean;
  isError?: boolean;

  onRefresh?: () => void;

  emptyMessage?: string;
}
'''
    
            # Crear el archivo
            HelperFile.write(
                folder_path=folder_path,
                file_name="table.types.ts",
                content=content
            )