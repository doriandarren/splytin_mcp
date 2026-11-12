
from helpers.helper_file import HelperFile
from gen.php_laravel.to_module_crud.helpers.helper_laravel_resource import HelperLaravelResource


class LaravelCrudResource:

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

        folder_path = HelperLaravelResource.get_folder_path(
            full_path,
            version_api,
            plural_name
        )

        column_attributes = HelperLaravelResource.format_column_attributes(
            columns
        )

        includes = HelperLaravelResource.format_includes(
            columns
        )

        relationships = HelperLaravelResource.format_relationships(
            columns,
            singular_name_snake,
            plural_name_snake
        )

        content = f"""<?php

namespace App\\Http\\Resources\\{version_api}\\{plural_name};

use Illuminate\\Http\\Request;
use Illuminate\\Http\\Resources\\Json\\JsonResource;

class {singular_name}Resource extends JsonResource
{{

    /**
     * Transform the resource into an array.
     *
     * @return array<string, mixed>
     */
    public function toArray(Request $request): array
    {{
        return [
            'type' => '{singular_name_snake}',
            'id' => $this->id,
            'attributes' => [
{column_attributes}
                'created_at' => $this->created_at,
                'updated_at' => $this->updated_at,
            ],
{includes}
{relationships}
            'links' => [
                'self' => route('{plural_name_kebab}.show', ['{singular_name_snake}' => $this->id])
            ]
        ];
    }}
}}
"""

        # Crear el archivo
        HelperFile.write(
            folder_path=folder_path,
            file_name=f"{singular_name}Resource.php",
            content=content
        )
