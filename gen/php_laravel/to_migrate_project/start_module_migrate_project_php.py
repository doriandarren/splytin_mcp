from gen.php_laravel.to_migrate_project.standard_module_migrate_proyect_php import standard_module_migrate_proyect_php
from helpers.helper_columns import parse_columns_input
from helpers.helper_menu import menu_checkbox, pause
from helpers.helper_print import input_with_validation


def start_module_migrate_project_php():

    # opt = [
    #     ("Route", "route"),
    #     ("List", "list"),
    #     ("Create", "create"),
    #     ("Edit", "edit"),
    #     ("Barril", "barrel"),
    #     ("Service", "service"),
    # ]

    # input_menu_checkbox = menu_checkbox("Componentes: ", opt)

    default_path_origin = "/Users/dorian/PHPProjects/docker-laravel-84/projects/api.splytin.com"
    default_path_destination = "/Users/dorian/PHPProjects/api.splytin.com"

    full_path_origin = input_with_validation("Carpeta Proyecto ORIGEN", default_path_origin)
    full_path_destination = input_with_validation("Carpeta Proyecto DESTINO", default_path_destination)

    # TODO refactor
    standard_module_migrate_proyect_php(full_path_origin, full_path_destination)


    pause()