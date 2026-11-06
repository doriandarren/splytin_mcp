
import os
from gen.helpers.helper_file import HelperFile


class LaravelCrudFactory:

    def invoke(
        self,
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
        Genera el archivo.
        """

        folder_path = os.path.join(
            full_path,
            "database",
            "factories",
            "API",
            plural_name
        )

        # Obtener los nombres de las columnas dinámicamente
        column_names = [column["name"] for column in columns]

        content = f"""<?php

namespace Database\\Factories\\API\\{plural_name};

use Illuminate\\Database\\Eloquent\\Factories\\Factory;

use App\\Enums\\Dev\\EnumDefaultCompany;

/**
* @extends \\Illuminate\\Database\\Eloquent\\Factories\\Factory<\\App\\Models\\{namespace}\\{plural_name}\\{singular_name}>
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

        # Agregar las columnas dinámicamente
        for column in column_names:
            content += f"            '{column}' => $this->faker->word(),\n"

        content += """        ];

    }
}
"""

        # Crear el archivo
        HelperFile.write(
            folder_path=folder_path,
            file_name=f"{singular_name}Factory.php",
            content=content
        )
