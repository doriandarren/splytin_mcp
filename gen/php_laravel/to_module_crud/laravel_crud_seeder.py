
import os
from helpers.helper_file import HelperFile


class LaravelCrudSeeder:

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
            "seeders"
        )

        # Obtener los nombres de las columnas
        column_names = [column["name"] for column in columns]

        content = f"""<?php

namespace Database\\Seeders;

use Illuminate\\Database\\Seeder;
use App\\Models\\{namespace}\\{plural_name}\\{singular_name};
use App\\Enums\\Dev\\EnumDefaultCompany;

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

        # Agregar las columnas dinámicamente
        for column in column_names:
            content += f"            '{column}' => '{column}',\n"

        content += """            'created_by' => EnumDefaultCompany::SYSTEM_ID,
            'updated_by' => EnumDefaultCompany::SYSTEM_ID,
        ]);
    }
}
"""

        # Crear el archivo
        HelperFile.write(
            folder_path=folder_path,
            file_name=f"{singular_name}Seeder.php",
            content=content
        )
