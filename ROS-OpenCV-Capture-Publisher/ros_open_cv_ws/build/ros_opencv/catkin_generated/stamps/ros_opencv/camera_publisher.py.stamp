#!/usr/bin/env python2.7
# Here, we are saying to ROS that this is a Python soruce file

# Import rospy that enables us to use ROS with Python
import rospy

# Messages will send in form of images consequently, thus
from sensor_msgs.msg import Image

# cv_bridge is a package that consists of a library for converting OpenCV images (of tpye cv::Mat) into a ROS image message and for converting ROS image message back to OpenCV images that is, it serves as a bridge between OpenCV and ROS
from cv_bridge import CvBridge

# Import OpenCV
import cv2

# Create the name of our publisher node
publisherNodeName = "camera_sensor_publisher"

# Create the name of our topic over which we will transmit the image messages. Make sure that the same name is used in the spurce file of subscriber
topicName = "video_topic"

# Initialize the node
rospy.init_node(publisherNodeName, anonymous=True)

# Create a publisher object, specify the name of the topic, a type of the message being sent (Image) and define the buffer size (queue_size)
publisher = rospy.Publisher(topicName, queue_size=60)

# Rate of transmitting the messages
rate = rospy.Rate(30)

# Create the video capture object
videoCaptureObject = cv2.videoCapture(0)

# Create the CvBridge object that will be used to convert OpenCV Images to ROS image messages
bridgeObject = CvBridge()

# Infinite loop that captures the images and transmits them through the topic
while not rospy.is_shutdown():
    # Returns two values; first one is boolean for success/failure and second one is for actual frame.
    returnValue, capturedFrame = videoCaptureObject.read()

    # Transmit
    if returnValue == True:
        # Print the message, convert OpenCV to ROS image message and publish the converted image through the topic
        rospy.loginfo("Video frame captured and published")
        imageTotransmit = bridgeObject.cv2_to_compressed_imgmsg(capturedFrame)
        publisher.publish(imageTotransmit)
    # Wait for certain time to make sure that the specified transmission rate is achieved
    rate.sleep()