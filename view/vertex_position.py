import bpy

# Shift+A, Mesh -> Plane 

me =  bpy.context.object.data
e = me.edges[0]

print(f"Edge: {e}")

e_vv = e.vertices

print(f"Edge vertices: {e_vv}")

e_v0 = e.vertices[0]
e_v1 = e.vertices[1]

print(f"Edge vertices: {e_v0}, {e_v1}")

me_vv = me.vertices

print(f"Mesh vertices: {me_vv}")

me_v = me_vv[0]

print(f"Mesh vertex: {me_v}")

# https://blender.stackexchange.com/questions/1311/how-can-i-get-vertex-positions-from-a-mesh
co = me_v.co

print(f"Vertex coordinates: {co}")





