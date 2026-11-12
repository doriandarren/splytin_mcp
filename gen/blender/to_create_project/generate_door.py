import os
from helpers.helper_print import print_message, GREEN, CYAN


def generate_door(full_path):
    create_basic_door(full_path)



def create_basic_door(full_path):
    """
    Genera el archivo
    """

    folder_path = os.path.join(full_path, "doors")
    file_path = os.path.join(folder_path, "door_basic.py")

    os.makedirs(folder_path, exist_ok=True)

    content = f'''import bpy
import bmesh
import math
from mathutils import Vector

# =========================================================
# CONFIG
# =========================================================

DOOR_NAME = "DoorWithFrame"

DOOR_WIDTH = 0.82
DOOR_HEIGHT = 2.04
DOOR_THICKNESS = 0.04

BASE_LOCATION = (0.0, 0.0, DOOR_HEIGHT / 2)

# Paneles
PANEL_MARGIN_X = 0.11
PANEL_MARGIN_TOP = 0.14
PANEL_MARGIN_BOTTOM = 0.20
PANEL_GAP_X = 0.08
PANEL_GAP_Y = 0.12

TOP_PANEL_HEIGHT_RATIO = 0.72
BOTTOM_PANEL_HEIGHT_RATIO = 1.30

# Relieve
OUTER_INSET = 0.022
INNER_INSET = 0.012
PANEL_RECESS = 0.012

# Bevel puerta
BEVEL_WIDTH = 0.002
BEVEL_SEGMENTS = 2

# Pomo
KNOB_HEIGHT = 0.96
KNOB_OFFSET_FROM_EDGE = 0.075

KNOB_RADIUS = 0.022
KNOB_SCALE_Y = 0.72

ROSETTE_RADIUS = 0.028
ROSETTE_DEPTH = 0.008

NECK_RADIUS = 0.010
NECK_LENGTH = 0.028

SPINDLE_RADIUS = 0.005
SPINDLE_EXTRA = 0.010

# Marco
FRAME_SIDE_WIDTH = 0.09
FRAME_TOP_HEIGHT = 0.09
FRAME_DEPTH = 0.06
FRAME_GAP = 0.005

FRAME_BEVEL_WIDTH = 0.0025
FRAME_BEVEL_SEGMENTS = 2

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

def create_material(name, color, roughness=0.42, metallic=0.0):
    mat = bpy.data.materials.get(name)
    if mat:
        return mat

    mat = bpy.data.materials.new(name=name)
    mat.use_nodes = True
    bsdf = mat.node_tree.nodes.get("Principled BSDF")
    bsdf.inputs["Base Color"].default_value = color
    bsdf.inputs["Roughness"].default_value = roughness
    bsdf.inputs["Metallic"].default_value = metallic
    return mat

def assign_material(obj, mat):
    if obj.data.materials:
        obj.data.materials[0] = mat
    else:
        obj.data.materials.append(mat)

def add_bevel(obj, width=0.002, segments=2):
    mod = obj.modifiers.new(name="Bevel", type='BEVEL')
    mod.width = width
    mod.segments = segments
    mod.limit_method = 'ANGLE'
    mod.angle_limit = math.radians(30)
    mod.profile = 0.7

def join_objects(objs, new_name):
    deselect_all()
    for obj in objs:
        obj.select_set(True)
    bpy.context.view_layer.objects.active = objs[0]
    bpy.ops.object.join()
    result = bpy.context.object
    result.name = new_name
    return result

# =========================================================
# CREAR HOJA
# =========================================================

def create_door_leaf():
    bpy.ops.mesh.primitive_cube_add(location=BASE_LOCATION)
    door = bpy.context.object
    door.name = DOOR_NAME
    door.dimensions = (DOOR_WIDTH, DOOR_THICKNESS, DOOR_HEIGHT)
    apply_transform(door)
    return door

# =========================================================
# PANELES EN COORDENADAS LOCALES
# =========================================================

def make_panel_boxes_local():
    left = -DOOR_WIDTH / 2 + PANEL_MARGIN_X
    right = DOOR_WIDTH / 2 - PANEL_MARGIN_X

    bottom = -DOOR_HEIGHT / 2 + PANEL_MARGIN_BOTTOM
    top = DOOR_HEIGHT / 2 - PANEL_MARGIN_TOP

    total_inner_width = right - left
    col_width = (total_inner_width - PANEL_GAP_X) / 2.0

    total_inner_height = top - bottom - PANEL_GAP_Y
    ratio_sum = TOP_PANEL_HEIGHT_RATIO + BOTTOM_PANEL_HEIGHT_RATIO

    top_h = total_inner_height * (TOP_PANEL_HEIGHT_RATIO / ratio_sum)
    bottom_h = total_inner_height * (BOTTOM_PANEL_HEIGHT_RATIO / ratio_sum)

    boxes = []

    # inferior izquierda
    boxes.append((left, left + col_width, bottom, bottom + bottom_h))
    # inferior derecha
    boxes.append((left + col_width + PANEL_GAP_X, right, bottom, bottom + bottom_h))
    # superior izquierda
    boxes.append((
        left,
        left + col_width,
        bottom + bottom_h + PANEL_GAP_Y,
        bottom + bottom_h + PANEL_GAP_Y + top_h
    ))
    # superior derecha
    boxes.append((
        left + col_width + PANEL_GAP_X,
        right,
        bottom + bottom_h + PANEL_GAP_Y,
        bottom + bottom_h + PANEL_GAP_Y + top_h
    ))

    return boxes

def bisect_at_x(bm, x_value):
    geom = bm.verts[:] + bm.edges[:] + bm.faces[:]
    bmesh.ops.bisect_plane(
        bm,
        geom=geom,
        plane_co=Vector((x_value, 0.0, 0.0)),
        plane_no=Vector((1.0, 0.0, 0.0)),
        clear_outer=False,
        clear_inner=False
    )

def bisect_at_z(bm, z_value):
    geom = bm.verts[:] + bm.edges[:] + bm.faces[:]
    bmesh.ops.bisect_plane(
        bm,
        geom=geom,
        plane_co=Vector((0.0, 0.0, z_value)),
        plane_no=Vector((0.0, 0.0, 1.0)),
        clear_outer=False,
        clear_inner=False
    )

def cut_face_exact(bm, boxes):
    x_values = set()
    z_values = set()

    for x0, x1, z0, z1 in boxes:
        x_values.add(round(x0, 6))
        x_values.add(round(x1, 6))
        z_values.add(round(z0, 6))
        z_values.add(round(z1, 6))

    for x in sorted(x_values):
        bisect_at_x(bm, x)

    for z in sorted(z_values):
        bisect_at_z(bm, z)

    bmesh.ops.remove_doubles(bm, verts=bm.verts, dist=0.00001)

def get_side_faces(bm, front=True):
    target_y = max(v.co.y for v in bm.verts) if front else min(v.co.y for v in bm.verts)
    normal_check = (lambda n: n.y > 0.95) if front else (lambda n: n.y < -0.95)

    faces = []
    for f in bm.faces:
        c = f.calc_center_median()
        if normal_check(f.normal) and abs(c.y - target_y) < 1e-4:
            faces.append(f)
    return faces

def face_in_box(face, box):
    x0, x1, z0, z1 = box
    c = face.calc_center_median()
    eps = 1e-5
    return (x0 + eps) < c.x < (x1 - eps) and (z0 + eps) < c.z < (z1 - eps)

def create_panel_relief_on_side(bm, boxes, front=True):
    side_faces = get_side_faces(bm, front=front)

    panel_faces = []
    for box in boxes:
        matches = [f for f in side_faces if face_in_box(f, box)]
        if not matches:
            continue
        biggest = max(matches, key=lambda f: f.calc_area())
        panel_faces.append(biggest)

    final_inner_faces = []

    for face in panel_faces:
        res1 = bmesh.ops.inset_individual(
            bm,
            faces=[face],
            thickness=OUTER_INSET,
            depth=0.0
        )

        faces1 = [f for f in res1["faces"] if isinstance(f, bmesh.types.BMFace)]
        if not faces1:
            continue

        inner_face_1 = max(faces1, key=lambda f: f.calc_area())

        res2 = bmesh.ops.inset_individual(
            bm,
            faces=[inner_face_1],
            thickness=INNER_INSET,
            depth=0.0
        )

        faces2 = [f for f in res2["faces"] if isinstance(f, bmesh.types.BMFace)]
        if not faces2:
            continue

        inner_face_2 = max(faces2, key=lambda f: f.calc_area())
        final_inner_faces.append(inner_face_2)

    direction = -1.0 if front else 1.0

    for f in final_inner_faces:
        bmesh.ops.translate(
            bm,
            verts=list(set(f.verts)),
            vec=Vector((0.0, direction * PANEL_RECESS, 0.0))
        )

def create_panel_relief_both_sides(door):
    bm = bmesh.new()
    bm.from_mesh(door.data)
    bm.faces.ensure_lookup_table()
    bm.edges.ensure_lookup_table()
    bm.verts.ensure_lookup_table()

    boxes = make_panel_boxes_local()

    cut_face_exact(bm, boxes)

    bm.faces.ensure_lookup_table()
    bm.edges.ensure_lookup_table()
    bm.verts.ensure_lookup_table()

    create_panel_relief_on_side(bm, boxes, front=True)

    bm.faces.ensure_lookup_table()
    bm.edges.ensure_lookup_table()
    bm.verts.ensure_lookup_table()

    create_panel_relief_on_side(bm, boxes, front=False)

    bm.normal_update()
    bm.to_mesh(door.data)
    bm.free()

# =========================================================
# POMO REALISTA
# =========================================================

def create_rosette(name, location, rotation_x_deg=90):
    bpy.ops.mesh.primitive_cylinder_add(
        radius=ROSETTE_RADIUS,
        depth=ROSETTE_DEPTH,
        location=location
    )
    obj = bpy.context.object
    obj.name = name
    obj.rotation_euler.x = math.radians(rotation_x_deg)
    return obj

def create_neck(name, location, length):
    bpy.ops.mesh.primitive_cylinder_add(
        radius=NECK_RADIUS,
        depth=length,
        location=location
    )
    obj = bpy.context.object
    obj.name = name
    obj.rotation_euler.x = math.radians(90)
    return obj

def create_knob_body(name, location):
    bpy.ops.mesh.primitive_uv_sphere_add(
        radius=KNOB_RADIUS,
        location=location,
        segments=32,
        ring_count=16
    )
    obj = bpy.context.object
    obj.name = name
    obj.scale.y = KNOB_SCALE_Y
    apply_transform(obj)
    return obj

def create_spindle(name, location, depth):
    bpy.ops.mesh.primitive_cylinder_add(
        radius=SPINDLE_RADIUS,
        depth=depth,
        location=location
    )
    obj = bpy.context.object
    obj.name = name
    obj.rotation_euler.x = math.radians(90)
    return obj

def create_realistic_knob():
    x = DOOR_WIDTH / 2 - KNOB_OFFSET_FROM_EDGE
    z = -DOOR_HEIGHT / 2 + KNOB_HEIGHT

    front_surface_y = DOOR_THICKNESS / 2
    back_surface_y = -DOOR_THICKNESS / 2

    front_rosette_y = front_surface_y + ROSETTE_DEPTH / 2
    back_rosette_y = back_surface_y - ROSETTE_DEPTH / 2

    front_neck_y = front_surface_y + ROSETTE_DEPTH + NECK_LENGTH / 2
    back_neck_y = back_surface_y - ROSETTE_DEPTH - NECK_LENGTH / 2

    front_knob_y = front_surface_y + ROSETTE_DEPTH + NECK_LENGTH + KNOB_RADIUS * 0.72
    back_knob_y = back_surface_y - ROSETTE_DEPTH - NECK_LENGTH - KNOB_RADIUS * 0.72

    spindle_depth = DOOR_THICKNESS + ROSETTE_DEPTH * 2 + SPINDLE_EXTRA

    parts = []

    parts.append(create_rosette("KnobFrontRosette", (x, front_rosette_y, z)))
    parts.append(create_rosette("KnobBackRosette", (x, back_rosette_y, z)))

    parts.append(create_neck("KnobFrontNeck", (x, front_neck_y, z), NECK_LENGTH))
    parts.append(create_neck("KnobBackNeck", (x, back_neck_y, z), NECK_LENGTH))

    parts.append(create_knob_body("KnobFrontBody", (x, front_knob_y, z)))
    parts.append(create_knob_body("KnobBackBody", (x, back_knob_y, z)))

    parts.append(create_spindle("KnobSpindle", (x, 0.0, z), spindle_depth))

    knob = join_objects(parts, "DoorKnobRealistic")
    return knob

# =========================================================
# MARCO
# =========================================================

def create_frame_piece(name, location, dimensions):
    bpy.ops.mesh.primitive_cube_add(location=location)
    obj = bpy.context.object
    obj.name = name
    obj.dimensions = dimensions
    apply_transform(obj)
    return obj

def create_door_frame():
    outer_width = DOOR_WIDTH + FRAME_SIDE_WIDTH * 2 + FRAME_GAP * 2
    outer_height = DOOR_HEIGHT + FRAME_TOP_HEIGHT + FRAME_GAP * 2

    frame_y = FRAME_DEPTH / 2 - ((FRAME_DEPTH - DOOR_THICKNESS) / 2)

    left_x = BASE_LOCATION[0] - DOOR_WIDTH / 2 - FRAME_GAP - FRAME_SIDE_WIDTH / 2
    right_x = BASE_LOCATION[0] + DOOR_WIDTH / 2 + FRAME_GAP + FRAME_SIDE_WIDTH / 2

    center_z = BASE_LOCATION[2]
    top_z = BASE_LOCATION[2] + DOOR_HEIGHT / 2 + FRAME_GAP + FRAME_TOP_HEIGHT / 2
    bottom_z = BASE_LOCATION[2] - DOOR_HEIGHT / 2 - FRAME_GAP - FRAME_TOP_HEIGHT / 2

    left = create_frame_piece(
        "DoorFrameLeft",
        (left_x, frame_y, center_z),
        (FRAME_SIDE_WIDTH, FRAME_DEPTH, outer_height)
    )

    right = create_frame_piece(
        "DoorFrameRight",
        (right_x, frame_y, center_z),
        (FRAME_SIDE_WIDTH, FRAME_DEPTH, outer_height)
    )

    top = create_frame_piece(
        "DoorFrameTop",
        (BASE_LOCATION[0], frame_y, top_z),
        (outer_width, FRAME_DEPTH, FRAME_TOP_HEIGHT)
    )

    bottom = create_frame_piece(
        "DoorFrameBottom",
        (BASE_LOCATION[0], frame_y, bottom_z),
        (outer_width, FRAME_DEPTH, FRAME_TOP_HEIGHT)
    )

    frame = join_objects([left, right, top, bottom], "DoorFrame")
    return frame

# =========================================================
# MAIN
# =========================================================

def build_door_with_frame():
    mat_door = create_material(
        "Mat_DoorLeafWithFrame",
        (0.95, 0.92, 0.87, 1.0),
        roughness=0.42,
        metallic=0.0
    )

    mat_knob = create_material(
        "Mat_DoorKnobDark",
        (0.12, 0.12, 0.12, 1.0),
        roughness=0.35,
        metallic=0.35
    )

    mat_frame = create_material(
        "Mat_DoorFrame",
        (0.96, 0.94, 0.90, 1.0),
        roughness=0.45,
        metallic=0.0
    )

    # Hoja
    door = create_door_leaf()
    create_panel_relief_both_sides(door)
    add_bevel(door, BEVEL_WIDTH, BEVEL_SEGMENTS)
    assign_material(door, mat_door)

    # Pomo
    knob = create_realistic_knob()
    add_bevel(knob, 0.0012, 2)
    assign_material(knob, mat_knob)
    knob.parent = door

    # Marco
    frame = create_door_frame()
    add_bevel(frame, FRAME_BEVEL_WIDTH, FRAME_BEVEL_SEGMENTS)
    assign_material(frame, mat_frame)

    print("Puerta con marco y pomo creada correctamente.")

# Ejecutar
build_door_with_frame()
'''

    try:
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)