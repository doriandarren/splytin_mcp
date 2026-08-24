import os
from gen.helpers.helper_print import print_message, GREEN, CYAN

def generate_resource(
    full_path,
    namespace,
    version_api,
    project_name,
    singular_name,
    plural_name,
    singular_name_kebab,
    plural_name_kebab,
    singular_name_snake,
    plural_name_snake,
    columns
):
    """
    Genera el archivo
    """

    folder_path = os.path.join(full_path, "app", "Http", "Resources", namespace, version_api, plural_name)
    file_path = os.path.join(folder_path, f"{singular_name}Resource.php")

    os.makedirs(folder_path, exist_ok=True)

    content = f'''<?php

namespace App\\Http\\Resources\\{namespace}\\{version_api}\\{plural_name};

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
'''
    
    content += "\n".join(
    [
        f"                '{column['name']}' => $this->{column['name']},"
        for column in columns
    ]
)


    content += f'''
                'created_at' => $this->created_at,
                'updated_at' => $this->updated_at,
            ],
            //'relationships' => [
            //    'author' => [
            //        'data' => [
            //            'type' => 'user',
            //            'id' => $this->user_id
            //        ],
            //        'links' => [
            //            'self' => route('authors.show', ['author' => $this->user_id])
            //        ]
            //    ]
            //],
            //'includes' => new UserResource($this->whenLoaded('author')),
            //'links' => [
            //    'self' => route('tickets.show', ['ticket' => $this->id])
            //]
        ];
    }}
}}
'''

    try:
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)
