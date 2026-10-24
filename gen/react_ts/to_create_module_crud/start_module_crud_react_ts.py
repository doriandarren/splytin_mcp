import os
from dotenv import load_dotenv
from gen.react_ts.to_create_module_crud.standard_module_crud_react_ts import StandardModuleCrudReactTs
from gen.helpers.helper_columns import parse_columns_input
from gen.helpers.helper_menu import menu_checkbox, pause
from gen.helpers.helper_print import input_with_validation


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
        default_version_api = "V1"
        default_folder_group = "api"

        default_path = os.getenv("DEFAULT_PATH_PROJECT_REACT_TS")

        full_path = input_with_validation("Carpeta Proyecto", default_path)
        namespace = input_with_validation("Namespace (ERP / API / INVOICES)", default_namespace)
        singular_name = input_with_validation("Nombre singular", "AgendaUnloading")
        plural_name = input_with_validation("Nombre plural", "AgendaUnloadings")
        input_columns = input_with_validation("Columnas: ", "user_id:fk name age:integer description")

        columns = parse_columns_input(input_columns)

        # TODO refactor
        obj = StandardModuleCrudReactTs()
        obj.invoke(
            full_path=full_path,
            namespace=namespace,
            singular_name=singular_name,
            plural_name=plural_name,
            columns=columns,
            input_menu_checkbox=input_menu_checkbox,
            version_api=default_version_api,
            folder_group=default_folder_group
        )


        pause()


