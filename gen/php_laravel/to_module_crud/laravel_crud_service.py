
from helpers.helper_file import HelperFile
from gen.php_laravel.to_module_crud.helpers.helper_laravel_controller import HelperLaravelController
from gen.php_laravel.to_module_crud.helpers.helper_laravel_service import HelperLaravelService


class LaravelCrudService:

    def invoke(
        self,
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
        Genera el archivo.
        """

        folder_path = HelperLaravelService.get_folder_path(
            full_path,
            version_api,
            plural_name
        )

        path_use_model = HelperLaravelController.get_model_import(
            namespace,
            plural_name,
            singular_name
        )

        store_columns = HelperLaravelService.format_store_columns(
            columns
        )

        update_columns = HelperLaravelService.format_update_columns(
            columns
        )

        set_params = HelperLaravelService.format_set_params(
            columns
        )

        set_doc_params = HelperLaravelService.format_set_doc_params(
            columns
        )

        set_columns = HelperLaravelService.format_set_columns(
            columns
        )

        content = f"""<?php

namespace App\\Services\\{version_api}\\{plural_name};

use App\\Enums\\EnumApiSetup;
use App\\Http\\Filters\\{version_api}\\{plural_name}\\{singular_name}Filter;
{path_use_model}

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
            ->orderBy('id', 'desc')
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
            ->orderBy('id', 'desc')
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
            ->orderBy('id', 'desc')
            ->paginate($perPage);
    }}

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
{store_columns}
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

{update_columns}
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
{set_doc_params}    * @return {singular_name}
    */
    public function set{singular_name}(
{set_params}
    ): {singular_name}
    {{
        $obj = new {singular_name}();
{set_columns}
        return $obj;
    }}
}}
"""

        # Crear el archivo
        HelperFile.write(
            folder_path=folder_path,
            file_name=f"{singular_name}Service.php",
            content=content
        )
