#!/usr/bin/python

import numpy as np
import roslib
import rospy
from std_msgs.msg import Float32MultiArray
from sensor_msgs.msg import PointCloud

def sub_array(msg):
  print type(msg.data)
  print len(msg.data)
  return

def sub_pc(msg):
  print type(msg.points)
  print len(msg.points)
  return

if __name__ == "__main__":
  rospy.init_node('sub_test',anonymous=True)
  rospy.Subscriber("array",Float32MultiArray,sub_array)
  rospy.Subscriber("pc",PointCloud,sub_pc)
  try:
    rospy.spin()
  except KeyboardInterrupt:
    print "Shutting down"
