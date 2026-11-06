
from gen.helpers.helper_file import HelperFile
from gen.php_laravel.to_module_crud.helpers.helper_laravel_controller import HelperLaravelController


class LaravelCrudControllerIndex:

    def invoke(
        self,
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
        Genera el archivo.
        """

        folder_path = HelperLaravelController().get_folder_path(
            full_path,
            namespace,
            version_api,
            folder_group,
            plural_name
        )

        controller_namespace = HelperLaravelController.get_namespace(
            namespace,
            version_api,
            folder_group,
            plural_name
        )

        path_use_model = HelperLaravelController.get_model_import(
            namespace,
            plural_name,
            singular_name
        )

        content = f'''<?php

{controller_namespace}

use App\\Http\\Controllers\\API\\V1\\ApiController;
use Illuminate\\Support\\Facades\\Auth;
use Illuminate\\Http\\JsonResponse;
{path_use_model}
use App\\Http\\Filters\\{version_api}\\{plural_name}\\{singular_name}Filter;
use App\\Policies\\{version_api}\\{plural_name}\\{singular_name}Policy;
use App\\Http\\Resources\\{version_api}\\{plural_name}\\{singular_name}Resource;
use App\\Services\\{version_api}\\{plural_name}\\{singular_name}Service;



class {singular_name}IndexController extends ApiController
{{
    protected $policyClass = {singular_name}Policy::class;
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
        $this->isAble('index', {singular_name}::class);
        if ($this->isAdmin(Auth::user()->roles)) {{
            // By Admin
            $data = $this->service->index($filter);
        }} elseif ($this->isManager(Auth::user()->roles)) {{
            // By Manager
            $data = $this->service->indexByRoleManager($filter);
        }} elseif ($this->isUser(Auth::user()->roles)) {{
            // By User
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

        # Crear el archivo
        HelperFile.write(
            folder_path=folder_path,
            file_name=f"{singular_name}IndexController.php",
            content=content
        )
