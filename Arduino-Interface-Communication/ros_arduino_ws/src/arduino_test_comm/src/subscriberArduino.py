#!/usr/bin/env python2.7

import rospy
# We expect to receive Int32
from std_msgs.msg import Int32

# Node name
nodeName = "messagesubs"

# Topic name, it has to match the topic name specified in the Arduino code
topicName = "info_back"

# This is the callback function, when the message is received, this function will be executed. It simply print the result to screen
def callbackFunction(message):
    print("From Arduino, we received %d"%message.data)

# Initialize our subscriber node. We set "anonymous = True" to make sure that the node has a unique name. This parameter will add random numbers to the end of the node name
rospy.init_node(nodeName, anonymous=True)

# Subscribe to the topicName, we specify the type of the message we want to receive and we specify the callbackFunction
rospy.Subscriber(topicName, Int32, callbackFunction)

# Loop
rospy.spin()