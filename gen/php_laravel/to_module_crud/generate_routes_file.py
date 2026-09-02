import os
from gen.helpers.helper_print import print_message, GREEN, CYAN

def generate_routes_file(
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

    folder_path = os.path.join(full_path, "routes", namespace, version_api)
    file_path = os.path.join(folder_path, f"{plural_name_snake}.php")

    os.makedirs(folder_path, exist_ok=True)

    content = f"""<?php

use Illuminate\\Support\\Facades\\Route;
use App\\Enums\\EnumAbilitySuffix;
use App\\Http\\Controllers\\{namespace}\\{version_api}\\{plural_name}\\{singular_name}IndexController;
use App\\Http\\Controllers\\{namespace}\\{version_api}\\{plural_name}\\{singular_name}ShowController;
use App\\Http\\Controllers\\{namespace}\\{version_api}\\{plural_name}\\{singular_name}StoreController;
use App\\Http\\Controllers\\{namespace}\\{version_api}\\{plural_name}\\{singular_name}UpdateController;
use App\\Http\\Controllers\\{namespace}\\{version_api}\\{plural_name}\\{singular_name}DestroyController;


/**
* {plural_name}
*/
Route::prefix('{plural_name_kebab}')
    ->middleware('auth:sanctum')
    ->group(function () {{

        Route::get('/', {singular_name}IndexController::class)
            ->middleware('abilities:{plural_name_snake}' . EnumAbilitySuffix::INDEX);

        Route::get('/{{{singular_name_snake}:id}}', {singular_name}ShowController::class)
            ->middleware('abilities:{plural_name_snake}' . EnumAbilitySuffix::SHOW);

        Route::post('/', {singular_name}StoreController::class)
            ->middleware('abilities:{plural_name_snake}' . EnumAbilitySuffix::STORE);

        Route::patch('/{{{singular_name_snake}:id}}', {singular_name}UpdateController::class)
            ->middleware('abilities:{plural_name_snake}' . EnumAbilitySuffix::UPDATE);

        Route::delete('/{{{singular_name_snake}:id}}', {singular_name}DestroyController::class)
            ->middleware('abilities:{plural_name_snake}' . EnumAbilitySuffix::DESTROY);
        
}});


"""

    try:
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)

