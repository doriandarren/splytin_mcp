import os
from gen.helpers.helper_print import print_message, GREEN, CYAN


# Función auxiliar para generar reglas de validación
def generate_validation_rules(columns):
    validation_rules = ""

    rules_by_type = {
        "string": "required|string",
        "text": "required|string",
        "integer": "required|integer",
        "float": "required|numeric",
        "decimal": "required|numeric",
        "boolean": "required|boolean",
        "date": "required|date",
        "datetime": "required|date",
        "timestamp": "required|date",
        "email": "required|email",
    }

    for index, column in enumerate(columns):
        column_type = column["type"]

        if column_type == "fk":
            str_value = (
                f"required|integer|exists:{column['related_table']},id"
            )
        else:
            str_value = rules_by_type.get(
                column_type,
                "required"
            )

            # Añadir tamaño si aplica
            if column_type in {"string", "email"} and column.get("size"):
                str_value += f"|max:{column['size']}"

        is_last = index == len(columns) - 1

        validation_rules += (
            f"            '{column['name']}' => '{str_value}',"
        )

        if not is_last:
            validation_rules += "\n"

    return validation_rules






def generate_request_update(
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

    folder_path = os.path.join(full_path, "app", "Http", "Requests", namespace, version_api, plural_name)
    file_path = os.path.join(folder_path, f"Update{singular_name}Request.php")

    os.makedirs(folder_path, exist_ok=True)

    content = f"""<?php

namespace App\\Http\\Requests\\{namespace}\\{version_api}\\{plural_name};

use Illuminate\\Contracts\\Validation\\ValidationRule;
use Illuminate\\Foundation\\Http\\FormRequest;

class Update{singular_name}Request extends FormRequest
{{
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
{generate_validation_rules(columns)}
       ];
    }}
}}

"""


    try:
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)
