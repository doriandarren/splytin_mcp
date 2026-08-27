import os
from gen.helpers.helper_print import print_message, GREEN, CYAN



def generate_module_auth(full_path):
    # Login
    create_login_request(full_path)
    create_login(full_path)
    
    # Logout
    create_logout(full_path)
    
    # Register
    create_register_request(full_path)
    create_register(full_path)
    
    # Forgot Password
    create_forgot_password_request(full_path)
    create_forgot_password(full_path)
    
    # Restore Password
    create_reset_password_request(full_path)
    create_reset_password(full_path)
    
    create_user(full_path)
    create_route(full_path)
    
    



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





def create_logout(full_path):
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
    file_path = os.path.join(styles_path, "AuthLogoutController.php")

    # Contenido por defecto
    content = """<?php

namespace App\\Http\\Controllers\\API\\V1\\Auth;

use App\\Http\\Controllers\\Controller;
use Illuminate\\Http\\Request;
use Illuminate\\Http\\JsonResponse;

class AuthLogoutController extends Controller
{
    /**
     * @param Request $request
     * @return JsonResponse
     */
    public function __invoke(Request $request): JsonResponse
    {

        $user = $request->user();
        $request->user()->tokens()->delete();

        return $this->respondWithData("Successfully logged out");

    }
    
}
"""

    try:
        # Crear o sobrescribir el archivo con el contenido
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)






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
use Illuminate\\Http\\Request;
use App\\Enums\\Roles\\EnumRole;
use App\\Enums\\UserStatuses\\EnumUserStatus;
use App\\Models\\SHARED\Roles\\Role;
use App\\Models\\User;

class AuthRegisterController extends Controller
{{
    /**
     * @param Request $request
     * @return JsonResponse
     */
    public function __invoke(Request $request): JsonResponse
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






def create_user(full_path):
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
    file_path = os.path.join(styles_path, "AuthUserController.php")

    # Contenido por defecto
    content = """<?php

namespace App\\Http\\Controllers\\API\\V1\\Auth;

use App\\Http\\Controllers\\Controller;
use Illuminate\\Http\\JsonResponse;
use Illuminate\\Http\\Request;
use stdClass;

class AuthUserController extends Controller
{
    /**
     * @param Request $request
     * @return JsonResponse
     */
    public function __invoke(Request $request): JsonResponse
    {
        $data = new stdClass();
        $data->user = $request->user();
        //$data->user->abilities = $request->user()->abilities;
        $data->user->roles = $request->user()->roles;

        if($this->isAdmin($request->user()->roles)){

            return $this->respondWithData("User current", $data->user);

        }else{

            return $this->respondWithData("User current", $data->user);
        }

    }

}
"""

    try:
        # Crear o sobrescribir el archivo con el contenido
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)



def create_route(full_path):
    """
    Genera un archivo

    Args:
        full_path (str): Ruta completa del proyecto.
    """
    styles_path = os.path.join(full_path, "routes", "API", "V1")

    # Crear la carpeta si no existe
    if not os.path.exists(styles_path):
        os.makedirs(styles_path)
        print_message(f"Carpeta creada: {styles_path}", GREEN)

    # Ruta completa del archivo
    file_path = os.path.join(styles_path, "auth.php")

    # Contenido por defecto
    content = r"""<?php

use Illuminate\Support\Facades\Route;
use App\Http\Controllers\API\V1\Auth\AuthLoginController;
use App\Http\Controllers\API\V1\Auth\AuthLogoutController;
use App\Http\Controllers\API\V1\Auth\AuthRegisterController;
use App\Http\Controllers\API\V1\Auth\AuthUserController;
use App\Http\Controllers\API\V1\Auth\AuthForgotPasswordController;
use App\Http\Controllers\API\V1\Auth\AuthUserController;

/*
|--------------------------------------------------------------------------
| API Auth
|--------------------------------------------------------------------------
*/

// Login
Route::post('auth/login', [AuthLoginController::class, '__invoke']);

// Register
Route::post('auth/register', [AuthRegisterController::class, '__invoke']);

// Password Reset
Route::post('auth/forgot-password', [AuthForgotPasswordController::class, '__invoke']);
Route::post('auth/reset-password', [AuthResetPasswordController::class, '__invoke']);


Route::group(['middleware' => 'auth:sanctum'], function () {
    Route::get('auth/user', [AuthUserController::class, '__invoke']);
    Route::post('auth/logout', [AuthLogoutController::class, '__invoke']);
});
"""

    try:
        # Crear o sobrescribir el archivo con el contenido
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)





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






def create_reset_password_request(full_path):
    """
    Genera el archivo
    """

    folder_path = os.path.join(full_path, "app", "Http", "Requests", "API", "V1", "Auth")
    file_path = os.path.join(folder_path, "AuthResetPasswordRequest.php")

    os.makedirs(folder_path, exist_ok=True)

    content = f'''<?php

namespace App\\Http\\Requests\\API\\V1\\Auth;

use Illuminate\\Contracts\\Validation\\ValidationRule;
use Illuminate\\Foundation\\Http\\FormRequest;

class AuthResetPasswordRequest extends FormRequest
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
            'email' => [
                'required',
                'email',
            ],
            'token' => [
                'required',
                'string',
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

'''

    try:
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)





def create_reset_password(full_path):
    """
    Genera el archivo
    """

    folder_path = os.path.join(full_path, "app", "Http", "Controllers", "API", "V1", "Auth")
    file_path = os.path.join(folder_path, "AuthResetPasswordController.php")

    os.makedirs(folder_path, exist_ok=True)

    content = f"""<?php

namespace App\\Http\\Controllers\\API\\V1\\Auth;

use App\\Http\\Controllers\\Controller;
use App\\Http\\Requests\\API\\V1\\Auth\\AuthResetPasswordRequest;
use Illuminate\\Http\\JsonResponse;
use Illuminate\\Support\\Facades\\Hash;
use Illuminate\\Support\\Facades\\Password;
use Illuminate\\Support\\Str;


class AuthResetPasswordController extends Controller
{{

    public function __invoke(AuthResetPasswordRequest $request): JsonResponse
    {{
        $status = Password::reset(
            $request->only(
                'email',
                'password',
                'password_confirmation',
                'token'
            ),
            function ($user, string $password) {{
                $user->forceFill([
                    'password' => Hash::make($password),
                    'remember_token' => Str::random(60),
                ])->save();
            }}
        );

        if ($status !== Password::PASSWORD_RESET) {{
            return $this->respondWithError(
                'Password could not be reset',
                [],
                422
            );
        }}

        return $this->respondWithData(
            'Password reset successfully',
            []
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