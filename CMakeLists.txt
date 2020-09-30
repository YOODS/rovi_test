cmake_minimum_required(VERSION 2.8.3)
project(rovi_test)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  std_msgs
  geometry_msgs
  sensor_msgs
  stereo_msgs
  cv_bridge
  tf2_ros
  rovi
  rovi_utils
)

catkin_package(
  CATKIN_DEPENDS roscpp std_msgs geometry_msgs sensor_msgs cv_bridge tf2_ros
  DEPENDS OpenCV
)

#catkin_python_setup()

include_directories(
  include
  ${catkin_INCLUDE_DIRS}
  ${OpenCV_INCLUDE_DIRS}
  ${EIGEN3_INCLUDE_DIRS}
)

add_executable(pubarray 01/pubarray.cpp)
target_link_libraries(pubarray ${catkin_LIBRARIES})
add_executable(pubpc 01/pubpc.cpp)
target_link_libraries(pubpc ${catkin_LIBRARIES})
add_executable(pubshm 01/pubshm.cpp)
target_link_libraries(pubshm ${catkin_LIBRARIES})
