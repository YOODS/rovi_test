#!/usr/bin/python

import cv2
import numpy as np
import open3d as o3d

mesh=0.001
radius=0.05
theta=0
floats=np.array([]).reshape((-1,3))
while theta<np.pi*3/5:
  px=radius*np.cos(theta)
  pz=radius*np.sin(theta)-3*mesh
  depth=0
  while depth<0.1:
    py=depth
    floats=np.vstack((floats,[[px,py,pz]]))
    depth=depth+mesh
  theta=theta+mesh/radius

print floats
pc=o3d.PointCloud()
pc.points=o3d.Vector3dVector(floats)
o3d.write_point_cloud("arc2.ply",pc,True,False)


