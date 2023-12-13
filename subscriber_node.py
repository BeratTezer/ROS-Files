#!/usr/bin/env python2.7

import rospy
from std_msgs.msg import Int32

# Name of the node
nodeName = 'messagesubscriber'

# Name of the topic - has to match the name of the topic in the publisher node.
topicName = 'information'

# Callback function
# Everytime the message arrivesto the subsricber node, the callback function is executed in this call-back funciton we simply print the same

def callbackFunction(message):
	print("We received %d"%message.data)

# Here, we initialize our subsriber node.
# we call it as nodeName. We set "anonymous=True" to ensure that the node has a unique name of the publisher node that is to end of the nodeName

rospy.init_node(nodeName)

# Here we subsribe to the topicName, we specify the type of the message we want to receive, and specify the name of the callback function that is executed once the message arrives.

rospy.Subscriber(topicName, Int32, callbackFunction)

# This function doesn't return until the node is stopped that is, it serves as a while loop.
rospy.spin()
