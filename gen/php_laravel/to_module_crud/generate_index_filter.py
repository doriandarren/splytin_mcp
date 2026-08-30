import os
from gen.helpers.helper_print import print_message, GREEN, CYAN


def format_columns_function(columns):

    content = """
    public function email($value)
    {{
        $likeStr = str_replace('*', '%', $value);
        return $this->builder->where('email', 'like', $likeStr);
    }}

    public function name($value)
    {{
        $likeStr = str_replace('*', '%', $value);
        return $this->builder->where('name', 'like', $likeStr);
    }}
    
    """

    return content



def generate_index_filter(
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

    folder_path = os.path.join(full_path, "app", "Http", "Filters", namespace, version_api, plural_name)
    file_path = os.path.join(folder_path, f"{singular_name}Filter.php")

    os.makedirs(folder_path, exist_ok=True)
    
    
    
    
    

    content = f"""<?php

namespace App\\Http\\Filters\\{namespace}\\{version_api}\\{plural_name};

use App\\Http\\Filters\\API\\V1\\QueryFilter;


class {singular_name}Filter extends QueryFilter
{{

    protected $sortable = [
        'name',
        'email',
        'created_at' => 'created_at',
        'updated_at' => 'updated_at',
    ];


    public function include($value)
    {{
        return $this->builder->with($value);
    }}


    public function id($value)
    {{
        return $this->builder->whereIn('id', explode(',', $value));
    }}


{format_columns_function(columns)}


    public function createdAt($value)
    {{
        $dates = explode(',', $value);

        if(count($dates) > 1){{
            return $this->builder->whereBetween('created_at', $dates);
        }}

        return $this->builder->whereDate('created_at', $value);
    }}


    public function updatedAt($value)
    {{
        $dates = explode(',', $value);

        if(count($dates) > 1){{
            return $this->builder->whereBetween('updated_at', $dates);
        }}

        return $this->builder->whereDate('updated_at', $value);
    }}

}}
"""

    try:
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)
