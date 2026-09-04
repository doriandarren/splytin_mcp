import os
from gen.helpers.helper_print import print_message, GREEN, CYAN


def format_relation_fields(columns):
        
    content = ''
    
    for column in columns:
        if column["is_fk"]:
            content += f"""    // public function {column["relationship_name"]}(): BelongsTo
    // {{\n"""
            content += f"""    //     return $this->belongsTo({column["related_model"]}::class, '{column["relationship_column"]}', 'id');"""
            content += f"""
    // }}\n\n"""
    
    
    return content



def format_relation_uses(columns):
    content = ''
    
    for column in columns:
        if column["is_fk"]:
            content += f"""use Illuminate\\Database\\Eloquent\\Relations\\BelongsTo; """
            
    return content
    






def generate_model_file(
    full_path, 
    namespace,
    singular_name, 
    plural_name, 
    plural_name_snake,
    columns
):
    """
    Genera el archivo
    """
    
    folder_path = os.path.join(full_path, "app", "Models", namespace, plural_name)
    file_path = os.path.join(folder_path, f"{singular_name}.php")

    os.makedirs(folder_path, exist_ok=True)
    

    content = f"""<?php

namespace App\\Models\\{namespace}\\{plural_name};

use Illuminate\\Database\\Eloquent\\Factories\\HasFactory;
use Illuminate\\Database\\Eloquent\\Model;
use Illuminate\\Database\\Eloquent\\Builder;
use App\\Http\\Filters\\API\\V1\\QueryFilter;
{format_relation_uses(columns)}

class {singular_name} extends Model
{{
    use HasFactory;
    // use SoftDeletes;

    protected $connection = '{namespace.lower()}';
    protected $table = '{plural_name_snake}';
    
    
"""

    content += f"""    protected $fillable = [
        {', \n        '.join([f"'{column["name"]}'" for column in columns])}
    ];

"""
    
    content += f"""
    /***********************
    * Scope Filter
    ***********************/
    public function scopeFilter(Builder $builder, QueryFilter $filters)
    {{
        return $filters->apply($builder);
    }}
    

    /***********************
    * RELATIONS
    ***********************/
    
{format_relation_fields(columns)}    

    // TODO add relation tables
    // public function classrelacion()
    // {{
    //     return $this->hasMany(Relation::class, 'relacion_id', 'id');
    // }}
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
    
    
    generate_model_file(
        full_path="/Users/dorian/PHPProjects/api.app1.com",
        namespace="SHARED",
        singular_name="Ability",
        plural_name="Abilities",
        plural_name_snake="abilities",
        columns=columns,
    )