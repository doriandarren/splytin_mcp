import os
from gen.helpers.helper_file import HelperFile
from gen.helpers.helper_print import print_cyan, print_green, print_red, run_command


class ReactTsTanstackQuery:
    
    
    def invoke(self, full_path):
        self.install(full_path)
        self.create_query_provider(full_path)
        self.update_app(full_path)
    
    
    
    def install(self, full_path):
        # Instalar dependencias
        run_command(
            "npm install @tanstack/react-query",
            cwd=full_path
        )
        
        print_green("@tanstack/react-query creado correctamente.")



    def create_query_provider(self, full_path):
        """
        Genera el archivo.
        """
    
        folder_path = os.path.join(full_path, "src", "providers")
    
        content = r'''// src/providers/QueryProvider.tsx
import {
  QueryClient,
  QueryClientProvider,
} from "@tanstack/react-query";

import type { ReactNode } from "react";

export const queryClient = new QueryClient({
  defaultOptions: {
    queries: {
      staleTime: 60 * 1000,
      retry: 1,
      refetchOnWindowFocus: false,
    },
  },
});

interface QueryProviderProps {
  children: ReactNode;
}

export const QueryProvider = ({ children }: QueryProviderProps) => {
  return (
    <QueryClientProvider client={queryClient}>
      {children}
    </QueryClientProvider>
  );
};
'''
    
        # Crear el archivo
        HelperFile.write(
            folder_path=folder_path,
            file_name="QueryProvider.tsx",
            content=content
        )




    def update_app(self, full_path):
        """
        Actualiza el archivo
        """
        main_path = os.path.join(full_path, "src", "App.tsx")
    
        # Verificar si el archivo existe
        if not os.path.exists(main_path):
            print_cyan(f"Error: {main_path} no existe.")
            return False
    
        try:
            # Leer el contenido del archivo
            with open(main_path, "r", encoding="utf-8") as f:
                content = f.read()
    
            # Reemplazos
            replacements = {
                ## New Item -> KEY : VALUE
                """<Suspense fallback={<div>Cargando...</div>}>
      <RouterProvider router={appRouter} />
    </Suspense>""":
                """<QueryProvider>
      <Suspense fallback={<div>Cargando...</div>}>
        <RouterProvider router={appRouter} />
      </Suspense>
    </QueryProvider>""",
                """import { appRouter } from "./app.router";""":
                """import { appRouter } from "./app.router";
import { QueryProvider } from "./providers/QueryProvider";"""
            }
    
            # Validar y aplicar los reemplazos
            new_content = content
    
            for old_text, new_text in replacements.items():
                if old_text not in new_content:
                    raise ValueError(f"No se encontró el texto esperado: {old_text}")
    
                new_content = new_content.replace(old_text, new_text, 1)
    
            if new_content == content:
                raise ValueError("No se realizó ningún reemplazo.")
    
            # Escribir el contenido actualizado
            with open(main_path, "w", encoding="utf-8") as f:
                f.write(new_content)
    
            print_green(f"{main_path} actualizado correctamente.")
    
            return True
    
        except Exception as e:
            print_red(f"Error al actualizar {main_path}: {e}")
            return False
    
        