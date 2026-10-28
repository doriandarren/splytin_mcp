import os
from gen.helpers.helper_print import print_message, GREEN, CYAN, run_command





def generate_exception_handler_response(full_path):
    """
    Genera un archivo

    Args:
        full_path (str): Ruta completa del proyecto.
    """
    styles_path = os.path.join(full_path, "app", "Exceptions")

    # Crear la carpeta si no existe
    if not os.path.exists(styles_path):
        os.makedirs(styles_path)
        print_message(f"Carpeta creada: {styles_path}", GREEN)

    # Ruta completa del archivo
    file_path = os.path.join(styles_path, "HandlerResponse.php")

    # Contenido por defecto
    content = r"""<?php

namespace App\Exceptions;

use Illuminate\Http\JsonResponse;

class HandlerResponse
{
    public static function respondWithValidationErrors(array $errors, int $statusCode = 422): JsonResponse
    {
        $items = [];

        foreach ($errors as $field => $messages) {
            foreach ((array) $messages as $message) {
                $items[] = [
                    'detail' => (string) $message,
                    'status' => (string) $statusCode,
                    'code' => 'invalid',
                    'meta' => ['field' => (string) $field],
                ];
            }
        }

        return new JsonResponse(
            ['errors' => $items],
            $statusCode,
            ['Content-Type' => 'application/vnd.api+json']
        );
    }

    public static function respondWithError($message, $statusCode, $errors = null): JsonResponse
    {
        $details = [];
        if (is_array($errors)) {
            array_walk_recursive($errors, function ($detail) use (&$details) {
                if (is_string($detail) && $detail !== '') {
                    $details[] = $detail;
                }
            });
        } elseif (is_string($errors) && $errors !== '') {
            $details[] = $errors;
        }

        if ($details === []) {
            $details[] = (string) $message;
        }

        $statusCode = (int) $statusCode;
        $errorCode = match ($statusCode) {
            401 => 'not_authenticated',
            403 => 'permission_denied',
            404 => 'not_found',
            405 => 'method_not_allowed',
            409 => 'conflict',
            400, 422 => 'invalid',
            default => 'error',
        };

        return new JsonResponse([
            'errors' => array_map(fn (string $detail) => [
                'detail' => $detail,
                'status' => (string) $statusCode,
                'code' => $errorCode,
            ], $details),
        ], $statusCode, ['Content-Type' => 'application/vnd.api+json']);
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
