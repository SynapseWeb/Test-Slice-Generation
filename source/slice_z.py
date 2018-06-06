import bpy
from mathutils import Vector

num_slices = 25

# Use the currently selected object
object = bpy.context.object

# Apply any transformations
bpy.ops.object.transform_apply ( location=True, rotation=True, scale=True )

# Get the bounding box
local_coords = object.bound_box[:]
om = object.matrix_world
worldify = lambda p: om * Vector(p[:])
coords = [ worldify(p).to_tuple() for p in local_coords ]

x_vals = [ v[0] for v in coords ]
y_vals = [ v[1] for v in coords ]
z_vals = [ v[2] for v in coords ]

min_x = min(x_vals)
max_x = max(x_vals)
min_y = min(y_vals)
max_y = max(y_vals)
min_z = min(z_vals)
max_z = max(z_vals)

center_x = (max_x + min_x) / 2.0
center_y = (max_y + min_y) / 2.0

print ( str(min_x) + " < x < " + str(max_x) )
print ( str(min_y) + " < y < " + str(max_y) )
print ( str(min_z) + " < z < " + str(max_z) )

dz = (max_z - min_z) / num_slices
if num_slices > 1:
    dz = (max_z - min_z) / (num_slices-1)

plane_names = []
for zn in range(num_slices):
    print ( "Slice " + str(zn) + " is at " + str(min_z+(zn*dz)))
    bpy.ops.mesh.primitive_plane_add()
    plane_names.append ( bpy.context.object.name )
    print ( "Scale Plane" )
    bpy.context.object.scale[0] = 2.0 * (max_x - min_x)
    bpy.context.object.scale[1] = 2.0 * (max_y - min_y)
    print ( "Translate Plane" )
    bpy.context.object.location[0] = center_x
    bpy.context.object.location[1] = center_y
    bpy.context.object.location[2] = min_z+(zn*dz)
    if zn == 0:
        # Apply just a small delta to get the bottom plane inside the object
        bpy.context.object.location[2] += dz/(2*num_slices)
    if zn == (num_slices-1):
        # Apply just a small delta to get the top plane inside the object
        bpy.context.object.location[2] += -dz/(2*num_slices)
        
    #bpy.ops.transform.translate ( value=(center_x, center_y, min_z+(zn*dz)) )
    print ( "Adding boolean" )
    bpy.ops.object.modifier_add ( type='BOOLEAN' )
    bpy.context.object.modifiers["Boolean"].object = object
    bpy.ops.object.modifier_apply ( apply_as='DATA', modifier="Boolean" )
