import os
from gen.helpers.helper_print import print_message, GREEN, CYAN

def generate_factory_file(
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

    folder_path = os.path.join(full_path, "database", "factories")
    file_path = os.path.join(folder_path, f"{singular_name}Factory.php")

    os.makedirs(folder_path, exist_ok=True)
    
    # Obtener los nombres de las columnas dinámicamente
    column_names = [column["name"] for column in columns]

    content = f"""<?php

namespace Database\\Factories\\{plural_name};

use Illuminate\\Database\\Eloquent\\Factories\\Factory;

/**
* @extends \\Illuminate\\Database\\Eloquent\\Factories\\Factory<\\App\\Models\\{plural_name}\\{singular_name}>
*/
class {singular_name}Factory extends Factory
{{
    /**
    * Define the model's default state.
    *
    * @return array<string, mixed>
    */
    public function definition()
    {{
        // php artisan make:factory {singular_name}Factory

        return [
"""

    # Agregar las columnas dinámicamente en el método `definition`
    for column in column_names:
        content += f"            '{column}' => $this->faker->word(),\n"

    content += f"""        ];

    }}
}}
"""

    try:
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)
