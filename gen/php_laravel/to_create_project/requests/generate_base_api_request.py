import os
from gen.helpers.helper_print import print_message, GREEN, CYAN

def generate_base_api_request(full_path):
    """
    Genera el archivo
    """

    folder_path = os.path.join(full_path, "app", "Http", "Requests")
    file_path = os.path.join(folder_path, "BaseApiRequest.php")

    os.makedirs(folder_path, exist_ok=True)

    content = r"""<?php

namespace App\Http\Requests;

use Illuminate\Foundation\Http\FormRequest;

class BaseApiRequest extends FormRequest
{
    protected array $attributeMap = [];

    public function mappedAttributes(): array
    {
        $attributes = [];

        foreach ($this->attributeMap as $key => $attribute) {
            if ($this->has($key)) {
                $attributes[$attribute] = $this->input($key);
            }
        }

        return $attributes;
    }
}
"""

    try:
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)
