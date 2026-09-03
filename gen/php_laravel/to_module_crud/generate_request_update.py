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
        "string": ["sometimes", "string"],
        "text": ["sometimes", "string"],
        "integer": ["sometimes", "integer"],
        "float": ["sometimes", "numeric"],
        "decimal": ["sometimes", "numeric"],
        "boolean": ["sometimes", "boolean"],
        "date": ["sometimes", "date"],
        "datetime": ["sometimes", "date"],
        "timestamp": ["sometimes", "date"],
        "email": ["sometimes", "email"],
    }

    for index, column in enumerate(columns):

        column_type = column["type"]

        # ---------------------------------
        # Reglas base
        # ---------------------------------

        if column_type == "fk":
            rules = [
                "sometimes",
                "integer",
                f"exists:{column['related_table']},id",
            ]

        else:
            rules = rules_by_type.get(
                column_type,
                ["sometimes"]
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
            f"            'data.attributes.{column['name']}' => [\n"
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
                f"                Rule::unique("
                f"'{plural_name_snake}', "
                f"'{column['name']}'"
                f")->ignore("
                f"$this->route('{singular_name_snake}')"
                f"),\n"
            )

        validation_rules += "            ],"

        # Salto de línea excepto último
        if index != len(columns) - 1:
            validation_rules += "\n"

    return validation_rules






def create_attribute_map(columns):

    lines = []

    for column in columns:
        name = column["name"]

        if column["type"] == "fk":
            lines.append(
                f"        'data.relationships.{column['relationship_name']}.data.id' => '{name}',"
            )
        else:
            lines.append(
                f"        'data.attributes.{name}' => '{name}',"
            )

    content = """protected array $attributeMap = [
"""
    content += "\n".join(lines)
    content += """
    ];"""

    return content





def generate_request_update(
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
    file_path = os.path.join(folder_path, f"Update{singular_name}Request.php")

    os.makedirs(folder_path, exist_ok=True)

    content = f"""<?php

namespace App\\Http\\Requests\\{namespace}\\{version_api}\\{plural_name};

use App\\Http\\Requests\\BaseApiRequest;
use Illuminate\\Contracts\\Validation\\ValidationRule;
use Illuminate\\Validation\\Rule;
use Illuminate\\Http\\Exceptions\\HttpResponseException;
use App\\Traits\\ApiResponses;

class Update{singular_name}Request extends BaseApiRequest
{{
    
    use ApiResponses;

{create_attribute_map(columns)}
    
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
{generate_request_validation_rules(columns, singular_name, singular_name_camel, singular_name_snake, plural_name_snake )}
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
