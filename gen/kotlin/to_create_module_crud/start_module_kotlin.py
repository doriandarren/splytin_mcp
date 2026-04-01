from helpers.helper_columns import parse_columns_input
from helpers.helper_menu import menu_checkbox, pause
from helpers.helper_print import input_with_validation


def start_module_kotlin():

    opt = [
        ("Route", "route"),
        ("List", "list"),
        ("Create", "create"),
        ("Edit", "edit"),
        ("Barril", "barrel"),
        ("Service", "service"),
    ]

    input_menu_checkbox = menu_checkbox("Componentes: ", opt)

    default_path = "/Users/dorian/AndroidStudioProjects"

    fullt_path = input_with_validation("Carpeta Proyecto", default_path)
    singular_name = input_with_validation("Nombre singular", "AgendaUnloading")
    plural_name = input_with_validation("Nombre plural", "AgendaUnloadings")
    input_columns = input_with_validation("Columnas: ", "user_id:fk name age:integer description")

    columns = parse_columns_input(input_columns)

    # TODO refactor
    # standard_module_crud_XXXXXX(full_path, singular_name, plural_name, columns, input_menu_checkbox)

    pause()