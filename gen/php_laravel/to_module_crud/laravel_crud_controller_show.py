
from helpers.helper_file import HelperFile
from gen.php_laravel.to_module_crud.helpers.helper_laravel_controller import HelperLaravelController


class LaravelCrudControllerShow:

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

        folder_path = HelperLaravelController.get_folder_path(
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

        content = f"""<?php

{controller_namespace}

use App\\Http\\Controllers\\API\\V1\\ApiController;
use Illuminate\\Support\\Facades\\Auth;
use Illuminate\\Http\\JsonResponse;
{path_use_model}
use App\\Policies\\{version_api}\\{plural_name}\\{singular_name}Policy;
use App\\Services\\{version_api}\\{plural_name}\\{singular_name}Service;
use App\\Http\\Resources\\{version_api}\\{plural_name}\\{singular_name}Resource;

class {singular_name}ShowController extends ApiController
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
    * @urlParam id required The ID of the table.
    *
    * @param {singular_name} ${singular_name_camel}
    * @return JsonResponse
    */
    public function __invoke({singular_name} ${singular_name_camel}): JsonResponse
    {{
        $this->isAble('show', ${singular_name_camel});
        if($this->isAdmin(Auth::user()->roles)){{
            $data = $this->service->show(${singular_name_camel}->id);
        }} else if($this->isManager(Auth::user()->roles)){{
            $data = $this->service->showByRoleManager(${singular_name_camel}->id);
        }} else {{
            $data = $this->service->showByRoleUser(${singular_name_camel}->id);
        }}
        return $this->respondWithData(
            '{singular_name} show',
            new {singular_name}Resource($data)
        );
    }}
}}
"""

        # Crear el archivo
        HelperFile.write(
            folder_path=folder_path,
            file_name=f"{singular_name}ShowController.php",
            content=content
        )
