import os
from gen.helpers.helper_print import print_message, GREEN, CYAN



def generate_auth_logout(full_path):
    create_logout(full_path)
    




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

