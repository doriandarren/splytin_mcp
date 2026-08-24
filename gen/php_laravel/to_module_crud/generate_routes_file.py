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
use App\\Http\\Controllers\\{namespace}\\{version_api}\\{plural_name}\\{singular_name}ListController;
use App\\Http\\Controllers\\{namespace}\\{version_api}\\{plural_name}\\{singular_name}ShowController;
use App\\Http\\Controllers\\{namespace}\\{version_api}\\{plural_name}\\{singular_name}StoreController;
use App\\Http\\Controllers\\{namespace}\\{version_api}\\{plural_name}\\{singular_name}UpdateController;
use App\\Http\\Controllers\\{namespace}\\{version_api}\\{plural_name}\\{singular_name}DestroyController;



/**
* {plural_name}
*/
Route::group(['prefix' => '{plural_name_kebab}/'], function () {{

	Route::group(['middleware' => 'auth:sanctum'], function() {{
        
		Route::get('list', [{singular_name}ListController::class, '__invoke'])->middleware('abilities:{plural_name_snake}' . EnumAbilitySuffix::LIST);
		Route::get('show/{{{singular_name_snake}:id}}', [{singular_name}ShowController::class, '__invoke'])->middleware('abilities:{plural_name_snake}' . EnumAbilitySuffix::SHOW);
		Route::post('store', [{singular_name}StoreController::class, '__invoke'])->middleware('abilities:{plural_name_snake}' . EnumAbilitySuffix::STORE);
		Route::put('update/{{{singular_name_snake}:id}}', [{singular_name}UpdateController::class, '__invoke'])->middleware('abilities:{plural_name_snake}' . EnumAbilitySuffix::UPDATE);
		Route::delete('delete/{{{singular_name_snake}:id}}', [{singular_name}DestroyController::class, '__invoke'])->middleware('abilities:{plural_name_snake}' . EnumAbilitySuffix::DESTROY);
		
	}});
}});
"""

    try:
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)