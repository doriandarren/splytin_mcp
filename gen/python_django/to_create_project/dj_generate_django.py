import os
from gen.helpers.helper_file import HelperFile
from gen.helpers.helper_print import print_message, GREEN, CYAN, run_command
from gen.python_django.helpers.helper_file import helper_create_init_file, helper_update_list


class DjGenerateDjango:


    def invoke(self, full_path, project_name_format, app_main, venv_python):
        """
        Genera el archivo
        """
        self.install_django(full_path, venv_python)
        self.install_requests(full_path, venv_python)
        
        self.create_app(full_path, app_main, venv_python)
        self.create_commands(full_path, app_main, venv_python)
        
        self.install_django_rest_framework(full_path, venv_python)
        self.update_settings(full_path, app_main)
        


        
    def install_django(self, full_path, venv_python):
        print_message("Instalando django...", CYAN)
        run_command(f'"{venv_python}" -m pip install django', cwd=full_path)
        print_message("django instalado correctamente.", GREEN)
        
        
    def install_requests(self, full_path, venv_python):
        print_message("Instalando requests...", CYAN)
        run_command(f'"{venv_python}" -m pip install requests', cwd=full_path)
        print_message("requests instalado correctamente.", GREEN)



    def install_django_rest_framework(self, full_path, venv_python):
        print_message("Instalando djangorestframework...", CYAN)
        run_command(f'"{venv_python}" -m pip install djangorestframework', cwd=full_path)
        print_message("djangorestframework instalado correctamente.", GREEN)


    def create_app(self, full_path, app_main, venv_python):
        print_message("Creando app Principal..." + app_main, CYAN)

        # Esto crea el proyecto dentro del directorio actual
        run_command(f'"{venv_python}" -m django startproject {app_main} .', cwd=full_path)

        print_message(f"App Principal: {app_main} creado correctamente.", GREEN)





    def create_commands(self, full_path, app_main, venv_python):
        """
        Genera el archivo
        """

        folder_path = os.path.join(
            full_path,
            app_main,
            "management",
            "commands"
        )

        folder_path_management = os.path.join(
            full_path,
            app_main,
            "management"
        )

        # Crear __init__.py en Commands
        HelperFile.write(
            folder_path=folder_path,
            file_name="__init__.py",
            content=""
        )

        # Crear __init__.py en Management
        HelperFile.write(
            folder_path=folder_path_management,
            file_name="__init__.py",
            content=""
        )


        content = r'''from pathlib import Path
import shutil

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Elimina las migraciones de todas las apps dentro de proyecto/apps, excepto __init__.py"

    def add_arguments(self, parser):
        parser.add_argument(
            "--dry-run",
            action="store_true",
            help="Muestra qué archivos se borrarían sin eliminarlos",
        )

    def handle(self, *args, **options):
        dry_run = options["dry_run"]

        # clear_migracions.py está en:
        # proyecto/main/management/commands/clear_migracions.py
        # subimos hasta proyecto/
        base_dir = Path(__file__).resolve().parents[3]
        apps_dir = base_dir / "apps"

        if not apps_dir.exists() or not apps_dir.is_dir():
            self.stdout.write(
                self.style.ERROR(f"No existe la carpeta de apps: {apps_dir}")
            )
            return

        deleted_files = 0
        deleted_dirs = 0
        found = False

        for app_dir in apps_dir.iterdir():
            if not app_dir.is_dir():
                continue

            migrations_dir = app_dir / "migrations"

            if not migrations_dir.exists() or not migrations_dir.is_dir():
                continue

            found = True
            self.stdout.write(f"\nRevisando app: {app_dir.name}")

            # Borrar archivos .py excepto __init__.py
            for py_file in migrations_dir.glob("*.py"):
                if py_file.name == "__init__.py":
                    continue

                if dry_run:
                    self.stdout.write(f"[DRY RUN] Se borraría: {py_file}")
                else:
                    py_file.unlink()
                    self.stdout.write(f"Eliminado: {py_file}")
                    deleted_files += 1

            # Borrar archivos .pyc
            for pyc_file in migrations_dir.glob("*.pyc"):
                if dry_run:
                    self.stdout.write(f"[DRY RUN] Se borraría: {pyc_file}")
                else:
                    pyc_file.unlink()
                    self.stdout.write(f"Eliminado: {pyc_file}")
                    deleted_files += 1

            # Borrar carpeta __pycache__
            pycache_dir = migrations_dir / "__pycache__"
            if pycache_dir.exists() and pycache_dir.is_dir():
                if dry_run:
                    self.stdout.write(f"[DRY RUN] Se borraría directorio: {pycache_dir}")
                else:
                    shutil.rmtree(pycache_dir)
                    self.stdout.write(f"Eliminado directorio: {pycache_dir}")
                    deleted_dirs += 1

        if not found:
            self.stdout.write(
                self.style.WARNING("No se encontraron carpetas migrations dentro de apps/")
            )
            return

        if dry_run:
            self.stdout.write(
                self.style.WARNING("\nSimulación completada")
            )
        else:
            self.stdout.write(
                self.style.SUCCESS(
                    f"\nProceso completado. Archivos eliminados: {deleted_files}, carpetas eliminadas: {deleted_dirs}"
                )
            )
    '''

        # Crear el archivo
        HelperFile.write(
            folder_path=folder_path,
            file_name="clear_migrations.py",
            content=content
        )
            


            


    def update_settings(self, full_path, app_main):
        
        # Agregar rest_framework a INSTALLED_APPS
        helper_update_list(
            full_path, 
            f"{app_main}/settings.py", 
            "INSTALLED_APPS", 
            f"'rest_framework',                   # required for DRF"
        )
        
        
        # Agregar main a INSTALLED_APPS
        helper_update_list(
            full_path, 
            f"{app_main}/settings.py", 
            "INSTALLED_APPS", 
            f"'{app_main}',                             # Module main"
        )
