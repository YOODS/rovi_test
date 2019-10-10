#!/usr/bin/python

import cv2
import numpy as np
import open3d as o3d

radius=0.005
points=10000
theta=2*np.pi*np.random.rand(points)
phi=np.pi*np.random.rand(points)-np.pi/2
px=radius*np.cos(phi)*np.cos(theta)
py=radius*np.cos(phi)*np.sin(theta)
pz=radius*np.sin(phi)

mesh=np.vstack((px,py,pz)).T

pc=o3d.PointCloud()
pc.points=o3d.Vector3dVector(mesh)
o3d.write_point_cloud("sphere.ply",pc,True,False)


