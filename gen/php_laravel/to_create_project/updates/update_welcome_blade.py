import os
from gen.helpers.helper_print import print_message, GREEN, CYAN



def update_welcome_blade(full_path, project_name, domain_name):
    """
    Genera un archivo

    Args:
        full_path (str): Ruta completa del proyecto.
    """
    styles_path = os.path.join(full_path, "resources", "views")

    # Crear la carpeta si no existe
    if not os.path.exists(styles_path):
        os.makedirs(styles_path)
        print_message(f"Carpeta creada: {styles_path}", GREEN)

    # Ruta completa del archivo
    file_path = os.path.join(styles_path, "welcome.blade.php")

    # Contenido por defecto
    content = r"""<!DOCTYPE html>
<html lang="{{ str_replace('_', '-', app()->getLocale()) }}">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        
        <link rel="icon" href="{{ asset('brand/images/company_logos/favicon.ico') }}" type="image/x-icon">

        <title>{{ env('APP_NAME') }}</title>

        <!-- Fonts -->
        <link rel="preconnect" href="https://fonts.bunny.net">
        <link href="https://fonts.bunny.net/css?family=instrument-sans:400,500,600" rel="stylesheet" />
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css" />

        <!-- Styles / Scripts -->
        <script src="https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"></script>

    </head>
    
    <body class="bg-[#e6e6e6] min-h-screen flex flex-col justify-between">
        <div class="flex flex-1 items-center justify-center px-4">
            <img
                src="{{ asset('brand/images/company_logos/logo.svg') }}"
                alt="logo"
                class="w-40 sm:w-48 md:w-56 lg:w-64 xl:w-72 h-auto mx-auto animate__animated animate__zoomIn"
            />
        </div>
        <footer class="w-full text-md text-left text-black px-8 mb-5 animate__animated animate__slideInLeft">
            ©<span id="year"></span> __PROJECT_NAME__ - Developed by <a href="https://splytin.com" target="_blank"><strong> Splytin</strong></a>.
        </footer>
        <script>
            document.getElementById("year").textContent = new Date().getFullYear();
        </script>
    </body>

</html>
"""

    content = content.replace('__PROJECT_NAME__', project_name)


    try:
        # Crear o sobrescribir el archivo con el contenido
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)

