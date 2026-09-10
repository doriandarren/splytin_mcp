import os
from gen.helpers.helper_print import print_message, GREEN, CYAN





def update_app_service_provider(full_path):
    """
    Actualiza el archivo
    """
    main_path = os.path.join(full_path, "app", "Providers", "AppServiceProvider.php")

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
            """    public function boot(): void
    {""",
            """    public function boot(): void
    {
        Blueprint::macro('userstamps', function () {
            $this->unsignedBigInteger('created_by')->nullable()->index();
            $this->unsignedBigInteger('updated_by')->nullable()->index();
            $this->unsignedBigInteger('deleted_by')->nullable()->index();
        });"""
        )



        # Reemplazos
        content = content.replace(
            """use Illuminate\Support\ServiceProvider;""",
            """use Illuminate\Support\ServiceProvider;
use Illuminate\Database\Schema\Blueprint;"""
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

    