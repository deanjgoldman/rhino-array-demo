import rhinoscriptsyntax as rs
import random

def rotate(mesh):
    rotation_x, rotation_y, rotation_z = random.sample(range(0, 360), 3)
    center_point = rs.MeshAreaCentroid(mesh)
    mesh = rs.RotateObject(mesh, center_point, rotation_x, [0,40,0], copy=False)
    mesh = rs.RotateObject(mesh, center_point, rotation_y, [1,0,0], copy=False)
    mesh = rs.RotateObject(mesh, center_point, rotation_z, copy=False)
    return mesh
