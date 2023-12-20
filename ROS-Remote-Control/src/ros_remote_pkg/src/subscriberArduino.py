#!/usr/bin/env python2.7

import rospy

# We expect the receive Int32 messages
from std_msgs.msg import Int32

# Node name
nodeName = "messagesubs"

# Topic names. Make sure that in the Arduino code, 
# the subscriber nodes are subscribed to these exact topics
topicNameLeftEncoder = "left_encoder_pulses"
topicNameRightEncoder = "right_encoder_pulses"

# These are callback functions. They are called when the messages are received.
# They will print the encoder readings to the screen
def callbackFunctionLeftEncoder(message1):
    print("Left encoder pulses: %s" %message1.data)

def callbackFunctionRightEncoder(message2):
    print("Left encoder pulses: %s" %message2.data)


# Initialize our subscriber node.
# We set "anonymous=True" to ensure that the node has a unique name
# this option will add random numbers to the end of the publisher node
#  that is, to the end of the nodeName.
rospy.init_node(nodeName, anonymous=True)

# Subscribe to the topics. 
# We specify the type of the messages we want to receive.
# Specify the callback functions.
rospy.Subscriber(topicNameLeftEncoder, Int32, callbackFunctionLeftEncoder)
rospy.Subscriber(topicNameRightEncoder, Int32, callbackFunctionRightEncoder)

# Spin the code
rospy.spin()