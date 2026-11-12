import os
from helpers.helper_file import HelperFile
from helpers.helper_print import print_cyan, print_green, print_red, run_command


class ReactTsSonner:

    def invoke(self, full_path):
        self.install(full_path)
        self.create_alerta_ts(full_path)
        self.update_app(full_path)
            
    
    
    def install(self, full_path):
        # Instalar dependencias
        run_command(
            "npx shadcn@latest add sonner",
            cwd=full_path
        )
        
        print_green("Proyecto creado correctamente.")



    def create_alerta_ts(self, full_path):
        """
        Genera el archivo.
        """
    
        folder_path = os.path.join(full_path, "src", "components", "alerts")
    
        content = r'''// src/components/alerts/alerta.ts
import { toast } from "sonner";

export const alerta = {
  success: (message: string) => {
    return toast.success(message);
  },

  error: (message: string) => {
    return toast.error(message);
  },

  warning: (message: string) => {
    return toast.warning(message);
  },

  info: (message: string) => {
    return toast.info(message);
  },

  loading: (message: string) => {
    return toast.loading(message);
  },

  dismiss: (id?: string | number) => {
    toast.dismiss(id);
  },
};
'''
    
        # Crear el archivo
        HelperFile.write(
            folder_path=folder_path,
            file_name="alerta.ts",
            content=content
        )
        
    
    
    def update_app(self, full_path):
        """
        Actualiza App.tsx agregando:
        - QueryProvider.
        - Toaster de Sonner.
        - Evita duplicados.
        """

        main_path = os.path.join(full_path, "src", "App.tsx")

        if not os.path.isfile(main_path):
            print_cyan(f"Error: {main_path} no existe.")
            return False

        try:
            with open(main_path, "r", encoding="utf-8") as f:
                content = f.read()

            new_content = content

            # Agregar import Toaster
            if 'import { Toaster } from "@/components/ui/sonner";' not in new_content:
                new_content = new_content.replace(
                    'import { QueryProvider } from "./providers/QueryProvider";',
                    '''import { QueryProvider } from "./providers/QueryProvider";
import { Toaster } from "@/components/ui/sonner";''',
                    1
                )

            # 4. Agregar Toaster si no existe
            if "<Toaster" not in new_content:
                
                # Añadir Fragment y Toaster
                new_content = new_content.replace(
                    """  return (
    <QueryProvider>""",
                    """  return (
    <>
      <QueryProvider>""",
                    1
                )

                new_content = new_content.replace(
                    """    </QueryProvider>
  );""",
                    """      </QueryProvider>
      <Toaster position="top-right" richColors closeButton duration={4000} />
    </>
  );""",
                    1
                )

            if new_content == content:
                print_cyan("App.tsx ya está actualizado.")
                return True

            with open(main_path, "w", encoding="utf-8") as f:
                f.write(new_content)

            print_green(f"{main_path} actualizado correctamente.")
            return True

        except Exception as e:
            print_red(f"Error al actualizar {main_path}: {e}")
            return False
