from gen.helpers.helper_file import HelperFile
from gen.php_laravel.to_module_crud.helpers.helper_laravel_route import HelperLaravelRoute


class LaravelCrudRoute:

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
        Genera el archivo de rutas del CRUD
        y actualiza routes/api.php.
        """

        folder_path = HelperLaravelRoute.get_folder_path(
            full_path,
            namespace,
            version_api
        )

        controller_imports = HelperLaravelRoute.get_controller_imports(
            namespace,
            version_api,
            folder_group,
            plural_name,
            singular_name
        )

        content = f"""<?php

use Illuminate\\Support\\Facades\\Route;
{controller_imports}


/**
* {plural_name}
*/
Route::prefix('{plural_name_kebab}')
    ->middleware('auth:sanctum')
    ->name('{plural_name_kebab}.')
    ->group(function () {{

        Route::get('/', {singular_name}IndexController::class)
            ->name('index');

        Route::get('/{{{singular_name_snake}:id}}', {singular_name}ShowController::class)
            ->name('show');

        Route::post('/', {singular_name}StoreController::class)
            ->name('store');

        Route::patch('/{{{singular_name_snake}:id}}', {singular_name}UpdateController::class)
            ->name('update');

        Route::delete('/{{{singular_name_snake}:id}}', {singular_name}DestroyController::class)
            ->name('destroy');
    }});

"""

        # ---------------------------------
        # Crear archivo de rutas
        # ---------------------------------

        HelperFile.write(
            folder_path=folder_path,
            file_name=f"{plural_name_snake}.php",
            content=content
        )

        # ---------------------------------
        # Actualizar routes/api.php
        # ---------------------------------

        HelperLaravelRoute.update_route_api_php(
            full_path,
            namespace,
            version_api,
            plural_name_snake
        )
