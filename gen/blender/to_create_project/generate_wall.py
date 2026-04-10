import os
from helpers.helper_print import print_message, GREEN, CYAN

def generate_wall(full_path):
    create_wall_lisa(full_path)
    create_stone_wall_blocks(full_path)




def create_wall_lisa(full_path):
    """
    Genera el archivo
    """

    folder_path = os.path.join(full_path, "wall")
    file_path = os.path.join(folder_path, "wall_lisa.py")

    os.makedirs(folder_path, exist_ok=True)

    content = r'''import bpy

def create_old_wall(name="SM_OldWall", location=(0,0,0)):
    # Crear pared base
    bpy.ops.mesh.primitive_plane_add(size=2, location=location)
    wall = bpy.context.active_object
    wall.name = name

    # Subdividir para permitir displacement
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.subdivide(number_cuts=50)
    bpy.ops.object.mode_set(mode='OBJECT')

    # Crear material
    mat = bpy.data.materials.new(name="WallMaterial")
    mat.use_nodes = True

    nodes = mat.node_tree.nodes
    links = mat.node_tree.links

    nodes.clear()

    # Nodos
    output = nodes.new(type='ShaderNodeOutputMaterial')
    bsdf = nodes.new(type='ShaderNodeBsdfPrincipled')
    tex = nodes.new(type='ShaderNodeTexImage')
    disp = nodes.new(type='ShaderNodeDisplacement')

    # Cargar imagen (CAMBIA ESTA RUTA)
    tex.image = bpy.data.images.load("/ruta/a/tu/textura.jpg")

    # Conexiones
    links.new(tex.outputs['Color'], bsdf.inputs['Base Color'])
    links.new(bsdf.outputs['BSDF'], output.inputs['Surface'])
    links.new(tex.outputs['Color'], disp.inputs['Height'])
    links.new(disp.outputs['Displacement'], output.inputs['Displacement'])

    # Ajustes
    disp.inputs['Scale'].default_value = 0.2

    wall.data.materials.append(mat)

    # Activar displacement real
    bpy.context.scene.cycles.feature_set = 'EXPERIMENTAL'
    mat.cycles.displacement_method = 'BOTH'

    return wall

create_old_wall()
'''

    try:
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)
        
        
        
        
def create_stone_wall_blocks(full_path):
    """
    Genera el archivo
    """

    folder_path = os.path.join(full_path, "wall")
    file_path = os.path.join(folder_path, "wall_texture.py")

    os.makedirs(folder_path, exist_ok=True)

    content = r'''import bpy
import bmesh
import random
import math


def create_material(name, color):
    mat = bpy.data.materials.new(name=name)
    mat.use_nodes = False
    mat.diffuse_color = color
    return mat


def create_pbr_stone_material(name="Stone_PBR"):
    mat = bpy.data.materials.new(name=name)
    mat.use_nodes = True

    nodes = mat.node_tree.nodes
    links = mat.node_tree.links
    nodes.clear()

    output = nodes.new(type='ShaderNodeOutputMaterial')
    output.location = (500, 0)

    principled = nodes.new(type='ShaderNodeBsdfPrincipled')
    principled.location = (200, 0)
    principled.inputs["Specular IOR Level"].default_value = 0.3

    links.new(principled.outputs["BSDF"], output.inputs["Surface"])

    tex_coord = nodes.new(type='ShaderNodeTexCoord')
    tex_coord.location = (-1200, 0)

    mapping = nodes.new(type='ShaderNodeMapping')
    mapping.location = (-1000, 0)
    mapping.inputs["Scale"].default_value = (1.5, 1.5, 1.5)

    links.new(tex_coord.outputs["Object"], mapping.inputs["Vector"])

    # Base color
    noise_color = nodes.new(type='ShaderNodeTexNoise')
    noise_color.location = (-800, 220)
    noise_color.inputs["Scale"].default_value = 7.0
    noise_color.inputs["Detail"].default_value = 8.0
    noise_color.inputs["Roughness"].default_value = 0.5

    color_ramp = nodes.new(type='ShaderNodeValToRGB')
    color_ramp.location = (-550, 220)
    color_ramp.color_ramp.elements[0].position = 0.25
    color_ramp.color_ramp.elements[0].color = (0.22, 0.20, 0.18, 1.0)
    color_ramp.color_ramp.elements[1].position = 0.85
    color_ramp.color_ramp.elements[1].color = (0.52, 0.48, 0.42, 1.0)

    links.new(mapping.outputs["Vector"], noise_color.inputs["Vector"])
    links.new(noise_color.outputs["Fac"], color_ramp.inputs["Fac"])
    links.new(color_ramp.outputs["Color"], principled.inputs["Base Color"])

    # Roughness
    noise_rough = nodes.new(type='ShaderNodeTexNoise')
    noise_rough.location = (-800, -40)
    noise_rough.inputs["Scale"].default_value = 10.0
    noise_rough.inputs["Detail"].default_value = 5.0

    rough_ramp = nodes.new(type='ShaderNodeValToRGB')
    rough_ramp.location = (-550, -40)
    rough_ramp.color_ramp.elements[0].color = (0.55, 0.55, 0.55, 1.0)
    rough_ramp.color_ramp.elements[1].color = (0.9, 0.9, 0.9, 1.0)

    links.new(mapping.outputs["Vector"], noise_rough.inputs["Vector"])
    links.new(noise_rough.outputs["Fac"], rough_ramp.inputs["Fac"])
    links.new(rough_ramp.outputs["Color"], principled.inputs["Roughness"])

    # Normal / bump
    noise_normal = nodes.new(type='ShaderNodeTexNoise')
    noise_normal.location = (-800, -320)
    noise_normal.inputs["Scale"].default_value = 22.0
    noise_normal.inputs["Detail"].default_value = 10.0
    noise_normal.inputs["Roughness"].default_value = 0.65

    bump = nodes.new(type='ShaderNodeBump')
    bump.location = (-550, -320)
    bump.inputs["Strength"].default_value = 0.18
    bump.inputs["Distance"].default_value = 0.02

    links.new(mapping.outputs["Vector"], noise_normal.inputs["Vector"])
    links.new(noise_normal.outputs["Fac"], bump.inputs["Height"])
    links.new(bump.outputs["Normal"], principled.inputs["Normal"])

    return mat


def deform_stone(obj, strength=0.06):
    mesh = obj.data
    bm = bmesh.new()
    bm.from_mesh(mesh)

    for vert in bm.verts:
        vert.co.x += random.uniform(-strength, strength)
        vert.co.y += random.uniform(-strength, strength)
        vert.co.z += random.uniform(-strength, strength)

    bm.to_mesh(mesh)
    bm.free()


def add_bevel_modifier(obj, width=0.02, segments=2):
    bevel = obj.modifiers.new(name="Bevel", type='BEVEL')
    bevel.width = width
    bevel.segments = segments
    bevel.limit_method = 'ANGLE'


def create_back_fill_wall(name, location, width, height, depth, color=(0.24, 0.22, 0.19, 1.0)):
    x, y, z = location

    bpy.ops.mesh.primitive_cube_add(
        location=(x, y - depth / 2, z + height / 2)
    )
    back_wall = bpy.context.active_object
    back_wall.name = name

    back_wall.scale[0] = width / 2
    back_wall.scale[1] = depth / 2
    back_wall.scale[2] = height / 2

    bpy.context.view_layer.objects.active = back_wall
    back_wall.select_set(True)
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)

    mat = create_material(f"{name}_Mat", color)
    back_wall.data.materials.append(mat)

    return back_wall


def create_single_stone(
    name,
    location=(0, 0, 0),
    width=1.0,
    height=0.5,
    depth=0.35,
    deform_strength=0.05,
    bevel_width=0.02,
    bevel_segments=2,
    material=None
):
    x, y, z = location

    bpy.ops.mesh.primitive_cube_add(location=(x, y, z))
    stone = bpy.context.active_object
    stone.name = name

    stone.scale[0] = width / 2
    stone.scale[1] = depth / 2
    stone.scale[2] = height / 2

    bpy.context.view_layer.objects.active = stone
    stone.select_set(True)
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)

    stone.rotation_euler[0] = math.radians(random.uniform(-4, 4))
    stone.rotation_euler[1] = math.radians(random.uniform(-4, 4))
    stone.rotation_euler[2] = math.radians(random.uniform(-3, 3))

    bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)

    deform_stone(stone, strength=deform_strength)

    if material:
        stone.data.materials.append(material)

    add_bevel_modifier(
        stone,
        width=bevel_width,
        segments=bevel_segments
    )

    return stone


def create_stone_wall_pro(
    name="SM_StoneWall_01",
    location=(0, 0, 0),
    wall_width=4.0,
    wall_height=2.5,
    wall_depth=0.35,
    rows=5,
    min_stone_width=0.45,
    max_stone_width=1.0,
    min_stone_height=0.28,
    max_stone_height=0.55,
    joint_gap=0.03,
    irregularity=0.04,
    deform_strength=0.05,
    bevel_width=0.02,
    bevel_segments=2,
    back_fill_depth=0.08
):
    base_x, base_y, base_z = location

    stone_material = create_pbr_stone_material(f"{name}_PBR_Stone")

    back_wall = create_back_fill_wall(
        name=f"{name}_BackFill",
        location=(base_x, base_y, base_z + 0.04),
        width=wall_width + 0.1,
        height=wall_height - 0.08,
        depth=back_fill_depth
    )

    created_stones = []
    current_z = base_z

    for row in range(rows):
        row_height = random.uniform(min_stone_height, max_stone_height)
        current_x = base_x - wall_width / 2

        row_offset = random.uniform(-0.15, 0.15)
        current_x += row_offset

        while current_x < base_x + wall_width / 2:
            stone_width = random.uniform(min_stone_width, max_stone_width)
            stone_depth = wall_depth + random.uniform(-0.03, 0.04)

            remaining = (base_x + wall_width / 2) - current_x
            if remaining <= min_stone_width * 0.5:
                break
            if stone_width > remaining:
                stone_width = remaining

            pos_x = current_x + stone_width / 2 + random.uniform(-irregularity, irregularity)
            pos_y = base_y + random.uniform(-0.015, 0.015)
            pos_z = current_z + row_height / 2 + random.uniform(-irregularity, irregularity)

            stone = create_single_stone(
                name=f"{name}_Stone_{row}_{len(created_stones)}",
                location=(pos_x, pos_y, pos_z),
                width=stone_width,
                height=row_height,
                depth=stone_depth,
                deform_strength=deform_strength,
                bevel_width=bevel_width,
                bevel_segments=bevel_segments,
                material=stone_material
            )

            created_stones.append(stone)
            current_x += stone_width + joint_gap

        current_z += row_height + joint_gap

        if current_z >= base_z + wall_height:
            break

    collection_name = name
    collection = bpy.data.collections.get(collection_name)
    if not collection:
        collection = bpy.data.collections.new(collection_name)
        bpy.context.scene.collection.children.link(collection)

    all_objects = [back_wall] + created_stones

    for obj in all_objects:
        for col in obj.users_collection:
            col.objects.unlink(obj)
        collection.objects.link(obj)

    return {
        "status": "success",
        "message": f"Stone wall '{name}' created successfully",
        "stones_count": len(created_stones),
        "collection": collection.name
    }


create_stone_wall_pro()
'''

    try:
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)