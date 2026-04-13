import os
from gen.blender.to_create_project.barrels.generate_barrel_metal import generate_barrel_metal
from gen.blender.to_create_project.barrels.generate_barrel_wood import generate_barrel_wood
from gen.blender.to_create_project.generate_door import generate_door
from gen.blender.to_create_project.generate_tree import generate_tree
from gen.blender.to_create_project.generate_wall import generate_wall
from helpers.helper_menu import pause


def standard_aseets_blender(full_path, input_menu_checkbox=None):

    # Input Default
    if input_menu_checkbox is None:
        input_menu_checkbox = ["assets"]


    if "assets" in input_menu_checkbox:
        generate_wall(full_path)
        generate_tree(full_path)
        generate_door(full_path)
        generate_barrel_wood(full_path)
        generate_barrel_metal(full_path)
        
        