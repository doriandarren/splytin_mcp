import os
from gen.helpers.helper_print import print_message, GREEN, CYAN




def formmat_column_attributes(columns):
    lines = []

    for column in columns:
        lines.append(f"                '{column['name']}' => $this->{column['name']},")

    content = "\n".join(lines)

    return content



def format_relationships(columns, singular_name_snake, plural_name_snake):
    lines = []
    
    flag = False
    
    for column in columns:
        if column["is_fk"]:
            flag = True
    
    
    if flag:
        
        lines.append(f"""            'relationships' => [""")                
        
        for column in columns:
            if column["is_fk"]:
                
                column_name_case = column["relationship_name"].replace("_", "-")
                
                lines.append(f"""                '{column["relationship_name"]}' => [
                    'data' => [
                        'type' => '{column["relationship_name"]}',
                        'id' => $this->{column["relationship_column"]}
                    ],
                    'links' => [
                        'self' => route('{column["related_table"]}.show', ['{column_name_case}' => $this->{column["relationship_column"]}])
                    ]
                ],""")
                
        lines.append(f"""            ],""")


    content = "\n".join(lines)

    return content




def format_includes(columns):
    lines = []
    
    flag = False
    
    for column in columns:
        if column["is_fk"]:
            flag = True
    
    
    if flag:
        
        lines.append(f"""            // 'includes' => [""")                
        
        for column in columns:
            if column["is_fk"]:
                lines.append(f"""                // new {column["related_model"]}Resource($this->whenLoaded('{column["related_table"]}')),""")
                
        lines.append(f"""            //],""")


    content = "\n".join(lines)

    return content
    






def generate_resource(
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

    folder_path = os.path.join(full_path, "app", "Http", "Resources", namespace, version_api, plural_name)
    file_path = os.path.join(folder_path, f"{singular_name}Resource.php")

    os.makedirs(folder_path, exist_ok=True)

    content = f"""<?php

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
{formmat_column_attributes(columns)}
                'created_at' => $this->created_at,
                'updated_at' => $this->updated_at,
            ],
{format_relationships(columns, singular_name_snake, plural_name_snake)}

{format_includes(columns)}

            //'includes' => new UserResource($this->whenLoaded('author')),
            'links' => [
                'self' => route('{plural_name_kebab}.show', ['{plural_name_snake}' => $this->{singular_name_snake}_id])
            ]
        ];
    }}
}}
"""

    try:
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)








## Para probar solamente
if __name__ == "__main__":
    
    columns = [
        {
            'is_fk': True,
            'is_index': False,
            'is_nullable': False,
            'is_unique': False,
            'is_unsigned': False,
            'name': 'user_id',
            'options': ['fk'],
            'precision': None,
            'raw_type': 'fk',
            'related_model': 'User',
            'related_table': 'users',
            'relationship_name': 'user',
            'relationship_column': 'user_id',
            'scale': None,
            'size': None,
            'type': 'fk',
        },
        {
            'is_fk': True,
            'is_index': False,
            'is_nullable': False,
            'is_unique': False,
            'is_unsigned': False,
            'name': 'customer_id',
            'options': ['fk'],
            'precision': None,
            'raw_type': 'fk',
            'related_model': 'Customer',
            'related_table': 'customers',
            'relationship_name': 'customer',
            'relationship_column': 'customer_id',
            'scale': None,
            'size': None,
            'type': 'fk',
        },
        {
            'is_fk': False,
            'is_index': False,
            'is_nullable': False,
            'is_unique': True,
            'is_unsigned': False,
            'name': 'name',
            'options': ['string(30)', 'unique'],
            'precision': None,
            'raw_type': 'string(30)',
            'scale': None,
            'size': 30,
            'type': 'string',
        },
        {
            'is_fk': False,
            'is_index': False,
            'is_nullable': False,
            'is_unique': False,
            'is_unsigned': False,
            'name': 'amount',
            'options': ['decimal(10,2)'],
            'precision': 10,
            'raw_type': 'decimal(10,2)',
            'scale': 2,
            'size': None,
            'type': 'decimal',
        },
        {
            'is_fk': False,
            'is_index': False,
            'is_nullable': False,
            'is_unique': False,
            'is_unsigned': False,
            'name': 'amount_with_tax',
            'options': ['float'],
            'precision': None,
            'raw_type': 'float',
            'scale': None,
            'size': None,
            'type': 'float',
        },
        {
            'is_fk': False,
            'is_index': False,
            'is_nullable': False,
            'is_unique': False,
            'is_unsigned': False,
            'name': 'description',
            'options': ['varchar(10)'],
            'precision': None,
            'raw_type': 'varchar(10)',
            'scale': None,
            'size': 10,
            'type': 'string',
        },
        {
            'is_fk': False,
            'is_index': False,
            'is_nullable': False,
            'is_unique': False,
            'is_unsigned': False,
            'name': 'note',
            'options': ['string'],
            'precision': None,
            'raw_type': 'string',
            'scale': None,
            'size': 255,
            'type': 'string',
        },
        {
            'is_fk': False,
            'is_index': False,
            'is_nullable': False,
            'is_unique': False,
            'is_unsigned': False,
            'name': 'has_active',
            'options': ['boolean'],
            'precision': None,
            'raw_type': 'boolean',
            'scale': None,
            'size': None,
            'type': 'boolean',
        },
    ]
    
    
    
    generate_resource(
        full_path="/Users/dorian/PHPProjects/api.app1.com",
        namespace="SHARED",
        version_api="V1",
        project_name="app1",
        singular_name="Ability",
        plural_name="Abilities",
        singular_name_camel="ability",
        plural_name_camel="abilities",
        singular_name_kebab="ability",
        plural_name_kebab="abilities",
        singular_name_snake="ability",
        plural_name_snake="abilities",
        columns=columns,
    )