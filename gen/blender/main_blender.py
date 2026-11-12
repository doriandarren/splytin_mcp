import sys
import os

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if BASE_DIR not in sys.path:
    sys.path.append(BASE_DIR)

from gen.blender.to_create_project.start_assets_blender import start_assets_blender
from helpers.helper_print import print_header
from helpers.helper_menu import menu_list, clear_screen


def main_blender(base_dir):
    """Menú principal para generar código (proyectos / módulos)."""

    while True:
        clear_screen()
        print_header("Blender")

        str_input = menu_list(
            "¿Qué quieres crear?: ",
            [
                {"name": "Assets", "value": "assets"},
                # {"name": "Módulo CRUD", "value": "crud"},
                {"name": "Volver", "value": "back"},
            ]
        )

        opt = str_input.strip().lower()

        print(f"Crear un: {str_input} ")

        if opt == 'assets':
            start_assets_blender(base_dir)
            
        # elif opt == 'crud':
        #     pass
            # start_module_X()
            
        elif opt == 'back':
            print("\nVolviendo al menú anterior...\n")
            break

        else:
            print("Opción no reconocida.")
