import os
from gen.helpers.helper_print import print_message, GREEN, CYAN


def find_namespace(namespace, version_api, folder_group, plural_name):
    
    text = f"namespace App\\Http\\Controllers\\{namespace}\\{version_api}\\{plural_name};"
    
    if folder_group:
        text = f"namespace App\\Http\\Controllers\\{namespace}\\{version_api}\\{folder_group}\\{plural_name};"
    
    return text



def generate_controller_show_file(
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
    file_path = os.path.join(folder_path, f"{singular_name}ShowController.php")

    os.makedirs(folder_path, exist_ok=True)

    content = f"""<?php

{find_namespace(namespace, version_api, folder_group, plural_name)}

use App\\Http\\Controllers\\Api\\V1\\ApiController;
use Illuminate\\Support\\Facades\\Auth;
use Illuminate\\Http\\JsonResponse;
use App\\Models\\{namespace}\\{plural_name}\\{singular_name};
use App\\Services\\{namespace}\\{version_api}\\{plural_name}\\{singular_name}Service;
use App\\Http\\Resources\\{namespace}\\{version_api}\\{plural_name}\\{singular_name}Resource;

class {singular_name}ShowController extends ApiController
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

    try:
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)
