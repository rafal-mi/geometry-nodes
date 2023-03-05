import bpy

# Shift+A, Mesh -> Plane 

me =  bpy.context.object.data
ee = me.edges
e = ee[1]

print(f"Edge: {e}")

e_vv = e.vertices

print(f"Edge vertices: {e_vv}")

e_v0 = e.vertices[0]
e_v1 = e.vertices[1]

print(f"Edge vertices: {e_v0}, {e_v1}")

me_vv = me.vertices

for v in me_vv:
    print(f"    {v.co}")

print(f"Mesh vertices: {me_vv}")

for e in ee:
    for i in [0, 1]:
        print(f"    {e.vertices[i]} {me_vv[e.vertices[i]].co}")
    print("")
        

me_v = me_vv[0]

print(f"Mesh vertex: {me_v}")

# https://blender.stackexchange.com/questions/1311/how-can-i-get-vertex-positions-from-a-mesh
co = me_v.co

print(f"Vertex coordinates: {co}")





