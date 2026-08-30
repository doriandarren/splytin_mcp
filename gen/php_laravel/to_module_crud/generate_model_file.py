import os
from gen.helpers.helper_print import print_message, GREEN, CYAN

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

