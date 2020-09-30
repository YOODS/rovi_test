#!/usr/bin/python

import numpy as np
import roslib
import rospy
import time
import open3d as o3d
from std_msgs.msg import String
import sysv_ipc
memory=None

def sub_mem(msg):
  global memory
  print msg.data
  t0=time.time()
  m=eval(msg.data)
  if memory is None:
    memory = sysv_ipc.SharedMemory(m['key'])
  nd=np.frombuffer(memory.read(),dtype=np.float32,count=m['length']).reshape((-1,3)).astype(np.float64)
  t1=time.time()
  print t1-t0
  pc=o3d.geometry.PointCloud()
  pc.points=o3d.utility.Vector3dVector(nd)
  t2=time.time()
  print t2-t1
  return

if __name__ == "__main__":
  rospy.init_node('sub_test',anonymous=True)
  rospy.Subscriber("mem",String,sub_mem)
  try:
    rospy.spin()
  except KeyboardInterrupt:
    print "Shutting down"
