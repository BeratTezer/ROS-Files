#!/usr/bin/env python2.7

import rospy

# Images will send messages in form of images consequently
from sensor_msgs.msg import Image

# cv_bridge is a package that consists of a library for converting OpenCV images (of tpye cv::Mat) into a ROS image message and for converting ROS image message back to OpenCV images that is, it serves as a bridge between OpenCV and ROS
from cv_bridge import CvBridge

# Import OpenCV
import cv2

# Create the name of our subscriber node
subscriberNodeName = "camera_sensor_subscriber"

# Create the name of our topic over which we will transmit the image messages. Make sure that the same name is used in the spurce file of publisher
topicName = "video_topic"

# This function is a callback function that is called every time the message arrives
def callbackFunction(message):
    # Create a bridge object, print the message, convert from cv_bridge to OpenCV image format
    bridgeObject = CvBridge()
    rospy.loginfo("Received a video message/frame")
    convertedFrameBackToCV = bridgeObject.imgmsg_to_cv2(message)

    # Show the image on the screen, wait in miliseconds(Here only 1 milisecond).
    cv2.imshow("camera", convertedFrameBackToCV)
    cv2.waitKey(1)

# Initialize the subscriber node. anonymous = True means that a random number is added to the subscriber node name
rospy.init_node(subscriberNodeName, anonymous=True)

# Subscribe: specify the topic name, type of the message we will receive and the name of the callback function
rospy.Subscriber(topicName, Image, callbackFunction)

# Execute the code infintely, until we press ctr+c
rospy.spin()

# Destroy all the windows
cv2.destroyAllWindows()