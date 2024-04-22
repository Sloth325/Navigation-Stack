#! /usr/bin/env python

from typing import List, Tuple, Union

import actionlib
import numpy as np
import rospy
import tf
from actionlib_msgs.msg import GoalStatus
from geometry_msgs.msg import Point, Pose, PoseStamped, Quaternion
from move_base_msgs.msg import MoveBaseAction, MoveBaseActionGoal, MoveBaseGoal
from nav_msgs.msg import Path
from nav_msgs.srv import GetPlan, GetPlanResponse
from path_plan import is_goal_reachable, get_shortest_path_goal_pose
from std_msgs.msg import Header, String
from tf.transformations import euler_from_quaternion, quaternion_from_euler
from utils import buildPose, buildPoseStamped, get_current_pose, get_transform
from set_params import setup_params


def tmp_get_go_ahead_pose() -> PoseStamped:
    trans, rot = get_transform()
    trans[1] += 0
    trans[0] += 3
    return buildPoseStamped(Header(frame_id='map'), buildPose(trans, rot))


class AcrossDoor():

    def __init__(self) -> None:
        rospy.init_node('across_door')
        self.move_base = actionlib.SimpleActionClient("move_base", MoveBaseAction)
        # setup_params()
        rospy.loginfo("Waiting for move_base action server")
        self.move_base.wait_for_server(rospy.Duration(60))
        rospy.loginfo("Connected to move_base server...")

    def tmp_go_to(self, goal: PoseStamped):
        self.move_base.cancel_all_goals()
        while not rospy.is_shutdown():
            start_pose: PoseStamped = get_current_pose()
            while not is_goal_reachable(start_pose, goal):
                rospy.loginfo('Goal not available, waiting for door to be open')
                rospy.sleep(1)

            # short_goal = get_shortest_path_goal_pose(start_pose, goal)
            rospy.loginfo('Goal achievable!')
            self.try_move(MoveBaseGoal(target_pose=goal))
            break

    def try_move(self, goal: MoveBaseGoal):
        self.move_base.send_goal(goal)
        finished_time_limit = self.move_base.wait_for_result(rospy.Duration(600))
        if not finished_time_limit:
            self.move_base.cancel_goal()
            rospy.loginfo("Time out, didn't achieve goal")
        else:
            if self.move_base.get_state() == GoalStatus.SUCCEEDED:
                rospy.loginfo("Goal achieved.")
            else:
                print(self.move_base.get_state())

    def test(self):
        pose = get_shortest_path_goal_pose(get_current_pose(), tmp_get_go_ahead_pose())
        print(pose)


def go_across_door():
    robo = AcrossDoor()
    rospy.loginfo("WWADS")
    robo.tmp_go_to(tmp_get_go_ahead_pose())


if __name__ == '__main__':
    go_across_door()
