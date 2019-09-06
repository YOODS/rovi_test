#include <ros/ros.h>
#include <std_msgs/String.h>
#include <geometry_msgs/Point32.h>
#include <sensor_msgs/PointCloud.h>
#include <stdlib.h>
#include <math.h>

ros::NodeHandle *nh;
ros::Publisher *pub;

int maxpnt=500000;
int minpnt=500000;
double radius=0.5;

void callback(const ros::TimerEvent&){
  sensor_msgs::PointCloud pts;
  pts.header.stamp = ros::Time::now();
  pts.header.frame_id = "world";
  int N=maxpnt;
  if(maxpnt!=minpnt){
    N=minpnt+(long long)(maxpnt-minpnt)*rand()/RAND_MAX;
    pts.points.resize(N);
  }
  pts.points.resize(N);
  std::cout<<"points "<<N<<"\n";
  for (int n=0,i=0; n<N; n++){
    float theta=2*M_PI*rand()/RAND_MAX;
    float phi=M_PI*rand()/RAND_MAX-M_PI/2;
    pts.points[n].x=radius*cos(phi)*cos(theta);
    pts.points[n].y=radius*cos(phi)*sin(theta);
    pts.points[n].z=radius*sin(phi);
  }
  pub->publish(pts);
}
int main(int argc, char **argv){
  if(argc>=2) maxpnt=minpnt=atoi(argv[1]);
  if(argc>=3) minpnt=atoi(argv[2]);
  if(maxpnt<minpnt){ int a=maxpnt;maxpnt=minpnt;minpnt=a;}
  std::cout<<" min "<<minpnt<<" max "<<maxpnt<<"\n";

  ros::init(argc, argv, "pubpc");
  ros::NodeHandle n;
  nh = &n;
  ros::Timer timer = n.createTimer(ros::Duration(2.0), callback);
  ros::Publisher p0=n.advertise<sensor_msgs::PointCloud>("pc",1);
  pub = &p0;
  ros::spin();
  return 0;
}
