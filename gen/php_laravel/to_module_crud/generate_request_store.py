import os
from gen.helpers.helper_print import print_message, GREEN, CYAN



# Función auxiliar para generar reglas de validación
def generate_request_validation_rules(
    columns,
    singular_name,
    singular_name_camel,
    singular_name_snake,
    plural_name_snake
):
    validation_rules = ""

    rules_by_type = {
        "string": ["required", "string"],
        "text": ["required", "string"],
        "integer": ["required", "integer"],
        "float": ["required", "numeric"],
        "decimal": ["required", "numeric"],
        "boolean": ["required", "boolean"],
        "date": ["required", "date"],
        "datetime": ["required", "date"],
        "timestamp": ["required", "date"],
        "email": ["required", "email"],
    }

    for index, column in enumerate(columns):

        column_type = column["type"]

        # ---------------------------------
        # Reglas base
        # ---------------------------------

        if column_type == "fk":
            rules = [
                "required",
                "integer",
                f"exists:{column['related_table']},id",
            ]

        else:
            rules = rules_by_type.get(
                column_type,
                ["required"]
            ).copy()

            # Tamaño
            if (
                column_type in {"string", "email"}
                and column.get("size")
            ):
                rules.append(
                    f"max:{column['size']}"
                )

        # ---------------------------------
        # Nullable
        # ---------------------------------
        if column.get("is_nullable"):
            rules[0] = "nullable"


        # ---------------------------------
        # Generar array PHP
        # ---------------------------------
        validation_rules += (
            f"            '{column['name']}' => [\n"
        )

        for rule in rules:
            validation_rules += (
                f"                '{rule}',\n"
            )


        # ---------------------------------
        # Unique
        # ---------------------------------
        if column.get("is_unique"):
            validation_rules += (
            f"                'unique:{plural_name_snake},{column['name']}',\n"
        )

        validation_rules += "            ],"

        # Salto de línea excepto último
        if index != len(columns) - 1:
            validation_rules += "\n"

    return validation_rules







def generate_request_store(
    full_path,
    namespace,
    version_api,
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

    folder_path = os.path.join(full_path, "app", "Http", "Requests", namespace, version_api, plural_name)
    file_path = os.path.join(folder_path, f"Store{singular_name}Request.php")

    os.makedirs(folder_path, exist_ok=True)

    content = f"""<?php

namespace App\\Http\\Requests\\{namespace}\\{version_api}\\{plural_name};

use Illuminate\\Contracts\\Validation\\Validator;
use Illuminate\\Contracts\\Validation\\ValidationRule;
use Illuminate\\Foundation\\Http\\FormRequest;
use Illuminate\\Http\\Exceptions\\HttpResponseException;
use App\\Traits\\ApiResponses;

class Store{singular_name}Request extends FormRequest
{{
    
    use ApiResponses;
    
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
{generate_request_validation_rules(
    columns, 
    singular_name, 
    singular_name_camel, 
    singular_name_snake, 
    plural_name_snake
)}            
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
                $validator->errors(),
                422
            )
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



