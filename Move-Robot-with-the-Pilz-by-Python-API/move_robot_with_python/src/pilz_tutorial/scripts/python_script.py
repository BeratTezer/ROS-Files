#!/usr/bin/env python

from geometry_msgs.msg import Pose, Point
from pilz_robot_programming import *
import math
import rospy

__REQUIRED_API_VERSION__ = "1"  # API version
__ROBOT_VELOCITY__ = 0.5        # velocity of the robot

# main program
def start_program():
    print(r.get_current_pose()) # print the current position of thr robot in the terminal

    # define the positions:
    joint_goal = 150 # Use joint values for the first position
    cartesian_goal = 150 # Use cartesian coordinates for another position
    
    # Move to start point with joint values to avoid random trajectory
    r.move(Ptp(goal=joint_goal, vel_scale=__ROBOT_VELOCITY__))

    #Move to the second position
    r.move(Ptp(goal=cartesian_goal, vel_scale=__ROBOT_VELOCITY__))


if __name__ == "__main__":
    # init a rosnode
    rospy.init_node('robot_program_node')

    # initialisation
    r = Robot(__REQUIRED_API_VERSION__)  # instance of the robot

    # start the main program
    start_program()
