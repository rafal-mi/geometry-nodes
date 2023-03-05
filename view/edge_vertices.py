import bpy

# Shift+A, Mesh -> Plane 

me =  bpy.context.object.data
me_vv = me.vertices
me_ee = me.edges

print("Mesh vertices")

for (i, v) in enumerate(me_vv):
    print(f"    {i} {v.co}")

print("Mesh edge vertices")

for e in me_ee:
    for i in [0, 1]:
        print(f"    {e.vertices[i]} {me_vv[e.vertices[i]].co}")
    print("")
        





