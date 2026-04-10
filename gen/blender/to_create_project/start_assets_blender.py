import time

from gen.blender.to_create_project.standard_aseets_blender import standard_aseets_blender
from helpers.helper_columns import parse_columns_input
from helpers.helper_menu import menu_checkbox, pause
from helpers.helper_print import input_with_validation


def start_assets_blender(base_dir):

    opt = [
        ("Assets", "assets"),
    ]

    input_menu_checkbox = menu_checkbox("Componentes: ", opt)
    
    full_path = base_dir + "/_generated/assets" + time.strftime("%Y%m%d%H%M%S")
    
    # TODO refactor
    standard_aseets_blender(full_path, input_menu_checkbox)

    pause()