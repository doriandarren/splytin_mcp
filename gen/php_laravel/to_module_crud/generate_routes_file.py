import os
from gen.helpers.helper_print import print_message, GREEN, CYAN

def generate_routes_file(
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
    create_routes_file(
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
    )

    update_route_api_php(
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
    )



def find_namespace(namespace, version_api, folder_group, plural_name, singular_name):
    
    text = f"""use App\\Http\\Controllers\\{namespace}\\{version_api}\\{plural_name}\\{singular_name}IndexController;
use App\\Http\\Controllers\\{namespace}\\{version_api}\\{plural_name}\\{singular_name}ShowController;
use App\\Http\\Controllers\\{namespace}\\{version_api}\\{plural_name}\\{singular_name}StoreController;
use App\\Http\\Controllers\\{namespace}\\{version_api}\\{plural_name}\\{singular_name}UpdateController;
use App\\Http\\Controllers\\{namespace}\\{version_api}\\{plural_name}\\{singular_name}DestroyController;"""
    
    if folder_group:
        text = f"""use App\\Http\\Controllers\\{namespace}\\{version_api}\\{folder_group}\\{plural_name}\\{singular_name}IndexController;
use App\\Http\\Controllers\\{namespace}\\{version_api}\\{folder_group}\\{plural_name}\\{singular_name}ShowController;
use App\\Http\\Controllers\\{namespace}\\{version_api}\\{folder_group}\\{plural_name}\\{singular_name}StoreController;
use App\\Http\\Controllers\\{namespace}\\{version_api}\\{folder_group}\\{plural_name}\\{singular_name}UpdateController;
use App\\Http\\Controllers\\{namespace}\\{version_api}\\{folder_group}\\{plural_name}\\{singular_name}DestroyController;"""
    
    return text




def create_routes_file(
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


    folder_path = os.path.join(full_path, "routes", namespace, version_api)
    file_path = os.path.join(folder_path, f"{plural_name_snake}.php")

    os.makedirs(folder_path, exist_ok=True)

    content = f"""<?php

use Illuminate\\Support\\Facades\\Route;
{find_namespace(namespace, version_api, folder_group, plural_name, singular_name)}


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

    try:
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)










def update_route_api_php(
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
    Actualiza el archivo
    """
    main_path = os.path.join(full_path, "routes", "api.php")

    # Verificar si el archivo existe
    if not os.path.exists(main_path):
        print_message(f"Error: {main_path} no existe.", CYAN)
        return

    try:
        # Leer el contenido del archivo
        with open(main_path, "r") as f:
            content = f.read()
        
        
        marker = """    // ..."""
        string_replace = f"require base_path('routes/{namespace}/{version_api}/{plural_name_snake}.php');"
        
        
        if marker not in content:
            print_message(
                f"No se encontró el marcador en {main_path}",
                CYAN,
            )
            print(repr(marker))
            return
        
        
        if string_replace not in content:    
            replacement = f"""    // ...
    {string_replace}"""
    
            # Reemplazos
            content = content.replace(
                marker,
                replacement
            )
            
        

        # Escribir el contenido actualizado
        with open(main_path, "w") as f:
            f.write(content)

        print_message(
            f"{main_path} actualizado correctamente.",
            GREEN
        )

    except Exception as e:
        print_message(
            f"Error al actualizar {main_path}: {e}",
            CYAN
        )


