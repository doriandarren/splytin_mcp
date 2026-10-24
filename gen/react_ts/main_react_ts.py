from gen.helpers.helper_print import print_header
from gen.helpers.helper_menu import menu_list, clear_screen
from gen.react_ts.to_create_module_crud.start_module_crud_react_ts import StartModuleCrudReactTs
from gen.react_ts.to_create_project.start_project_react_ts import StartProjectReactTs



class MainReactTs:

    def invoke(self):
        """Menú principal para generar código (proyectos / módulos)."""

        while True:
            clear_screen()
            print_header("main_react_ts")

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
                obj = StartProjectReactTs()
                obj.invoke()
                
            elif opt == 'crud':
                obj = StartModuleCrudReactTs()
                obj.invoke()
                
            elif opt == 'back':
                print("\nVolviendo al menú anterior...\n")
                break

            else:
                print("Opción no reconocida.")
