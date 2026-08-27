import os
from gen.helpers.helper_print import print_message, GREEN, CYAN

def generate_auth_register(full_path):
    create_register_request(full_path)
    create_register(full_path)




def create_register_request(full_path):
    """
    Genera el archivo
    """

    folder_path = os.path.join(full_path, "app", "Http", "Requests", "API", "V1", "Auth")
    file_path = os.path.join(folder_path, "AuthRegisterRequest.php")

    os.makedirs(folder_path, exist_ok=True)

    content = f"""<?php

namespace App\\Http\\Requests\\API\\V1\\Auth;

use Illuminate\\Contracts\\Validation\\ValidationRule;
use Illuminate\\Foundation\\Http\\FormRequest;

class AuthRegisterRequest extends FormRequest
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
            'name' => [
                'required',
                'string',
                'max:255',
            ],

            'email' => [
                'required',
                'string',
                'email',
                'max:255',
                'unique:users,email',
            ],

            'password' => [
                'required',
                'string',
                'min:8',
                'confirmed',
            ],
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




def create_register(full_path):
    """
    Genera un archivo

    Args:
        full_path (str): Ruta completa del proyecto.
    """
    styles_path = os.path.join(full_path, "app", "Http", "Controllers", "API", "V1", "Auth")

    # Crear la carpeta si no existe
    if not os.path.exists(styles_path):
        os.makedirs(styles_path)
        print_message(f"Carpeta creada: {styles_path}", GREEN)

    # Ruta completa del archivo
    file_path = os.path.join(styles_path, "AuthRegisterController.php")

    # Contenido por defecto
    content = f"""<?php

namespace App\\Http\\Controllers\\API\\V1\\Auth;

use App\\Http\\Controllers\\Controller;
use Illuminate\\Http\\JsonResponse;
use App\\Http\\Requests\\API\\V1\\Auth\\AuthRegisterRequest;
use App\\Enums\\Roles\\EnumRole;
use App\\Enums\\UserStatuses\\EnumUserStatus;
use App\\Models\\SHARED\\Roles\\Role;
use App\\Models\\User;

class AuthRegisterController extends Controller
{{
    /**
     * @param AuthRegisterRequest $request
     * @return JsonResponse
     */
    public function __invoke(AuthRegisterRequest $request): JsonResponse
    {{

        $validated = $request->validated();

        $user = User::create([
            'name' => $validated['name'],
            'email' => $validated['email'],
            'password' => $validated['password'],
            'user_status_id' => EnumUserStatus::ACTIVE_ID,
        ]);

        $role = Role::where('name', EnumRole::USER)->first();

        $user->assignRole($role);
        
        $token = $user->createToken(
            'API Token for ' . $user->email,
            ['*'],
            now()->addDay()
        )->plainTextToken;

        return $this->respondWithToken(
            'Successfully created user.',
            $token
        );
    }}
}}
"""

    try:
        # Crear o sobrescribir el archivo con el contenido
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)

