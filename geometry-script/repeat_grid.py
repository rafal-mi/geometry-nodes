from geometry_script import *

#@tree("Repeat Grid")
#def repeat_grid(geometry: Geometry, width: Int, height: Int):
#    g = grid(
#        size_x=width, size_y=height,
#        vertices_x=width, vertices_y=height
#    ).mesh_to_points()
#    return g.instance_on_points(instance=geometry)


#@tree("Cube Tree")
#def cube_tree(size: Vector = (1, 1, 1)):
#    return cube(size=size)

@tree("Skin")
def skin():
    # Create a cube
    c = cube()
    # Create a sphere
    sphere = uv_sphere()
    # Transfer the position to the sphere
    transferred_position = c.transfer_attribute(
        data_type=TransferAttribute.DataType.FLOAT_VECTOR,
        attribute=position()
    )
    # Make the sphere conform to the shape of the cube
    return sphere.set_position(position=transferred_position)
