import sys
import os

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if BASE_DIR not in sys.path:
    sys.path.append(BASE_DIR)

from gen.kotlin.to_create_module_crud.start_module_kotlin import start_module_kotlin
from gen.kotlin.to_create_project.start_project_kotlin import start_project_kotlin
from helpers.helper_print import print_header
from helpers.helper_menu import menu_list, clear_screen


def main_kotlin():
    """Menú principal para generar código (proyectos / módulos)."""

    while True:
        clear_screen()
        print_header("Menú KOTLIN")

        str_input = menu_list(
            "¿Qué quieres crear?: ",
            [
                {"name": "Proyecto", "value": "project"},
                {"name": "Módulo CRUD", "value": "crud"},
                {"name": "Volver", "value": "back"},
            ]
        )

        opt = str_input.strip().lower()

        print(f"Crear un: {str_input} ")

        if opt == 'project':
            pass
            start_project_kotlin()
            
        if opt == 'crud':
            pass
            start_module_kotlin()
            
        elif opt == 'back':
            print("\nVolviendo al menú anterior...\n")
            break

        else:
            print("Opción no reconocida.")


if __name__ == "__main__":
    main_kotlin()