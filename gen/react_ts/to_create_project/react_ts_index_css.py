import os
from gen.helpers.helper_print import dd, print_green, print_red
from gen.react_ts.to_create_project.helpers.helper_react_ts_index_css import HelperReactTsIndexCss


class ReactTsIndexCss:

    def invoke(self, full_path):
        """
        Genera el archivo.
        """
        self.update_file(full_path)
        self.update_lines(full_path)
        
    
    
    def update_file(self, full_path):
        """
        Actualiza el archivo
        """
        main_path = os.path.join(full_path, "src", "index.css")
    
        # Verificar si el archivo existe
        if not os.path.exists(main_path):
            print_red(f"Error: {main_path} no existe.")
            dd(f"Error: {main_path} no existe.")
            return False
    
        try:
            # Leer el contenido del archivo
            with open(main_path, "r", encoding="utf-8") as f:
                content = f.read()
    

            # Reemplazos
            replacements = {
                ## New Item -> KEY : VALUE
                """  html {
    @apply font-sans;
    }""":
                """  html {
      @apply font-sans;
    }
    
    /* Cursor pointer para todos los botones */
    button:not(:disabled) {
        @apply cursor-pointer;
    }

    /* Cursor para botones deshabilitados */
    button:disabled {
        @apply cursor-not-allowed;
    }""",
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
    
 

    def update_lines(self, full_path):
        """
        Actualiza las variables de los temas claro y oscuro.
        """
        
        replacements = {
            "--background": [
                "oklch(1 0 0)",     # :root
                "oklch(0.145 0 0)",   # .dark
            ],
            "--foreground": [
                "oklch(0.23419 0.04671 250.475)",   # :root
                "oklch(0.97427 0.01005 228.886)",   # .dark
            ],
            "--card": [
                "oklch(1 0 0)",
                "oklch(0.24573 0.04480 249.009)",
            ],
            "--card-foreground": [
                "oklch(0.41441 0.05197 19.512)",
                "oklch(0.97427 0.01005 228.886)",
            ],
            "--popover": [
                "oklch(1 0 0)",
                "oklch(0.24573 0.04480 249.009)",
            ],
            "--popover-foreground": [
                "oklch(0.23419 0.04671 250.475)",
                "oklch(0.97427 0.01005 228.886)",
            ],
            "--primary": [
                "oklch(0.50220 0.09947 234.694)",
                "oklch(0.69198 0.13320 232.282)",
            ],
            "--primary-foreground": [
                "oklch(1 0 0)",
                "oklch(0.19558 0.03702 249.816)",
            ],
            "--secondary": [
                "oklch(0.96594 0.01507 228.960)",
                "oklch(0.31377 0.05284 243.554)",
            ],
            "--secondary-foreground": [
                "oklch(0.44994 0.08955 236.020)",
                "oklch(0.96594 0.01507 228.960)",
            ],
            "--muted": [
                "oklch(0.96722 0.00669 233.640)",
                "oklch(0.29923 0.04796 244.534)",
            ],
            "--muted-foreground": [
                "oklch(0.55439 0.04072 257.417)",
                "oklch(0.76997 0.03591 238.830)",
            ],
            "--accent": [
                "oklch(0.96594 0.01507 228.960)",
                "oklch(0.34802 0.06056 238.977)",
            ],
            "--accent-foreground": [
                "oklch(0.44994 0.08955 236.020)",
                "oklch(0.96594 0.01507 228.960)",
            ],
            "--destructive": [
                "oklch(0.59155 0.20203 21.239)",
                "oklch(0.71063 0.16615 22.216)",
            ],
            "--border": [
                "oklch(0.91942 0.01437 238.020)",
                "oklch(0.37093 0.04904 243.076)",
            ],
            "--input": [
                "oklch(0.91942 0.01437 238.020)",
                "oklch(0.37093 0.04904 243.076)",
            ],
            "--ring": [
                "oklch(0.68313 0.13756 233.260)",
                "oklch(0.69198 0.13320 232.282)",
            ],
            "--chart-1": [
                "oklch(0.68313 0.13756 233.260)",
                "oklch(0.69198 0.13320 232.282)",
            ],
            "--chart-2": [
                "oklch(0.50220 0.09947 234.694)",
                "oklch(0.50220 0.09947 234.694)",
            ],
            "--chart-3": [
                "oklch(0.58084 0.13334 245.954)",
                "oklch(0.75448 0.11154 230.865)",
            ],
            "--chart-4": [
                "oklch(0.23419 0.04671 250.475)",
                "oklch(0.82070 0.08044 228.714)",
            ],
            "--chart-5": [
                "oklch(0.82070 0.08044 228.714)",
                "oklch(0.50055 0.08072 240.684)",
            ],
            "--sidebar": [
                "oklch(1 0 0)",
                "oklch(0.23419 0.04671 250.475)",
            ],
            "--sidebar-foreground": [
                "oklch(0.23419 0.04671 250.475)",
                "oklch(0.97427 0.01005 228.886)",
            ],
            "--sidebar-primary": [
                "oklch(0.50220 0.09947 234.694)",
                "oklch(0.69198 0.13320 232.282)",
            ],
            "--sidebar-primary-foreground": [
                "oklch(1 0 0)",
                "oklch(0.19558 0.03702 249.816)",
            ],
            "--sidebar-accent": [
                "oklch(0.96594 0.01507 228.960)",
                "oklch(0.34802 0.06056 238.977)",
            ],
            "--sidebar-accent-foreground": [
                "oklch(0.44994 0.08955 236.020)",
                "oklch(0.96594 0.01507 228.960)",
            ],
            "--sidebar-border": [
                "oklch(0.91942 0.01437 238.020)",
                "oklch(0.37093 0.04904 243.076)",
            ],
            "--sidebar-ring": [
                "oklch(0.68313 0.13756 233.260)",
                "oklch(0.69198 0.13320 232.282)",
            ],
        }

        try:
            HelperReactTsIndexCss.update_lines(
                full_path,
                replacements,
            )

            print_green("index.css actualizado correctamente.")
            return True

        except Exception as e:
            print_red(f"Error al actualizar index.css: {e}")
            return False
    
        
