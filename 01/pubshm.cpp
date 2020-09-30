#include <ros/ros.h>
#include <std_msgs/String.h>
#include <geometry_msgs/Point32.h>
#include <sensor_msgs/PointCloud.h>
#include <stdlib.h>
#include <math.h>

#include <sys/shm.h>
static key_t shmkey=0x47454E50; //"GENP"
static unsigned char *shmptr=NULL;

ros::NodeHandle *nh;
ros::Publisher *pub;
float *buf_data;
int buf_count;

void callback(const ros::TimerEvent&){
  std_msgs::String msg;
  char s[32];
  for(int i=0;i<buf_count;i++){
    buf_data[i]=buf_data[i]+1;
    if(i<4) fprintf(stderr,"%f ",buf_data[i]);
  }
  fprintf(stderr,"\n");
  sprintf(s,"{'key':%u,'length':%d}",shmkey,buf_count);
  msg.data=s;
  pub->publish(msg);
}
int main(int argc, char **argv){
  ros::init(argc, argv, "pubshm");
  ros::NodeHandle n;
  nh = &n;
  ros::Timer timer = n.createTimer(ros::Duration(1.0), callback);
  ros::Publisher p0=n.advertise<std_msgs::String>("mem",1);
  pub = &p0;
  int pixels=1000000;
  int sid=shmget(shmkey,pixels*4*3,IPC_CREAT|0666);
  shmptr=(unsigned char *)shmat(sid, NULL, 0);
  shmptr[0]=123;//try writing
fprintf(stderr,"shmem %d\n",shmptr[0]);
  buf_data=(float *)shmptr;
  buf_count=pixels*3;
  for(int i=0;i<buf_count;i++) buf_data[i]=i;

  ros::spin();
  return 0;
}
