#!/usr/bin/env python2.7

import rospy
# Setting Int32 message
from std_msgs.msg import Int32

# Node name
nodeName = "messagepublisher"

# This is the topic name. Make sure that in the Arduino code, the subscriber node is subscribed to this exact topic
topicName = "information"

# Initialize the subscriber node. "anonymous=True" to make sure that the node has a unique name. This parameter will add random number to the end of the node name.
rospy.init_node(nodeName, anonymous=True)

# Our node is publishing messages to topicName. We specify the tpye of messages we want to publish (Int32), queue_size=5 simply means that we limit the name of queued messages if the subscriber cannot receive the messages fast enough
publisher1 = rospy.Publisher(topicName, Int32, queue_size=5)

# Specify the frequency of publishing the messages that is, we publish the messages with 1 (Hz)
ratePublisher = rospy.Rate(1)

# Initialize the integer that we plan to esnd we will increment this later on in while loop
intMessage = 1

while not rospy.is_shutdown():
    # This line is for debugging
    rospy.loginfo(intMessage)
    # Publish the messages
    publisher1.publish(intMessage)
    # Increment
    intMessage = intMessage+1
    # Pause for the previously defined rate
    ratePublisher.sleep()