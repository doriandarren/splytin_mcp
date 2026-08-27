import os
from gen.helpers.helper_print import print_message, GREEN, CYAN



def generate_auth_login(full_path):
    # Login
    create_login_request(full_path)
    create_login(full_path)



def create_login_request(full_path):
    """
    Genera el archivo
    """

    folder_path = os.path.join(full_path, "app", "Http", "Requests", "API", "V1", "Auth")
    file_path = os.path.join(folder_path, "AuthLoginRequest.php")

    os.makedirs(folder_path, exist_ok=True)

    content = f"""<?php

namespace App\\Http\\Requests\\API\\V1\\Auth;

use Illuminate\\Contracts\\Validation\\ValidationRule;
use Illuminate\\Foundation\\Http\\FormRequest;

class AuthLoginRequest extends FormRequest
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
            'email' => ['required', 'string', 'email'],
            'password' => ['required', 'string', 'min:8'],
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





def create_login(full_path):
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
    file_path = os.path.join(styles_path, "AuthLoginController.php")

    # Contenido por defecto
    content = f"""<?php

namespace App\\Http\\Controllers\\API\\V1\\Auth;

use App\\Http\\Controllers\\Controller;
use Illuminate\\Support\\Facades\\Auth;
use Illuminate\\Http\\JsonResponse;
use App\\Enums\\Roles\\EnumRole;
use App\\Utilities\\Messages\\MessageChannel;
use App\\Http\\Requests\\API\\V1\\Auth\\AuthLoginRequest;
use App\\Models\\User;


class AuthLoginController extends Controller
{{
    /**
     *
     * @bodyParam email string required Must be a valid email address. Example: satterfield.buddy@example.org
     * @bodyParam password string required
     *
     * @param AuthRequest $request
     * @return JsonResponse
     */
    public function __invoke(AuthLoginRequest $request): JsonResponse
    {{
        
        $credentials = $request->validated();

        //Response 200 but with error
        if(!Auth::attempt($credentials))
        {{
            return $this->respondHttpUnauthorized();
        }}


        $user = User::find(Auth::user()->id);
        //$user = Auth::user();
        // Delete Tokens
        //$user->tokens()->delete();


        if(count($user->roles) == 0){{
            MessageChannel::send(
                'Error Authentication ERP - User Id: (' . $user->id .') Usuario: ' . $user->name, 
                'Error Auth',
                true
            );
            return $this->respondWithError(
                'User without role', 
                ['e' => 'User without role']
            );
        }}


        // Validate Roles
        if($user->roles->contains('name', EnumRole::ADMIN)){{

            $token = $user->createToken(
                'API Token for ' . $user->email,
                ['*'],
                now()->addDay()
            )->plainTextToken;
            $userTemp = $user;
            //$userTemp->abilities = $user->abilities;
            return $this->respondWithToken('Login successfully - Admin', $token);

        }}else{{

            $arr = [];
            foreach ($user->abilities as $ability) {{
                $arr[] = $ability->name;
            }}
            $token = $user->createToken(
                    'API Token for ' . $user->email,
                    $arr,
                    now()->addDay()
                )->plainTextToken;
            return $this->respondWithToken('Login successfully', $token);
            
        }}

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
