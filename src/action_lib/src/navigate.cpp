#include <ros/ros.h>
#include <move_base_msgs/MoveBaseAction.h>
#include <actionlib/client/simple_action_client.h>
#include "std_msgs/String.h"
#include <sstream>
#include <iostream>
#include <signal.h>

using namespace std;
// SimpleActionClient, giving move_base a goal point
typedef actionlib::SimpleActionClient<move_base_msgs::MoveBaseAction> MoveBaseClient;

void DoShutdown(int sig)
{
	// exit
	ROS_INFO("shutting down!");
	ros::shutdown(); 
    exit(sig);
}

int main(int argc, char** argv){
    ros::init(argc, argv, "a_goals_sender"); //初始化ros节点的常规操作
    
    // 声明一个SimpleActionClient：
    //tell the action client that we want to spin a thread by default
    MoveBaseClient ac("move_base", true);

  //wait for the action server to come up
    while(!ac.waitForServer(ros::Duration(5.0))){
        ROS_INFO("Waiting for the move_base action server to come up");
    }
    // 声明一个目标点goal，注意MoveBaseGoal的格式：
    move_base_msgs::MoveBaseGoal goal;
    
    //在ctrl+c时有效执行退出操作，方便扩展（参见参考【3】）
    signal(SIGINT, DoShutdown);
    
    ros::NodeHandle n;
    ros::Rate loop_rate(100); 
    
    while (ros::ok())
    {
        //goal.target_pose.header.frame_id = "base_link";*/
        goal.target_pose.header.frame_id = "map";
        goal.target_pose.header.stamp = ros::Time::now();
		// 以下是一个随意取的二维目标点：
        goal.target_pose.pose.position.x = 1.3;
        goal.target_pose.pose.position.y = 7.56;
        goal.target_pose.pose.orientation.w = 1.0;

        ROS_INFO("Sending goal");
        // 定义好了goal，就可以调用SimpleActionClient的现成方法sendGoal()，非常方便：
        ac.sendGoal(goal);

        ac.waitForResult();
        // 判断是否执行成功：
        if(ac.getState() == actionlib::SimpleClientGoalState::SUCCEEDED)
          ROS_INFO("Hooray, the base moved to the goal");
        else
          ROS_INFO("The base failed to move for some reason");
      
        ros::spinOnce();

        loop_rate.sleep();
    }
    return 0;
}

