import os
from gen.helpers.helper_print import print_message, GREEN, CYAN



def generate_controller_index_file(
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

    folder_path = os.path.join(full_path, "app", "Http", "Controllers", namespace, version_api, plural_name)
    file_path = os.path.join(folder_path, f'{singular_name}IndexController.php')

    os.makedirs(folder_path, exist_ok=True)

    content = f'''<?php

namespace App\\Http\\Controllers\\{namespace}\\{version_api}\\{plural_name};

use App\\Http\\Controllers\\Controller;
use Illuminate\\Support\\Facades\\Auth;
use Illuminate\\Http\\JsonResponse;
use App\\Http\\Filters\\{namespace}\\{version_api}\\{plural_name}\\{singular_name}Filter;
use App\\Http\\Resources\\{namespace}\\{version_api}\\{plural_name}\\{singular_name}Resource;
use App\\Services\\{namespace}\\{version_api}\\{plural_name}\\{singular_name}Service;



class {singular_name}IndexController extends Controller
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
    * @return JsonResponse
    */
    public function __invoke({singular_name}Filter $filter): JsonResponse
    {{
        
        if ($this->isAdmin(Auth::user()->roles)) {{
            $data = $this->service->index($filter);
        }} elseif ($this->isManager(Auth::user()->roles)) {{
            $data = $this->service->indexByRoleManager($filter);
        }} elseif ($this->isUser(Auth::user()->roles)) {{
            $data = $this->service->indexByRoleUser($filter);
        }}
        
        return $this->respondWithPaginatedData(
            '{singular_name} index',
            {singular_name}Resource::collection($data),
            $data
        );
        
    }}
}}
'''

    try:
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)
