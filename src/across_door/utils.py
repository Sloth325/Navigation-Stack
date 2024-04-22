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


def buildPoseStamped(header: Header, pose: Pose) -> PoseStamped:
    return PoseStamped(header=header, pose=pose)


def buildPose(trans: Union[List[int], Tuple[int]], rot: Union[List[int], Tuple[int]]) -> Pose:
    position = Point(x=trans[0], y=trans[1], z=trans[2])
    orientation = Quaternion(x=rot[0], y=rot[1], z=rot[2], w=rot[3])
    return Pose(position=position, orientation=orientation)


def get_transform() -> Tuple[List, List]:
    """Get current transform wrt. map"""
    tf_listener = tf.TransformListener()
    while True:
        try:
            trans, rot = tf_listener.lookupTransform('/map', '/base_link', rospy.Time(0))
            return trans, rot
        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
            continue


def get_current_pose() -> PoseStamped:
    """Get current pose wrt. map"""
    trans, rot = get_transform()
    return buildPoseStamped(Header(frame_id='map'), buildPose(trans, rot))