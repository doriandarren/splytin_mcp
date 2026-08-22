import os
from gen.helpers.helper_print import print_message, GREEN, CYAN, run_command



def generate_messages(full_path):
    """
    Genera un archivo

    Args:
        full_path (str): Ruta completa del proyecto.
    """
    styles_path = os.path.join(full_path, "app", "Utilities", "Messages")

    # Crear la carpeta si no existe
    if not os.path.exists(styles_path):
        os.makedirs(styles_path)
        print_message(f"Carpeta creada: {styles_path}", GREEN)

    # Ruta completa del archivo
    file_path = os.path.join(styles_path, "MessageChannel.php")

    # Contenido por defecto
    content = r"""<?php

namespace App\Utilities\Messages;

use Illuminate\Http\Client\ConnectionException;
use Illuminate\Support\Facades\Http;
use stdClass;

class MessageChannel
{

    /**
     * @param $text
     * @param string $title
     * @param bool $isError
     * @return void
     */
    public static function send($text, string $title='Title', bool $isError = false): void
    {

        $title .= ' ' . env('APP_NAME') . ' ' . env('APP_ENV');

        // Limitar $text a 500 caracteres
        $text = mb_substr($text, 0, 500);

        $embed = [
            'title' => $title,
            'description' => $text,
            'color' => $isError ? 0xFF0000 : 0x00FF00 // Red : Green
        ];

        // JSON
        $payload = [
            'embeds' => [$embed]
        ];

        try {
            Http::withHeaders([
                'Content-Type' => 'application/json',
            ])
                ->post(env('MESSAGE_CHANNEL_URL'), $payload);
        } catch (\GuzzleHttp\Exception\GuzzleException $e) {
            echo 'Error: ' . $e->getMessage();
        }catch (ConnectionException $e) {
            echo 'Error: ' . $e->getMessage();
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
