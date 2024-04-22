import actionlib
import rospy
import tf
from actionlib_msgs.msg import GoalStatus
from geometry_msgs.msg import Pose, Point, Quaternion, PoseStamped
from move_base_msgs.msg import MoveBaseAction, MoveBaseActionGoal, MoveBaseGoal
from std_msgs.msg import String
from nav_msgs.srv import GetPlan
from nav_msgs.msg import Path
from std_msgs.msg import Header
from typing import List, Union, Tuple

rospy.init_node('across_door')
move_base = actionlib.SimpleActionClient("move_base", MoveBaseAction)
rospy.loginfo("Waiting for move_base action server")
move_base.wait_for_server(rospy.Duration(60))
rospy.loginfo("Connected to move_base server...")

move_base.cancel_all_goals()