#include"ros/ros.h"
#include"lidar_change/lidar.h"

int main(int argc, char  *argv[])
{
    setlocale(LC_ALL,"");
    if(argc != 3)
    {
        ROS_ERROR("请提交两个整数");
        return 1;
    }

    ros::init(argc,argv,"client");
    ros::NodeHandle nh;
    ros::ServiceClient client = nh.serviceClient<lidar_change::lidar>("changes");
    ros::service::waitForService("changes");
    lidar_change::lidar ld;
    ld.request.num1 = atoi(argv[1]);
    ld.request.num2 = atoi(argv[2]);

    bool flag = client.call(ld);

    if(flag)
    {
        ROS_INFO("请求正常处理");
    }
    else
    {
        ROS_ERROR("请求失败");
        return 1;
    }

    return 0;
}
