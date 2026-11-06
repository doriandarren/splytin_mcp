
from gen.helpers.helper_file import HelperFile
from gen.php_laravel.to_module_crud.helpers.helper_laravel_controller import HelperLaravelController


class LaravelCrudControllerStore:

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

        body_param_comments = HelperLaravelController.create_body_param_comments(
            columns
        )

        formatted_attributes = HelperLaravelController.format_attributes(
            columns,
            singular_name,
            singular_name_camel
        )

        first_letter_lower = HelperLaravelController.first_letter_lower(
            singular_name
        )

        content = f"""<?php

{controller_namespace}

use App\\Http\\Controllers\\API\\V1\\ApiController;
use Illuminate\\Support\\Facades\\Auth;
use Illuminate\\Http\\JsonResponse;
{path_use_model}
use App\\Http\\Requests\\{version_api}\\{plural_name}\\Store{singular_name}Request;
use App\\Policies\\{version_api}\\{plural_name}\\{singular_name}Policy;
use App\\Services\\{version_api}\\{plural_name}\\{singular_name}Service;
use App\\Http\\Resources\\{version_api}\\{plural_name}\\{singular_name}Resource;

class {singular_name}StoreController extends ApiController
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
    *
{body_param_comments}
    *
    * @param Store{singular_name}Request $request
    * @return JsonResponse
    */
    public function __invoke(Store{singular_name}Request $request): JsonResponse
    {{
        $this->isAble('store', {singular_name}::class);
        $attributes = $request->mappedAttributes();

{formatted_attributes}

        if ($this->isAdmin(Auth::user()->roles)) {{
            // By Admin
            $data = $this->service->store(${first_letter_lower});
        }} elseif ($this->isManager(Auth::user()->roles)) {{
            // By Manager
            $data = $this->service->store(${first_letter_lower});
        }} else {{
            // By User
            $data = $this->service->store(${first_letter_lower});
        }}

        return $this->respondWithData(
            '{singular_name} created',
            new {singular_name}Resource($data)
        );
    }}
}}
"""

        # Crear el archivo
        HelperFile.write(
            folder_path=folder_path,
            file_name=f"{singular_name}StoreController.php",
            content=content
        )
