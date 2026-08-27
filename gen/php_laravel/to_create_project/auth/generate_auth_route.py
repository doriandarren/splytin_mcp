import os
from gen.helpers.helper_print import print_message, GREEN, CYAN

def generate_auth_route(full_path):
    create_auth_route(full_path)



def create_auth_route(full_path):
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
use App\Http\Controllers\API\V1\Auth\AuthUserController;
use App\Http\Controllers\API\V1\Auth\AuthLogoutController;
use App\Http\Controllers\API\V1\Auth\AuthRegisterController;
use App\Http\Controllers\API\V1\Auth\AuthForgotPasswordController;
use App\Http\Controllers\API\V1\Auth\AuthResetPasswordController;

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
Route::get('auth/reset-password', function (Request $request) {
    return response()->json([
        'token' => $request->token,
        'email' => $request->email,
    ]);
})->name('password.reset');


// Logout & Auth User
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


