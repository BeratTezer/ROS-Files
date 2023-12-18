# Scripts:
## Publisher Node:
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

## Subscriber Node:
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

## Arduino Code:
	/* This code will subscribe to the topic "information",
	* then it will read messages from this topic. 
	* The message is an integer. It will mulitply the integer by 2,
	* and then it will send back (publish) the result to the topic called "info_back"
	*/

	#include <ros.h>
	#include <std_msgs/Int32.h>

	// Node handle
	ros::NodeHandle nh;

	// This message is sent back
	std_msgs::Int32 outputMessage;

	// Publisher, similar in python first we specify the topic name nd then the message
	ros::Publisher pub("info_back", &outputMessage);

	/* This is the callbackFunction for our subscriber when the message is
	* received, this funciton will be called this function will simply 
	* multiply inputMessage.data by 2 and publish the result
	*/ 

	void callbackFunction(const std_msgs::Int32 &inputMessage) {
	outputMessage.data = 2*inputMessage.data;
	pub.publish(&outputMessage);
	}

	// Subscriber
	ros::Subscriber<std_msgs::Int32>sub("information", &callbackFunction);

	void setup() {
	// put your setup code here, to run once:
	nh.initNode();
	nh.advertise(pub);
	nh.subscribe(sub);
	}

	void loop() {
	// put your main code here, to run repeatedly:
	nh.spinOnce();
	delay(1);
	}