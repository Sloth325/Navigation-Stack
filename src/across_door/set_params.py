from dynamic_reconfigure.client import Client


def setup_params():
    trajectory_planner = Client("/move_base/TebLocalPlannerROS")
    trajectory_params = {
        "yaw_goal_tolerance": 3,
    }
    config = trajectory_planner.update_configuration(trajectory_params)