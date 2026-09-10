import os
from gen.helpers.helper_print import print_message, GREEN, CYAN


def create_body_param_comments(columns):
    # Crear comentarios dinámicos para @bodyParam
    body_param_comments = ""
    for i, column in enumerate(columns):
        body_param_comments += f"    * @bodyParam {column['name']} string required"
        if i < len(columns) - 1:
            body_param_comments += "\n"
    return body_param_comments



def find_namespace(namespace, version_api, folder_group, plural_name):
    
    text = f"namespace App\\Http\\Controllers\\{namespace}\\{version_api}\\{plural_name};"
    
    if folder_group:
        text = f"namespace App\\Http\\Controllers\\{namespace}\\{version_api}\\{folder_group}\\{plural_name};"
    
    return text




def generate_controller_update_file(
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
    Genera el archivo
    """
    
    folder_parts = [
        full_path,
        "app",
        "Http",
        "Controllers",
        namespace,
        version_api,
    ]

    if folder_group:
        folder_parts.append(folder_group)

    folder_parts.append(plural_name)

    folder_path = os.path.join(*folder_parts)
    file_path = os.path.join(folder_path, f"{singular_name}UpdateController.php")

    os.makedirs(folder_path, exist_ok=True)

    content = f"""<?php

{find_namespace(namespace, version_api, folder_group, plural_name)}

use App\\Http\\Controllers\\Api\\V1\\ApiController;
use Illuminate\\Support\\Facades\\Auth;
use Illuminate\\Http\\JsonResponse;
use App\\Models\\{namespace}\\{plural_name}\\{singular_name};
use App\\Services\\{namespace}\\{version_api}\\{plural_name}\\{singular_name}Service;
use App\\Http\\Requests\\{namespace}\\{version_api}\\{plural_name}\\Update{singular_name}Request;
use App\\Http\\Resources\\{namespace}\\{version_api}\\{plural_name}\\{singular_name}Resource;

class {singular_name}UpdateController extends ApiController
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
{create_body_param_comments(columns)}
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

    try:
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)
