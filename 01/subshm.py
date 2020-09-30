#!/usr/bin/python

import numpy as np
import roslib
import rospy
from std_msgs.msg import String
import sysv_ipc
memory=None

def sub_mem(msg):
  global memory
  m=eval(msg.data)
  if memory is None:
    memory = sysv_ipc.SharedMemory(m['key'])
  memory_value = memory.read()
  na=np.frombuffer(memory_value, dtype=np.float32, count=9)
  print na
  return

if __name__ == "__main__":
  rospy.init_node('sub_test',anonymous=True)
  rospy.Subscriber("mem",String,sub_mem)
  try:
    rospy.spin()
  except KeyboardInterrupt:
    print "Shutting down"
