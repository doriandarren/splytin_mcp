import os
from helpers.helper_print import print_message, GREEN, CYAN



def generate_barrel_metal(full_path):
    """
    Genera el archivo
    """

    folder_path = os.path.join(full_path, "barrels")
    file_path = os.path.join(folder_path, "barrel_metal.py")

    os.makedirs(folder_path, exist_ok=True)

    content = r'''import bpy
import bmesh
import math

# =========================================================
# CONFIG
# =========================================================

BARREL_NAME = "SteelDrum"

# Dimensiones
DRUM_RADIUS = 0.30
DRUM_HEIGHT = 0.90
DRUM_SEGMENTS = 48

# Tapas
LID_INSET = 0.01
LID_DEPTH = 0.02

# Nervios / bandas
BAND_RADIUS_OFFSET = 0.0025
BAND_THICKNESS = 0.006
BAND_WIDTH_SCALE = 2.2
BAND_POSITIONS_Z = [0.18, 0.45, 0.72]

# Bevel
BODY_BEVEL_WIDTH = 0.0015
BODY_BEVEL_SEGMENTS = 2
BAND_BEVEL_WIDTH = 0.0008
BAND_BEVEL_SEGMENTS = 2

# =========================================================
# UTILIDADES
# =========================================================

def deselect_all():
    for obj in bpy.context.selected_objects:
        obj.select_set(False)

def set_active(obj):
    bpy.context.view_layer.objects.active = obj
    obj.select_set(True)

def apply_transform(obj):
    deselect_all()
    set_active(obj)
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    obj.select_set(False)

def shade_smooth(obj, angle_deg=30):
    deselect_all()
    set_active(obj)
    bpy.ops.object.shade_smooth()

    if hasattr(obj.data, "use_auto_smooth"):
        obj.data.use_auto_smooth = True

    if hasattr(obj.data, "auto_smooth_angle"):
        obj.data.auto_smooth_angle = math.radians(angle_deg)

    obj.select_set(False)

def add_bevel(obj, width=0.0015, segments=2):
    mod = obj.modifiers.new(name="Bevel", type='BEVEL')
    mod.width = width
    mod.segments = segments
    mod.limit_method = 'ANGLE'
    mod.angle_limit = math.radians(30)
    mod.profile = 0.7

def create_material(name, color, roughness=0.5, metallic=0.0):
    mat = bpy.data.materials.get(name)
    if mat:
        return mat

    mat = bpy.data.materials.new(name=name)
    mat.use_nodes = True
    bsdf = mat.node_tree.nodes["Principled BSDF"]
    bsdf.inputs["Base Color"].default_value = color
    bsdf.inputs["Roughness"].default_value = roughness
    bsdf.inputs["Metallic"].default_value = metallic
    return mat

def assign_material(obj, mat):
    if obj.data.materials:
        obj.data.materials[0] = mat
    else:
        obj.data.materials.append(mat)

# =========================================================
# CUERPO
# =========================================================

def create_drum_body():
    bpy.ops.mesh.primitive_cylinder_add(
        vertices=DRUM_SEGMENTS,
        radius=DRUM_RADIUS,
        depth=DRUM_HEIGHT,
        location=(0.0, 0.0, DRUM_HEIGHT / 2)
    )

    body = bpy.context.object
    body.name = f"{BARREL_NAME}_Body"

    apply_transform(body)
    add_bevel(body, BODY_BEVEL_WIDTH, BODY_BEVEL_SEGMENTS)
    shade_smooth(body, 30)

    return body

# =========================================================
# TAPAS
# =========================================================

def create_lid(z_pos, top=True):
    bpy.ops.mesh.primitive_cylinder_add(
        vertices=DRUM_SEGMENTS,
        radius=DRUM_RADIUS - LID_INSET,
        depth=LID_DEPTH,
        location=(0.0, 0.0, z_pos)
    )

    lid = bpy.context.object
    lid.name = f"{BARREL_NAME}_{'TopLid' if top else 'BottomLid'}"

    apply_transform(lid)
    add_bevel(lid, 0.001, 2)
    shade_smooth(lid, 30)

    return lid

def create_lids():
    top_lid = create_lid(DRUM_HEIGHT - LID_DEPTH / 2, top=True)
    bottom_lid = create_lid(LID_DEPTH / 2, top=False)
    return [top_lid, bottom_lid]

# =========================================================
# BANDAS PEQUEÑAS
# =========================================================

def create_band(z_pos, index):
    bpy.ops.mesh.primitive_torus_add(
        major_radius=DRUM_RADIUS + BAND_RADIUS_OFFSET,
        minor_radius=BAND_THICKNESS,
        location=(0.0, 0.0, z_pos),
        major_segments=72,
        minor_segments=12
    )

    band = bpy.context.object
    band.name = f"{BARREL_NAME}_Band_{index}"

    band.scale.z = BAND_WIDTH_SCALE
    apply_transform(band)

    add_bevel(band, BAND_BEVEL_WIDTH, BAND_BEVEL_SEGMENTS)
    shade_smooth(band, 30)

    return band

def create_bands():
    bands = []
    for i, z in enumerate(BAND_POSITIONS_Z):
        bands.append(create_band(z, i))
    return bands

# =========================================================
# MAIN
# =========================================================

def build_steel_drum():
    mat_body = create_material(
        "Mat_SteelDrumBody",
        (0.08, 0.18, 0.55, 1.0),
        roughness=0.42,
        metallic=0.85
    )

    mat_band = create_material(
        "Mat_SteelDrumBand",
        (0.10, 0.10, 0.10, 1.0),
        roughness=0.38,
        metallic=0.9
    )

    body = create_drum_body()
    assign_material(body, mat_body)

    lids = create_lids()
    for lid in lids:
        assign_material(lid, mat_body)

    bands = create_bands()
    for band in bands:
        assign_material(band, mat_band)

    print("Barril de acero creado correctamente.")

build_steel_drum()
'''

    try:
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)