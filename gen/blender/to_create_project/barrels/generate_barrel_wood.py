import os
from helpers.helper_print import print_message, GREEN, CYAN



def generate_barrel_wood(full_path):
    """
    Genera el archivo
    """

    folder_path = os.path.join(full_path, "barrels")
    file_path = os.path.join(folder_path, "barrel_wood.py")

    os.makedirs(folder_path, exist_ok=True)

    content = r'''import bpy
import bmesh
import math

# =========================================================
# CONFIG
# =========================================================

BARREL_NAME = "BarrelBodyProfile"

# Perfil del barril (radio, altura)
# Altura total: 1.0
PROFILE_POINTS = [
    (0.35, 0.00),
    (0.395, 0.12),
    (0.42, 0.24),
    (0.44, 0.36),
    (0.455, 0.46),
    (0.455, 0.54),
    (0.44, 0.64),
    (0.42, 0.76),
    (0.395, 0.88),
    (0.35, 1.00),
]

SCREW_STEPS = 48
BEVEL_WIDTH = 0.002
BEVEL_SEGMENTS = 2

# Grosor del barril
BARREL_WALL_THICKNESS = 0.025

# Aros
RING_RADIUS_OFFSET = 0.010
RING_THICKNESS = 0.008
RING_POSITIONS_Z = [0.15, 0.31, 0.69, 0.85]

# Tapas
LID_INSET = 0.018
LID_DEPTH = 0.03
LID_VERTICES = 24

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

def add_bevel(obj, width=0.002, segments=2):
    mod = obj.modifiers.new(name="Bevel", type='BEVEL')
    mod.width = width
    mod.segments = segments
    mod.limit_method = 'ANGLE'
    mod.angle_limit = math.radians(30)
    mod.profile = 0.7

def create_material(name, color, roughness=0.7, metallic=0.0):
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
# PERFIL / RADIO POR ALTURA
# =========================================================

def get_radius_at_height(z_world):
    """
    Interpola el radio del perfil según la altura z (0..1).
    """
    if z_world <= PROFILE_POINTS[0][1]:
        return PROFILE_POINTS[0][0]

    if z_world >= PROFILE_POINTS[-1][1]:
        return PROFILE_POINTS[-1][0]

    for i in range(len(PROFILE_POINTS) - 1):
        r1, z1 = PROFILE_POINTS[i]
        r2, z2 = PROFILE_POINTS[i + 1]

        if z1 <= z_world <= z2:
            t = (z_world - z1) / (z2 - z1)
            return r1 + (r2 - r1) * t

    return PROFILE_POINTS[-1][0]

# =========================================================
# CREAR PERFIL Y REVOLUCIONAR
# =========================================================

def create_barrel_body_from_profile():
    mesh = bpy.data.meshes.new(BARREL_NAME + "_Mesh")
    obj = bpy.data.objects.new(BARREL_NAME, mesh)
    bpy.context.collection.objects.link(obj)

    bm = bmesh.new()

    verts = []
    for radius, z in PROFILE_POINTS:
        v = bm.verts.new((radius, 0.0, z))
        verts.append(v)

    bm.verts.ensure_lookup_table()

    for i in range(len(verts) - 1):
        bm.edges.new((verts[i], verts[i + 1]))

    bm.to_mesh(mesh)
    bm.free()

    obj.location = (0.0, 0.0, 0.0)

    # Revolución con Screw
    screw = obj.modifiers.new(name="Screw", type='SCREW')
    screw.axis = 'Z'
    screw.angle = math.radians(360.0)
    screw.steps = SCREW_STEPS
    screw.render_steps = SCREW_STEPS
    screw.use_merge_vertices = True
    screw.merge_threshold = 0.0001
    screw.screw_offset = 0.0

    # Grosor
    solidify = obj.modifiers.new(name="Solidify", type='SOLIDIFY')
    solidify.thickness = BARREL_WALL_THICKNESS
    solidify.offset = 0.0

    deselect_all()
    set_active(obj)
    bpy.ops.object.modifier_apply(modifier=screw.name)
    bpy.ops.object.modifier_apply(modifier=solidify.name)

    # Ajustar para que la base quede en z=0
    obj.location.z = 0.0
    bpy.context.view_layer.update()
    min_z = min((obj.matrix_world @ v.co).z for v in obj.data.vertices)
    obj.location.z -= min_z

    apply_transform(obj)
    add_bevel(obj, BEVEL_WIDTH, BEVEL_SEGMENTS)
    shade_smooth(obj, 30)

    return obj

# =========================================================
# AROS
# =========================================================

def create_ring(z_pos, index):
    radius = get_radius_at_height(z_pos) + RING_RADIUS_OFFSET

    bpy.ops.mesh.primitive_torus_add(
        major_radius=radius,
        minor_radius=RING_THICKNESS,
        location=(0.0, 0.0, z_pos),
        major_segments=72,
        minor_segments=12
    )

    ring = bpy.context.object
    ring.name = f"{BARREL_NAME}_Ring_{index}"

    ring_widths = [3.8, 5.4, 5.4, 3.8]
    ring.scale.z = ring_widths[index]

    apply_transform(ring)

    add_bevel(ring, 0.0008, 2)
    shade_smooth(ring, 30)

    return ring

def create_rings():
    rings = []
    for i, z in enumerate(RING_POSITIONS_Z):
        rings.append(create_ring(z, i))
    return rings

# =========================================================
# TAPAS
# =========================================================

def create_lid(z_pos, top=True):
    radius = get_radius_at_height(z_pos) - LID_INSET

    bpy.ops.mesh.primitive_cylinder_add(
        vertices=LID_VERTICES,
        radius=radius,
        depth=LID_DEPTH,
        location=(0.0, 0.0, z_pos)
    )

    lid = bpy.context.object
    lid.name = f"{BARREL_NAME}_{'TopLid' if top else 'BottomLid'}"

    apply_transform(lid)
    add_bevel(lid, 0.0015, 2)
    shade_smooth(lid, 30)

    return lid

def create_lids():
    top_lid = create_lid(1.0 - LID_DEPTH / 2, top=True)
    bottom_lid = create_lid(LID_DEPTH / 2, top=False)
    return [top_lid, bottom_lid]

# =========================================================
# MAIN
# =========================================================

def build_barrel_body_profile():
    mat_wood = create_material(
        "Mat_BarrelBodyProfile",
        (0.42, 0.28, 0.14, 1.0),
        roughness=0.78,
        metallic=0.0
    )

    mat_metal = create_material(
        "Mat_BarrelMetalProfile",
        (0.12, 0.12, 0.12, 1.0),
        roughness=0.45,
        metallic=0.45
    )

    barrel = create_barrel_body_from_profile()
    assign_material(barrel, mat_wood)

    lids = create_lids()
    for lid in lids:
        assign_material(lid, mat_wood)

    rings = create_rings()
    for ring in rings:
        assign_material(ring, mat_metal)

    print("Barril completo creado correctamente.")

build_barrel_body_profile()
'''

    try:
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)
        
        
        
        
        




