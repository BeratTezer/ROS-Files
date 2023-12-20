#!/usr/bin/env python2.7

import rospy

# We will send Int32 messages
from std_msgs.msg import Int32

# Node name
nodeName = "messagepublisher"

# Topic names. Make sure that in the Arduino code, 
# the subscriber nodes are subscribed to these exact topics
topicNameLeftMotor = "left_motor_velocity"
topicNameRightMotor = "right_motor_velocity"

# Initialize our subscriber node.
# We set "anonymous=True" to ensure that the node has a unique name
# this option will add random numbers to the end of the publisher node
#  that is, to the end of the nodeName.
rospy.init_node(nodeName, anonymous=True)

# Our node is publishing messages to the specified topic names. 
# We specify the type of messages we want to publish(Int32).
# queue_size=5 means that we limit the number of queued messages
# if the subscriber cannot receive the messages fast enough.
publisherLeftMotor = rospy.Publisher(topicNameLeftMotor, Int32, queue_size=5)
publisherRightMotor = rospy.Publisher(topicNameRightMotor, Int32, queue_size=5)

# Specify the frequency of publishing the messages.
# We publish the messages with 1 [Hz]
ratePublisher = rospy.Rate(1)

# Initialize the integer that we plan to send.
# Values are from 0-255
# Velocity of left motor
leftMotor = 0
# Velocity of right motor
rightMotor = 0

while not rospy.is_shutdown():
    # These lines ar for debugging
    rospy.loginfo(leftMotor)
    rospy.loginfo(rightMotor)

    # Get the velocity values from the terminal
    leftMotor = int(input("Enter left motor velocity (0-255):\n"))
    rightMotor = int(input("Enter right motor velocity (0-255):\n"))
    
    # Publish the message
    publisherLeftMotor.publish(leftMotor)
    publisherRightMotor.publish(rightMotor)

    # Pause for previous defined rate
    ratePublisher.sleep()