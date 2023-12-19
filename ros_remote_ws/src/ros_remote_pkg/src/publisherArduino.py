#!/usr/bin/env python2.7

import rospy

# We will send Int32 messages
from std_msgs.msg import Int32

# Node name
nodeName = "messagepublisher"

# Topic names. Make sure that in the Arduino code, the subscriber nodes are subscribed to these exact topics
topicNameLeftMotor = "left_motor_velocity"
topicNameRightMotor = "right_motor_velocity"

# 