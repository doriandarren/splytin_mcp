import os

def create_controller_structure(base_ruta, path_controller):
    """
    Crea la estructura de carpetas 'base_ruta/app/path_controller' en la ruta especificada.
    """
    # Crear la ruta completa base_ruta/app/path_controller
    controller_folder_path = os.path.join(base_ruta, 'app', path_controller)

    if not os.path.exists(controller_folder_path):
        os.makedirs(controller_folder_path)
        print(f"Estructura de carpetas '{controller_folder_path}' creada.")

    return controller_folder_path




def generate_controller_update_file(
    base_ruta,
    namespace,
    version_api,
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
    Genera el archivo de controlador PHP para el método Update.
    """
    
    path_controller = "Http/Controllers/" + namespace + "/" + version_api + "/" + plural_name
    
    # Crear la estructura de carpetas llamando a create_controller_structure
    controller_folder_path = create_controller_structure(base_ruta, path_controller)

    # Nombre del archivo PHP será igual a singular_name
    file_name = f'{singular_name}UpdateController.php'
    controller_file_path = os.path.join(controller_folder_path, file_name)

    # Crear comentarios dinámicos para @bodyParam
    body_param_comments = ""
    for i, column in enumerate(columns):
        body_param_comments += f"    * @bodyParam {column['name']} string required"
        if i < len(columns) - 1:
            body_param_comments += "\n"

    # Contenido del archivo PHP del controlador adaptado
    controller_content = f"""<?php

namespace App\\Http\\Controllers\\{namespace}\\{version_api}\\{plural_name};

use App\\Http\\Controllers\\Controller;
use Illuminate\\Support\\Facades\\Auth;
use Illuminate\\Http\\JsonResponse;
use App\\Models\\{namespace}\\{plural_name}\\{singular_name};
use App\\Services\\{namespace}\\{version_api}\\{plural_name}\\{singular_name}Service;
use App\\Http\\Requests\\{namespace}\\{version_api}\\{plural_name}\\Update{singular_name}Request;
use App\\Http\\Resources\\{namespace}\\{version_api}\\{plural_name}\\{singular_name}Resource;

class {singular_name}UpdateController extends Controller
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
{body_param_comments}
    *
    * @param Update{singular_name}Request $request
    * @param {singular_name} ${singular_name_camel}
    * @return JsonResponse
    */
    public function __invoke(
        Update{singular_name}Request $request, 
        {singular_name} ${singular_name_camel}
    ): JsonResponse
    {{
        
        $attributes = $request->mappedAttributes();

        if($this->isAdmin(Auth::user()->roles)){{
            
            // By Admin
            $data = $this->service->update(
                ${singular_name_camel}->id,
                $attributes
            );

        }}elseif($this->isManager(Auth::user()->roles)){{
            
            // By Manager
            $data = $this->service->update(
                ${singular_name_camel}->id,
                $attributes
            );

        }}else{{

             // By User
            $data = $this->service->update(
                ${singular_name_camel}->id,
                $attributes
            );

        }}
        
        
        return $this->respondWithData(
            '{singular_name} updated',
            new {singular_name}Resource($data)
        );

    }}

}}"""

    # Escribir el archivo PHP con el contenido del controlador
    try:
        with open(controller_file_path, 'w') as controller_file:
            controller_file.write(controller_content)
            print(f"Archivo PHP controlador '{file_name}' creado en: {controller_folder_path}")
    except Exception as e:
        print(f"Error al crear el archivo de controlador '{file_name}': {e}")

