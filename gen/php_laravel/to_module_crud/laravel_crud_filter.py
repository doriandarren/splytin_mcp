
from gen.helpers.helper_file import HelperFile
from gen.php_laravel.to_module_crud.helpers.helper_laravel_filter import HelperLaravelFilter


class LaravelCrudFilter:

    def invoke(
        self,
        full_path,
        namespace,
        version_api,
        folder_group,
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

        folder_path = HelperLaravelFilter.get_folder_path(
            full_path,
            version_api,
            plural_name
        )

        columns_functions = HelperLaravelFilter.format_columns_function(
            columns
        )

        sortable_columns = "\n".join(
            f"        '{column['name']}',"
            for column in columns
        )

        content = f"""<?php

namespace App\\Http\\Filters\\{version_api}\\{plural_name};

use App\\Http\\Filters\\V1\\QueryFilter;


class {singular_name}Filter extends QueryFilter
{{

    protected $sortable = [
{sortable_columns}
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


{columns_functions}


    public function created_at($value)
    {{
        $dates = explode(',', $value);

        if(count($dates) > 1){{
            return $this->builder->whereBetween('created_at', $dates);
        }}

        return $this->builder->whereDate('created_at', $value);
    }}


    public function updated_at($value)
    {{
        $dates = explode(',', $value);

        if(count($dates) > 1){{
            return $this->builder->whereBetween('updated_at', $dates);
        }}

        return $this->builder->whereDate('updated_at', $value);
    }}

}}
"""

        # Crear el archivo
        HelperFile.write(
            folder_path=folder_path,
            file_name=f"{singular_name}Filter.php",
            content=content
        )
