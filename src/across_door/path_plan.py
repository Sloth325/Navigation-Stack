#! /usr/bin/env python

import actionlib
import rospy
import tf
from tf.transformations import euler_from_quaternion, quaternion_from_euler
from actionlib_msgs.msg import GoalStatus
from geometry_msgs.msg import Pose, Point, Quaternion, PoseStamped
from move_base_msgs.msg import MoveBaseAction, MoveBaseActionGoal, MoveBaseGoal
from std_msgs.msg import String
from nav_msgs.srv import GetPlan, GetPlanResponse
from nav_msgs.msg import Path
from std_msgs.msg import Header
from typing import List, Union, Tuple
import numpy as np


def get_path(start: PoseStamped, goal: PoseStamped) -> Path:
    """向movebase发请求 计算起始点直接是否有可行路径"""
    rospy.wait_for_service('/move_base/make_plan')
    planner = rospy.ServiceProxy('/move_base/make_plan', GetPlan)
    req = GetPlan()
    req.start = start
    req.goal = goal
    req.tolerance = .5
    path: Path = planner(req.start, req.goal, req.tolerance).plan
    return path


def is_goal_reachable(start: PoseStamped, goal: PoseStamped, error_time=3) -> bool:
    """判断路径是否可行

    error_time:
        有时候进行plan path的时候 会意外成功， 猜测是误差导致的。
        尝试进行error time次规划路线 如果都成功了，才认为路径可行
    """
    if error_time <= 0:
        return True
    return bool(get_path(start, goal).poses) and is_goal_reachable(start, goal, error_time - 1)


def get_shortest_path_goal_pose(start: PoseStamped, goal: PoseStamped) -> PoseStamped:

    def __generate_all_yaw_direction_pose(pose: Pose, angle_diff=0.05, rg=6) -> List[Pose]:
        ori: Quaternion = pose.orientation
        roll, pitch, yaw = euler_from_quaternion((ori.x, ori.y, ori.z, ori.w))
        res = []
        print(f'roll pitch yaw: {roll} {pitch} {yaw}')
        for degree in np.arange(yaw - rg, yaw + rg, angle_diff):
            orientation = Quaternion(*quaternion_from_euler(roll, pitch, degree))
            res.append(Pose(position=pose.position, orientation=orientation))
        return res

    def __pose2stamped(origin_posestamped: PoseStamped, pose: Pose) -> PoseStamped:
        return PoseStamped(header=origin_posestamped.header, pose=pose)

    # return goal

    posestampeds: List[PoseStamped] = list(
        map(lambda x: __pose2stamped(goal, x), __generate_all_yaw_direction_pose(goal.pose)))

    res = min(posestampeds, key=lambda x: get_path_length(get_path(start, x)))
    ori = res.pose.orientation
    roll, pitch, yaw = euler_from_quaternion((ori.x, ori.y, ori.z, ori.w))
    print(f'roll pitch yaw: {roll} {pitch} {yaw}')
    return res


def get_path_length(path: Path) -> float:
    path_length = 0
    for i in range(len(path.poses) - 1):
        pos_a_x = path.poses[i].pose.position.x
        pos_b_x = path.poses[i + 1].pose.position.x
        pos_a_y = path.poses[i].pose.position.y
        pos_b_y = path.poses[i + 1].pose.position.y
        path_length += np.sqrt(np.power(pos_a_x - pos_b_x, 2) + np.power(pos_a_y - pos_b_y, 2))
    return path_length