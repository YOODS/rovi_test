#!/usr/bin/python

import numpy as np
import open3d as o3d
import copy
from rovi_utils import ransac_solver as solver

Param={
  "normal_radius": 0.003,
  "distance_threshold": 0,
  "feature_mesh": 0.002,
  "feature_radius": 0.007,
  "icp_threshold": 0.003,
  "eval_threshold": 0.001,
  "rotate":0,
  "repeat":1}

model=o3d.read_point_cloud("../primitive/arc1.ply")
scene=o3d.read_point_cloud("../primitive/arc2.ply")
model.paint_uniform_color([1, 0.706, 0])
scene.paint_uniform_color([0, 0.651, 0.929])
o3d.draw_geometries([model, scene])

solver.learn([solver.toNumpy(model)],Param)
result=solver.solve([solver.toNumpy(scene)],Param)
print "Score",result["fitness"]
print "Tmat",result["transform"]
m1=copy.deepcopy(model)
m1.transform(result["transform"][0])
o3d.draw_geometries([m1, scene])
