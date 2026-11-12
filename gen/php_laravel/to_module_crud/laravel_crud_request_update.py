from helpers.helper_file import HelperFile
from gen.php_laravel.to_module_crud.helpers.helper_laravel_request import HelperLaravelRequest


class LaravelCrudRequestUpdate:

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

        folder_path = HelperLaravelRequest.get_folder_path(
            full_path,
            version_api,
            plural_name
        )

        attribute_map = HelperLaravelRequest.create_attribute_map(
            columns
        )

        validation_rules = HelperLaravelRequest.generate_update_validation_rules(
            columns,
            singular_name,
            singular_name_camel,
            singular_name_snake,
            plural_name_snake
        )

        content = f"""<?php

namespace App\\Http\\Requests\\{version_api}\\{plural_name};

use App\\Http\\Requests\\BaseApiRequest;
use Illuminate\\Contracts\\Validation\\Validator;
use Illuminate\\Contracts\\Validation\\ValidationRule;
use Illuminate\\Validation\\Rule;
use Illuminate\\Http\\Exceptions\\HttpResponseException;
use App\\Traits\\ApiResponses;

class Update{singular_name}Request extends BaseApiRequest
{{
    use ApiResponses;

    /**
    * Maps JSON:API request paths to model/database attributes.
    */
{attribute_map}
    /**
     * Determine if the user is authorized to make this request.
     */
    public function authorize(): bool
    {{
        return true;
    }}

    /**
     * Get the validation rules that apply to the request.
     *
     * @return array<string, ValidationRule|array<mixed>|string>
     */
    public function rules(): array
    {{
        return [
{validation_rules}
        ];
    }}
    /**
     * Handle a failed validation attempt.
     *
     * @param Validator $validator
     * @return void
     */
    protected function failedValidation(Validator $validator)
    {{
        throw new HttpResponseException(
            $this->respondWithError(
                'Validation error',
                $validator->errors()->toArray(),
                422
            )
        );
    }}
}}

"""

        # Crear el archivo
        HelperFile.write(
            folder_path=folder_path,
            file_name=f"Update{singular_name}Request.php",
            content=content
        )
