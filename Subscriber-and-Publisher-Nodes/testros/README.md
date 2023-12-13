Scripts:
	Publisher Node:
<code>
	#!/usr/bin/env python3

	# This line means that this is the Python file and it should be executed by the executed by the Python interpreter.

	# We need to improt "rospy" since this file is the ROS node it imports all the funcitons and package we need to we need to write the ROS node

	import rospy

	# We will publish integer messages, and consequently from ROS standart message package called std_msg we need to import Int32

	from std_msgs.msg import Int32

	nodeName = 'messagepublisher'
	topicName = 'information'

	# Here, we initialize our publisher node we call it as nodeName.

	# We set "anonymous=True" to ensure that the node has a unique name this option will add random numbers to the end of the publisher node that is, to the end of the nodeName.

	rospy.init_node(nodeName, anonymous=True)

	# This code line is saying that our node publishing to hte topicName, the messages is of type Int32.
	# "queue_size = 5" means that we limit the number of queued messages if subscriber cannot receive them fast enough.

	publisher1 = rospy.Publisher(topicName, Int32, queue_size=5)

	# Here we set the mesasge rate in Hz that is, we are publishing with the set frequency in Hz. For example 2Hz means that we are publishing two messages per second.

	ratePublisher = rospy.Rate(1)

	intMessage = 0

	while not rospy.is_shutdown():
		# This is useful for debugging: The message will be printed to the screeen then it will also be written to the log file and it will also be written to rosout - this is a tool for debugging.
		rospy.loginfo(intMessage)

		# Here we publish the message
		publisher1.publish(intMessage)

		# Change the message
		intMessage = intMessage+1

		# Here wait to make sure that the desired publishing rate is achieved
		ratePublisher.sleep()
</code>
