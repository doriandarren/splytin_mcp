import os
from helpers.helper_file import HelperFile


class ReactTsPaginationComponents:
    

    def invoke(self, full_path):
        
        # Components
        self.create_file_custom_pagination_tsx(full_path)
        self.create_file_pagination_types_ts(full_path)
        
        
    
        
    def create_file_custom_pagination_tsx(self, full_path):
        """
        Genera el archivo.
        """
        
        folder_path = os.path.join(full_path, "src", "components", "pagination")
    
        content = r'''// src/components/pagination/CustomPagination.tsx
import { ChevronLeft, ChevronRight } from "lucide-react";
import { useSearchParams } from "react-router";
import { useTranslation } from "react-i18next";

import { Button } from "@/components/ui/button";

interface Props {
    totalPages: number;
    total?: number;
}

export const CustomPagination = ({
    totalPages,
    total = 0,
}: Props) => {
    const { t, i18n } = useTranslation("pagination");
    const [searchParams, setSearchParams] = useSearchParams();

    // Idioma actual
    const locale = i18n.resolvedLanguage?.startsWith("en")
        ? "en-US"
        : "es-ES";

    // Página actual
    const queryPage = Number(searchParams.get("page") ?? "1");

    const page =
        Number.isSafeInteger(queryPage) && queryPage > 0
            ? queryPage
            : 1;

    // Cambiar página
    const handlePageChange = (newPage: number) => {
        if (newPage < 1 || newPage > totalPages) return;

        setSearchParams((prev) => {
            const next = new URLSearchParams(prev);
            next.set("page", newPage.toString());
            return next;
        });
    };

    return (
        <div className="flex flex-wrap items-center justify-between gap-4">

            {/* Total de registros */}
            <span className="text-sm text-muted-foreground">
                {t("total_records", {
                    total: total.toLocaleString(locale),
                })}
            </span>

            {/* Navegación */}
            <div className="flex flex-wrap items-center justify-center gap-2">

                {/* Anterior */}
                <Button
                    variant="outline"
                    size="sm"
                    disabled={page <= 1}
                    onClick={() => handlePageChange(page - 1)}
                >
                    <ChevronLeft className="size-4" />
                    {t("previous")}
                </Button>

                {/* Números de página */}
                {Array.from({ length: totalPages }, (_, index) => {
                    const pageNumber = index + 1;

                    return (
                        <Button
                            key={pageNumber}
                            variant={page === pageNumber ? "default" : "outline"}
                            size="sm"
                            onClick={() => handlePageChange(pageNumber)}
                        >
                            {pageNumber}
                        </Button>
                    );
                })}

                {/* Siguiente */}
                <Button
                    variant="outline"
                    size="sm"
                    disabled={totalPages === 0 || page >= totalPages}
                    onClick={() => handlePageChange(page + 1)}
                >
                    {t("next")}
                    <ChevronRight className="size-4" />
                </Button>
            </div>
        </div>
    );
};'''
        
            # Crear el archivo
        HelperFile.write(
            folder_path=folder_path,
            file_name="CustomPagination.tsx",
            content=content
        )
        
        
        
    def create_file_pagination_types_ts(self, full_path):
        """
        Genera el archivo.
        """
    
        folder_path = os.path.join(full_path, "src", "components", "pagination")
    
        content = r'''// src/components/pagination/pagination.types.ts
/**
 * Metadatos de paginación devueltos por la API.
 */
export interface PaginationMeta {
  current_page: number;
  per_page: number;
  last_page: number;
  total: number;
  from: number | null;
  to: number | null;
}

/**
 * Enlaces de navegación entre páginas.
 */
export interface PaginationLinks {
  first: string;
  last: string;
  prev: string | null;
  next: string | null;
}

/**
 * Respuesta genérica de una colección paginada.
 *
 * T representa el recurso que devuelve cada módulo.
 */
export interface PaginatedResponse<T> {
  data: T[];
  meta: PaginationMeta;
  links: PaginationLinks;
  message?: string;
  status_code?: number;
  success?: boolean;
}
'''
    
        # Crear el archivo
        HelperFile.write(
            folder_path=folder_path,
            file_name="pagination.types.ts",
            content=content
        )