import os
from gen.helpers.helper_print import print_message, GREEN, CYAN



def generate_service_file(
    full_path,
    namespace,
    version_api,
    folder_group,
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

    folder_path = os.path.join(full_path, "app", "Services", namespace, version_api, plural_name)
    file_path = os.path.join(folder_path, f"{singular_name}Service.php")

    os.makedirs(folder_path, exist_ok=True)
    
    # Obtener los nombres de las columnas dinámicamente
    column_names = [column["name"] for column in columns]
    

    content = f"""<?php

namespace App\\Services\\{namespace}\\{version_api}\\{plural_name};

use App\\Enums\\EnumApiSetup;
use App\\Http\\Filters\\{namespace}\\{version_api}\\{plural_name}\\{singular_name}Filter;
use App\\Models\\{namespace}\\{plural_name}\\{singular_name};

class {singular_name}Service
{{
    const WITH = [];
   
    /**
    * List by Admin
    * @return mixed
    */
    public function index({singular_name}Filter $filter)
    {{
        $perPage = request()->integer('perPage', EnumApiSetup::QUERY_DEFAULT_LIMIT);
        $perPage = max(1, min($perPage, EnumApiSetup::QUERY_MAX_LIMIT));
        
        return $filter
            ->apply({singular_name}::query())
            ->paginate($perPage);
    }}


    /**
    * List by Manager
    * @return mixed
    */
    public function indexByRoleManager({singular_name}Filter $filter)
    {{
        $perPage = request()->integer('perPage', EnumApiSetup::QUERY_DEFAULT_LIMIT);
        $perPage = max(1, min($perPage, EnumApiSetup::QUERY_MAX_LIMIT));
        
        return $filter
            ->apply({singular_name}::query())
            ->paginate($perPage);
    }}

    /**
    * List by User
    * @return mixed
    */
    public function indexByRoleUser({singular_name}Filter $filter)
    {{
        $perPage = request()->integer('perPage', EnumApiSetup::QUERY_DEFAULT_LIMIT);
        $perPage = max(1, min($perPage, EnumApiSetup::QUERY_MAX_LIMIT));
        
        return $filter
            ->apply({singular_name}::query())
            ->paginate($perPage);
    }} 
        
"""


    content += f"""
    /**
    * Show by Admin
	* @param $id
	* @return mixed
	*/
    public function show($id): mixed
    {{
        return {singular_name}::where('id', $id)
                            ->first();
    }}
    
    
    /**
    * Show by Manager
	* @param $id
	* @return mixed
	*/
    public function showByRoleManager($id): mixed
    {{
        return {singular_name}::where('id', $id)
                            ->first();
    }}
    
    
    /**
    * Show by User
	* @param $id
	* @return mixed
	*/
    public function showByRoleUser($id): mixed
    {{
        return {singular_name}::where('id', $id)
                            ->first();
    }}


    /**
    * Store
    * @param $data
    * @return {singular_name}
    */
    public function store($data): {singular_name}
    {{
        $objNew = new {singular_name}();
"""

    # Agregar las columnas dinámicamente en el método `store`
    for column in column_names:
        content += f"        $objNew->{column} = $data->{column};\n"

    content += f"""
        $objNew->save();
        return $objNew;
    }}
    

    /**
    * Update
    * @param $id
    * @param $data
    * @return {singular_name}
    */
    public function update($id, $data): mixed
    {{
    
        if(is_array($data)){{
			$obj = json_decode(json_encode($data), FALSE);
		}}else{{
			$obj = $data;
		}}
        
        $objOld = {singular_name}::query()->where('id', $id)->first();

"""

    # Separar las columnas dinámicamente en el método `update`
    for column in column_names:
        content += f"""        if (isset($obj->{column})) {{
            if ($obj->{column} != '' && !empty($obj->{column})) {{
                $objOld->{column} = $obj->{column};
            }}
        }}

"""
    content += f"""
        $objOld->save();
        return $objOld;
    }}


    /**
    * Destroy
    * @param $id
    * @return bool
    */
    public function destroy($id): bool
    {{
        return (bool) {singular_name}::query()->where('id', $id)->delete();
    }}


    /**
    * Set {singular_name}
"""

    # Agregar los `@param` dinámicos para cada columna
    for column in column_names:
        content += f"    * @param ${column}\n"
        
    param_content = ""
    
    for column in column_names:
        param_content += f"        ${column},\n"
    

    content += f"""    * @return {singular_name}
    */
    public function set{singular_name}(
{param_content}
    ): {singular_name}
    {{
        $obj = new {singular_name}();
"""

    # Agregar las columnas dinámicamente en el método `set`
    for column in column_names:
        content += f"        $obj->{column} = ${column};\n"

    content += f"""
        return $obj;
    }}
}}
"""

    try:
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)
