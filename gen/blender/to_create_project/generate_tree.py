import os
from helpers.helper_print import print_message, GREEN, CYAN

def generate_tree(full_path):
    """
    Genera el archivo
    """

    folder_path = os.path.join(full_path, "tree")
    file_path = os.path.join(folder_path, "tree.py")

    os.makedirs(folder_path, exist_ok=True)

    content = r'''import bpy
import bmesh
import random

def create_material(name, color):
    mat = bpy.data.materials.new(name=name)
    mat.use_nodes = False
    mat.diffuse_color = color
    return mat

def deform_trunk(obj, strength=0.08):
    mesh = obj.data
    bm = bmesh.new()
    bm.from_mesh(mesh)

    for vert in bm.verts:
        # Deformar más en X e Y para romper la forma perfecta
        vert.co.x += random.uniform(-strength, strength)
        vert.co.y += random.uniform(-strength, strength)

        # Un poco de variación en Z, pero mucho menos
        vert.co.z += random.uniform(-strength * 0.15, strength * 0.15)

    bm.to_mesh(mesh)
    bm.free()

def deform_leaves(obj, strength=0.12):
    mesh = obj.data
    bm = bmesh.new()
    bm.from_mesh(mesh)

    for vert in bm.verts:
        vert.co.x += random.uniform(-strength, strength)
        vert.co.y += random.uniform(-strength, strength)
        vert.co.z += random.uniform(-strength, strength)

    bm.to_mesh(mesh)
    bm.free()

def create_tree(name="Tree", location=(0, 0, 0)):
    x, y, z = location

    # Tronco
    bpy.ops.mesh.primitive_cylinder_add(
        vertices=10,
        radius=0.2,
        depth=2,
        location=(x, y, z + 1)
    )
    trunk = bpy.context.active_object
    trunk.name = f"{name}_Trunk"

    # Deformar el tronco para que no quede tan perfecto
    deform_trunk(trunk, strength=0.05)

    # Material tronco
    trunk_mat = create_material(
        f"{name}_Trunk_Mat",
        (0.36, 0.20, 0.09, 1.0)
    )
    trunk.data.materials.append(trunk_mat)

    # Copa base
    bpy.ops.mesh.primitive_ico_sphere_add(
        subdivisions=2,
        radius=1,
        location=(x, y, z + 2.5)
    )
    leaves = bpy.context.active_object
    leaves.name = f"{name}_Leaves"

    # Escala irregular
    leaves.scale[0] = random.uniform(0.9, 1.15)
    leaves.scale[1] = random.uniform(0.9, 1.15)
    leaves.scale[2] = random.uniform(0.95, 1.2)

    # Deformar copa
    deform_leaves(leaves, strength=0.12)

    # Material copa
    leaves_mat = create_material(
        f"{name}_Leaves_Mat",
        (0.10, 0.45, 0.12, 1.0)
    )
    leaves.data.materials.append(leaves_mat)

create_tree()
'''

    try:
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)