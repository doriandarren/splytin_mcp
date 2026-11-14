import os
from helpers.helper_print import print_green, print_red



class LaravelUpdateRouteApiPhp:

    def invoke(self, full_path):
        self.update_use(full_path)
        self.update_route(full_path)



    def update_use(self, full_path):
        """
        Actualiza el archivo
        """
        main_jsx_path = os.path.join(full_path, "routes", "api.php")

        # Verificar si el archivo existe
        if not os.path.exists(main_jsx_path):
            print_red(f"Error: {main_jsx_path} no existe.")
            return

        try:

            # Leer el contenido del archivo
            with open(main_jsx_path, "r") as f:
                content = f.read()


            # Reemplazos
            content = content.replace(
            """<?php
""",
            """<?php

use App\\Enums\\EnumApiSetup;"""
        )

            # Escribir el contenido actualizado
            with open(main_jsx_path, "w") as f:
                f.write(content)

            print_green("use api.php correctamente.")

        except Exception as e:
            print_red(f"Error al actualizar {main_jsx_path}: {e}")







    def update_route(self, full_path):
        """
        Agrega un bloque de contenido al final del archivo
        """
        file_path = os.path.join(full_path, "routes", "api.php")

        if not os.path.exists(file_path):
            print_red(f"Error: {file_path} no existe.")
            return

        block_to_add = """

Route::prefix(EnumApiSetup::API_VERSION )->group(function () {
    // Auth
    require base_path('routes/API/V1/auth.php');
    require base_path('routes/API/V1/dashboards.php');
    
    // Shared
    require base_path('routes/API/V1/dev.php');
    
    // API
    // ...
});
"""

        lines_to_add = block_to_add.splitlines()

        try:
            with open(file_path, "r") as f:
                existing_lines = f.read().splitlines()

            # Eliminar líneas en blanco al final
            while existing_lines and existing_lines[-1].strip() == "":
                existing_lines.pop()

            new_lines = []

            for line in lines_to_add:
                if line.strip() == "" or line not in existing_lines:
                    new_lines.append(line)

            if new_lines:
                with open(file_path, "w") as f:
                    f.write("\n".join(existing_lines + new_lines) + "\n")
                print_green(f"Actualizo el archivo api.php")
            else:
                print_green(f"No hay nuevas líneas que agregar")

        except Exception as e:
            print_red(f"Error al actualizar {file_path}: {e}")