#!/usr/bin/env python3

import rhinoscriptsyntax as rs
import random
import rotatexyz

def pick_meshes():
    '''
     Returns a list of meshes you wish to array around an object.
    '''

    mesh_list = []
    mesh1= rs.GetObject("Mesh1")
    mesh_list.append(mesh1)
    mesh2= rs.GetObject("Mesh2")
    mesh_list.append(mesh2)
    mesh3= rs.GetObject("Mesh3")
    mesh_list.append(mesh3)
    len_mesh_list = len(mesh_list)
    return mesh_list, len_mesh_list

def get_point_list():
    '''
    Returns the object that meshes will be arrayed around.
    '''
    point_cloud = rs.GetObject('Select point cloud', rs.filter.pointcloud)
    point_list = rs.PointCloudPoints(point_cloud)
    return point_list

def mesh_dict(mesh_list):
    '''
     A separate function for gathering the chosen meshes vertices and
     face vertices. Then storing them in a dictionary. Needed steps for
     generating them later.
    '''

    mesh_dict = {}
    len_mesh_list = len(mesh_list)
    for n in range(len_mesh_list):
        vertlist = []
        verts = rs.MeshVertices(mesh_list[n])
        vertlist.append(verts)
        face_verts = rs.MeshFaceVertices(mesh_list[n])
        vertlist.append(face_verts)
        mesh = mesh_list[n]
        mesh_dict[mesh] = vertlist
    return mesh_dict

def mesh_to_point(mesh_dict, point_list, mesh_list, len_mesh_list):
    '''
     Randomly selects a mesh from mesh_list, generates it and moves it
     to a point in point_list. Then checks for intersections
     with other meshes.
    '''

    mlist = []
    n = 0
    for point in point_list:
        added = rs.AddMesh(mesh_dict[mesh_list[n]][0], mesh_dict[mesh_list[n]][1])
        center = rs.MeshAreaCentroid(added)
        inset = rs.MeshClosestPoint(added, center)
        translation = [point[i]-inset[0][i] for i in range(0,3)]
        moved = rs.MoveObject(added, translation)
        mesh = rotatexyz.rotate(moved)
        mlist.append(mesh)
        n += 1
        if n == len_mesh_list:
            n = 0
    return(mlist)


if __name__ == '__main__':
    rs.GetObject(";)")
    mesh_list, len_mesh_list = pick_meshes()
    point_list = get_point_list()
    mesh_dict = mesh_dict(mesh_list)
    mlist = mesh_to_point(mesh_dict, point_list, mesh_list, len_mesh_list)
