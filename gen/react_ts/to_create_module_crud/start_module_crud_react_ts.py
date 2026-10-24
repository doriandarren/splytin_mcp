import os
from dotenv import load_dotenv
from helpers.helper_columns import parse_columns_input
from helpers.helper_menu import menu_checkbox, pause
from helpers.helper_print import input_with_validation


# Load ENV
load_dotenv()


class StartModuleCrudReactTs:

    def invoke(self):

        opt = [
            ("Route", "route"),
            ("List", "list"),
            ("Create", "create"),
            ("Edit", "edit"),
            ("Barril", "barrel"),
            ("Service", "service"),
        ]

        input_menu_checkbox = menu_checkbox("Componentes: ", opt)
        default_namespace = "API"

        default_path = os.getenv("DEFAULT_PATH_PROJECT_PHP")

        full_path = input_with_validation("Carpeta Proyecto", default_path)
        namespace = input_with_validation("Namespace (ERP / API / INVOICES)", default_namespace)
        singular_name = input_with_validation("Nombre singular", "AgendaUnloading")
        plural_name = input_with_validation("Nombre plural", "AgendaUnloadings")
        input_columns = input_with_validation("Columnas: ", "user_id:fk name age:integer description")

        columns = parse_columns_input(input_columns)

        # TODO refactor
        # obj = StandardModuleCrudReactTs()
        # obj.invoke(full_path, namespace, singular_name, plural_name, columns, input_menu_checkbox)

        pause()


