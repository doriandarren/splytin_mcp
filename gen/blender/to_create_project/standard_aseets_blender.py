import os
from gen.blender.to_create_project.generate_wall import generate_wall
from helpers.helper_menu import pause
from helpers.helper_print import camel_to_kebab, camel_to_snake
from helpers.helper_string import normalize_project_name


def standard_aseets_blender(full_path, input_menu_checkbox=None):

    # Input Default
    if input_menu_checkbox is None:
        input_menu_checkbox = ["assets"]


    if "assets" in input_menu_checkbox:
        generate_wall(full_path)
        