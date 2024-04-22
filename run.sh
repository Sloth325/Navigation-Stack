#! /bin/bash
gnome-terminal -t "ptp" -x bash -c "sudo ptpd -M -i enp2s0 -C;"
sleep 5s
gnome-terminal -t "hunter_robot_base" -x bash -c "roslaunch hunter_bringup hunter_robot_base.launch;"
#gnome-terminal -t "insta" -x bash -c "roslaunch usb_cam usb_cam-test.launch"
# sleep 3s
# gnome-terminal -t "azure_kinect" -x bash -c "source devel/setup.bash; roslaunch azure_kinect_ros_driver driver.launch;"
#gnome-terminal -t "imu" -x bash -c "roslaunch handsfree_ros_imu handsfree_imu.launch;"
#gnome-terminal -t "lidar" -x bash -c "roslaunch hesai_lidar hesai_lidar.launch;"


