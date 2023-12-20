# Scripts:
## Publisher Node:
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

## Subscriber Node:
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

## Arduino Communication
	// Arduino-ROS Library - Rosserial Arduino Library - We need to install this library in Arduino
	#include <ros.h>

	// We will be receiving int messages (velocities) and we will send back
	// int messages (encoder pulses) consequently, we need ROS Int32 data structure
	#include <std_msgs/Int32.h>

	// Left encoder
	int encoderPinLeft = 2;

	// Right encoder
	int encoderPinRight = 2;

	// Left motor pins
	int ENA = 5;
	int IN1 = 5;
	int IN2 = 7;

	// Right motor pins
	int IN3 = 9;
	int IN4 = 10;
	int ENB = 11;

	// These two variables count the total number of encoder pulses
	// Left encoder pulses
	volatile unsigned long totalPulsesLeft = 0;

	// Right encoder pulses
	volatile unsigned long totalPulsesRight = 0;

	// Motor velocities - there variable are set by ROS
	// Left motor
	int motorVelocityLeft = 0;

	// Left motor
	int motorVelocityRight = 0;

	// This is a handle of the ROS node
	ros::NodeHandle nh;

	// This is the callback function for the left motor
	// It simply sets the velocity of the left motor on the basis of the received ROS message
	void callbackFuncitonMotorLeft(const std_msgs::Int32 &motorVelocityLeftROS) {
	motorVelocityLeft = motorVelocityLeftROS.data;
	}

	// This is the callback function for the right motor
	// It simply sets the velocity of the rgi,right motor on the basis of the received ROS message
	void callbackFuncitonMotorRight(const std_msgs::Int32 &motorVelocityRightROS) {
	motorVelocityRight = motorVelocityRightROS.data;
	}

	// Publishers for the encoder pulses
	// Left encoder publisher
	std_msgs::Int32 leftEncoderROS;
	ros::Publisher leftEncodeROSPublisher("left_encoder_pulses", &leftEncoderROS);
	// Right encoder publisher
	std_msgs::Int32 rightEncoderROS;
	ros::Publisher rightEncodeROSPublisher("right_encoder_pulses", &rightEncoderROS);

	// Subscribers for left and right motor velocities
	// Left motor
	ros::Subscriber<std_msgs::Int32> leftMotorROSSubscriber("left_motor_velocity", &callbackFuncitonMotorLeft);
	// Left motor
	ros::Subscriber<std_msgs::Int32> rightMotorROSSubscriber("right_motor_velocity", &callbackFuncitonMotorRight);

	void setup() {
	// Set the encoder
	pinMode(encoderPinLeft, INPUT);
	pinMode(encoderPinRight, INPUT);

	// Attach the interrupts for tracking the pulses
	attachInterrupt(digitalPinToInterrupt(encoderPinLeft), interputFunctionLeft, RISING);
	attachInterrupt(digitalPinToInterrupt(encoderPinRight), interputFunctionRight, RISING); 

	// Motors
	// Left Motor
	pinMode(ENA, OUTPUT);
	pinMode(IN1, OUTPUT);
	pinMode(IN2, OUTPUT);
	// Right Motor
	pinMode(IN3, OUTPUT);
	pinMode(IN4, OUTPUT);
	pinMode(ENB, OUTPUT);

	// Set all motors OFF
	// Left
	digitalWrite(IN1, LOW);
	digitalWrite(IN2, LOW);
	// Right
	digitalWrite(IN3, LOW);
	digitalWrite(IN4, LOW);


	// Set the serial communication parameter via Bluetooth
	// nh.getHardware()->setPort(&Serial)
	nh.getHardware()->setBaud(9600);

	// Initialize the ROS node
	nh.initNode();

	// Publishers
	nh.advertise(leftEncodeROSPublisher);
	nh.advertise(rightEncodeROSPublisher);
	// Subscribers
	nh.subscribe(leftMotorROSSubscriber);
	nh.subscribe(rightMotorROSSubscriber);

	}

	void loop() {
	nh.spinOnce();

	// Set the speed of the motor (PWM signals) from 0 to 255
	// the variables motorVelocityLeft and motorVelocityRight
	// are filled on the basis of the messages received from ROS
	analogWrite(ENA, motorVelocityLeft);
	analogWrite(ENB, motorVelocityRight);

	// Set the direction and turn ON
	// Left motor
	digitalWrite(IN1, LOW);
	digitalWrite(IN2, HIGH);
	// Right motor
	digitalWrite(IN3, LOW);
	digitalWrite(IN4, HIGH);

	// Send back the encoder readings
	leftEncoderROS.data = totalPulsesLeft;
	rightEncoderROS.data = totalPulsesRight;
	leftEncodeROSPublisher.publish(&leftEncoderROS);
	rightEncodeROSPublisher.publish(&rightEncoderROS);

	delay(5);
	}

	// Interrupt funciton left encoder
	void interputFunctionLeft() {
	// Increment the total number of pulses
	totalPulsesLeft = totalPulsesLeft + 1;
	}

	// Interrupt funciton left encoder
	void interputFunctionRight() {
	// Increment the total number of pulses
	totalPulsesRight = totalPulsesRight + 1;
	}