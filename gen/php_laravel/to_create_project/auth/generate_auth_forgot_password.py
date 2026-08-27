import os
from gen.helpers.helper_print import print_message, GREEN, CYAN

def generate_auth_forgot_password(full_path):
    # Forgot Password
    create_forgot_password_request(full_path)
    create_forgot_password(full_path)





def create_forgot_password_request(full_path):
    """
    Genera el archivo
    """

    folder_path = os.path.join(full_path, "app", "Http", "Requests", "API", "V1", "Auth")
    file_path = os.path.join(folder_path, "AuthForgotPasswordRequest.php")

    os.makedirs(folder_path, exist_ok=True)

    content = f'''<?php

namespace App\\Http\\Requests\\API\\V1\\Auth;

use Illuminate\\Contracts\\Validation\\ValidationRule;
use Illuminate\\Foundation\\Http\\FormRequest;

class AuthForgotPasswordRequest extends FormRequest
{{
    /**
     * Determine if the user is authorized to make this request.
     */
    public function authorize(): bool
    {{
        return false;
    }}

    /**
     * Get the validation rules that apply to the request.
     *
     * @return array<string, ValidationRule|array<mixed>|string>
     */
    public function rules(): array
    {{
        return [
            'email' => [
                'required',
                'email',
                'exists:users,email',
            ],
        ];
    }}
}}
'''

    try:
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)
        
   

        


def create_forgot_password(full_path):
    """
    Genera el archivo
    """

    folder_path = os.path.join(full_path, "app", "Http", "Controllers", "API", "V1", "Auth")
    file_path = os.path.join(folder_path, "AuthForgotPasswordController.php")

    os.makedirs(folder_path, exist_ok=True)

    content = f'''<?php

namespace App\\Http\\Controllers\\API\\V1\\Auth;

use App\\Http\\Controllers\\Controller;
use App\\Http\\Requests\\API\\V1\\Auth\\AuthForgotPasswordRequest;
use Illuminate\\Http\\JsonResponse;
use Illuminate\\Support\\Facades\\Password;



class AuthForgotPasswordController extends Controller
{{

    public function __invoke(AuthForgotPasswordRequest $request): JsonResponse
    {{
        $status = Password::sendResetLink([
            'email' => $request->email,
        ]);

        if ($status !== Password::RESET_LINK_SENT) {{
            return $this->respondWithError(
                __($status),
                422
            );
        }}

        return $this->respondWithData(
            'Password reset link sent',
            []
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

