import os
from gen.helpers.helper_print import print_message, GREEN, CYAN



def generate_seeder_file(
    full_path,
    namespace,
    version_api,
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
    Genera el archivo
    """

    folder_path = os.path.join(full_path, "database", "seeders")
    file_path = os.path.join(folder_path, f"{singular_name}Seeder.php")

    os.makedirs(folder_path, exist_ok=True)
    
    # Obtener los nombres de las columnas dinámicamente
    column_names = [column["name"] for column in columns]

    content = f"""<?php

namespace Database\\Seeders;

use Illuminate\\Database\\Seeder;
use App\\Models\\{namespace}\\{plural_name}\\{singular_name};

class {singular_name}Seeder extends Seeder
{{
    /**
    * Run the settings seeds.
    *
    * @return void
    */
    public function run()
    {{
        // php artisan make:seeder {singular_name}Seeder

        {singular_name}::factory()->create([
"""

    # Agregar las columnas dinámicamente en el método `run`
    for column in column_names:
        content += f"            '{column}' => '{column}',\n"

    content += f"""        ]);
    }}
}}
"""

    try:
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)
