import os

def create_controller_structure(
    full_path,
    path_controller
):
    """
    Crea la estructura de carpetas 'full_path/app/path_controller' en la ruta especificada.
    """
    # Crear la ruta completa full_path/app/path_controller
    controller_folder_path = os.path.join(full_path, 'app', path_controller)

    if not os.path.exists(controller_folder_path):
        os.makedirs(controller_folder_path)
        print(f"Estructura de carpetas '{controller_folder_path}' creada.")

    return controller_folder_path


def generate_controller_show_file(
    full_path, 
    namespace, 
    version_api,
    singular_name, 
    plural_name,
    singular_name_kebab, 
    plural_name_kebab, 
    singular_name_snake, 
    plural_name_snake, 
    columns
):
    """
    Genera un archivo de controlador PHP basado en los nombres proporcionados y crea la estructura app/path_controller dentro de base_ruta.
    """
    
    path_controller = "Http/Controllers/" + namespace + "/" + version_api + "/" + plural_name
    
    # Crear la estructura de carpetas llamando a create_controller_structure
    controller_folder_path = create_controller_structure(full_path, path_controller)

    # Nombre del archivo PHP será igual a singular_name
    file_name = f'{singular_name}ShowController.php'
    controller_file_path = os.path.join(controller_folder_path, file_name)

    # Contenido del archivo PHP del controlador
    controller_content = f"""<?php

namespace App\\Http\\Controllers\\{namespace}\\{version_api}\\{plural_name};

use Illuminate\\Support\\Facades\\Auth;
use Illuminate\\Http\\JsonResponse;
use App\\Http\\Controllers\\Controller;
use App\\Models\\{namespace}\\{plural_name}\\{singular_name};
use App\\Services\\{namespace}\\{version_api}\\{plural_name}\\{singular_name}Service;
use App\\Http\\Resources\\{namespace}\\{version_api}\\{plural_name}\\{singular_name}Resource;

class {singular_name}ShowController extends Controller
{{
    /**
     * Construct
     *
     * @param {singular_name}Service $service
     */
    public function __construct(
        private {singular_name}Service $service
    ) {{}}


    /**
    * @header Authorization Bearer TOKEN 
    * @urlParam id required The ID of the table.
    *
    * @param {singular_name} ${singular_name_snake}
    * @return JsonResponse
    */
    public function __invoke({singular_name} ${singular_name_snake}): JsonResponse
    {{
        if($this->isAdmin(Auth::user()->roles)){{
            $data = $this->service->show(${singular_name_snake}->id);
        }} else if($this->isManager(Auth::user()->roles)){{
            $data = $this->service->showByRoleManager(${singular_name_snake}->id);
        }} else {{
            $data = $this->service->showByRoleUser(${singular_name_snake}->id);
        }}
        
        return $this->respondWithData(
            '{singular_name} show',
            new {singular_name}Resource($data)
        );
        
    }}
}}
"""

    # Escribir el archivo PHP con el contenido del controlador
    try:
        with open(controller_file_path, 'w') as controller_file:
            controller_file.write(controller_content)
            print(f"Archivo PHP controlador '{file_name}' creado en: {controller_folder_path}")
    except Exception as e:
        print(f"Error al crear el archivo PHP del controlador '{file_name}': {e}")
