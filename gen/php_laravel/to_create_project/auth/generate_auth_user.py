import os
from gen.helpers.helper_print import print_message, GREEN, CYAN



def generate_auth_user(full_path):
    create_auth_user(full_path)
    create_auth_user_resource(full_path)



def create_auth_user(full_path):
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
    content = r"""<?php

namespace App\Http\Controllers\API\V1\Auth;

use App\Http\Controllers\Api\\V1\ApiController;
use App\Http\Resources\V1\Auth\AuthUserResource;
use Illuminate\Http\JsonResponse;
use Illuminate\Http\Request;


class AuthUserController extends ApiController
{
    /**
     * @param Request $request
     * @return JsonResponse
     */
    public function __invoke(Request $request): JsonResponse
    {
        $data = $request->user()->load([
            'roles',
            'status'
        ]);
        
        return $this->respondWithData(
            'Auth show',
            new AuthUserResource($data)
        );

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





def create_auth_user_resource(full_path):
    """
    Genera un archivo

    Args:
        full_path (str): Ruta completa del proyecto.
    """
    styles_path = os.path.join(full_path, "app", "Http", "Resources", "V1", "Auth")

    # Crear la carpeta si no existe
    if not os.path.exists(styles_path):
        os.makedirs(styles_path)
        print_message(f"Carpeta creada: {styles_path}", GREEN)

    # Ruta completa del archivo
    file_path = os.path.join(styles_path, "AuthUserResource.php")

    # Contenido por defecto
    content = r"""<?php

namespace App\Http\Resources\V1\Auth;

use App\Http\Resources\V1\Roles\RoleResource;
use App\Http\Resources\V1\UserStatuses\UserStatusResource;
use Illuminate\Http\Request;
use Illuminate\Http\Resources\Json\JsonResource;

class AuthUserResource extends JsonResource
{
    /**
     * Transform the resource into an array.
     *
     * @return array<string, mixed>
     */
    public function toArray(Request $request): array
    {
        return [
            'type' => 'auth',
            'id' => $this->id,
            'attributes' => [
                'user_status_id' => $this->user_status_id,
                'name' => $this->name,
                'email' => $this->email,
                'image_url' => $this->image_url,
                'created_at' => $this->created_at,
                'updated_at' => $this->updated_at,
            ],
            // 'includes' => [
                // new UserStatusResource($this->whenLoaded('user_status')),
            //],
            'relationships' => [
                // Relación de muchos
                'roles' => RoleResource::collection($this->roles),
                // Relación de uno
                'user_status' => new UserStatusResource($this->status),
            ],
            'links' => [
                'self' => route('users.show', ['user' => $this->id])
            ]
        ];
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