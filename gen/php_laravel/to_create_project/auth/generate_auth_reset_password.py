import os
from gen.helpers.helper_print import print_message, GREEN, CYAN



def generate_auth_reset_password(full_path):
    # Restore Password
    create_reset_password_request(full_path)
    create_reset_password(full_path)
    
    ## Notifications
    create_auth_reset_password_notification(full_path)
    update_model_user(full_path)
    update_config_app(full_path)

    



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
    
    
    /**
     * Reset Password
     *
     * @param AuthResetPasswordRequest $request
     * @return JsonResponse
     */
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
        





def create_auth_reset_password_notification(full_path):
    """
    Genera el archivo
    """
    folder_path = os.path.join(full_path, "app", "Notifications", "Auth")
    file_path = os.path.join(folder_path, "AuthResetPasswordNotification.php")

    os.makedirs(folder_path, exist_ok=True)

    content = r'''<?php

namespace App\Notifications;

use Illuminate\Bus\Queueable;
use Illuminate\Notifications\Messages\MailMessage;
use Illuminate\Notifications\Notification;

class ResetPasswordNotification extends Notification
{
    use Queueable;

    public function __construct(
        protected string $token
    ) {
        //
    }

    public function via(object $notifiable): array
    {
        return ['mail'];
    }

    public function toMail(object $notifiable): MailMessage
    {
        $url = config('app.frontend_url')
            . '/reset-password?token='
            . $this->token
            . '&email='
            . urlencode($notifiable->email);

        return (new MailMessage)
            ->subject('Restablecer contraseña')
            ->greeting('¡Hola ' . $notifiable->name . '!')
            ->line('Hemos recibido una solicitud para restablecer tu contraseña.')
            ->action('Restablecer contraseña', $url)
            ->line('Si no has solicitado este cambio, puedes ignorar este correo.')
            ->salutation('Un saludo');
    }
}
'''

    try:
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)
        
        
        

        
def update_model_user(full_path):
    """
    Genera el archivo
    """
    folder_path = os.path.join(full_path, "app", "Notifications", "Auth")
    file_path = os.path.join(folder_path, "AuthResetPasswordNotification.php")

    os.makedirs(folder_path, exist_ok=True)

    content = r"""
   
"""

    try:
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)        


        
def update_model_user(full_path):
    """
    Actualiza el archivo
    """
    main_path = os.path.join(full_path, "Models", "User.php")

    # Verificar si el archivo existe
    if not os.path.exists(main_path):
        print_message(f"Error: {main_path} no existe.", CYAN)
        return

    try:
        # Leer el contenido del archivo
        with open(main_path, "r") as f:
            content = f.read()

        content = content.replace(
            """use Laravel\\Sanctum\\HasApiTokens;""",
            """use Laravel\\Sanctum\\HasApiTokens;
use App\\Notifications\\Auth\\AuthResetPasswordNotification;"""
        )


        # Reemplazos
        content = content.replace(
            """    /*********************
    * Relations
    ********************/""",
            """
    // Reset Password
    public function sendPasswordResetNotification($token): void
    {{
        $this->notify(new ResetPasswordNotification($token));
    }}

    /*********************
    * Relations
    ********************/"""
        )

        # Escribir el contenido actualizado
        with open(main_path, "w") as f:
            f.write(content)

        print_message(
            f"{main_path} actualizado correctamente.",
            GREEN
        )

    except Exception as e:
        print_message(
            f"Error al actualizar {main_path}: {e}",
            CYAN
        )

    


def update_config_app(full_path):
    """
    Actualiza el archivo
    """
    main_path = os.path.join(full_path, "config", "app.php")

    # Verificar si el archivo existe
    if not os.path.exists(main_path):
        print_message(f"Error: {main_path} no existe.", CYAN)
        return

    try:
        # Leer el contenido del archivo
        with open(main_path, "r") as f:
            content = f.read()

        # Reemplazos
        content = content.replace(
            """];""",
            """    ## Reset Password
    'frontend_url' => env('FRONTEND_URL'),

];"""
        )

        # Escribir el contenido actualizado
        with open(main_path, "w") as f:
            f.write(content)

        print_message(
            f"{main_path} actualizado correctamente.",
            GREEN
        )

    except Exception as e:
        print_message(
            f"Error al actualizar {main_path}: {e}",
            CYAN
        )

    

