# ROS_Files

## Creating a catkin Package
Go to the path: "catkin_ws/src". If not exist, create manually.
Then write and run this line: "catkin_create_pkg beginner_tutorials std_msgs rospy roscpp"
Then the tutorial files will be created.


## Creating Nodes in "roscore"
With this command "rosrun turtlesim turtlesim_node", we will be created one ros node.
To move the turtle, "rosrun turtlesim turtle_teleop_key" and use arrow keys.

	Rosnode Commands:
		- rosnode list -> list active nodes
		- rosnode ping -> test connectivity to node
		- rosnode info -> print information about node
		- rosnode machine -> list nodes running on a particular machine or list machines
		- rosnode kill -> kill a running node
		- rosnode cleanup -> purge registration information of unreachable nodes

	Rostopic Commands:
		- rostopic bw -> display bandwidth used by topic
		- rostopic delay -> display delay of topic from timestamp in header
		- rostopic echo -> print messages to screen
		- rostopic find -> find topics by type
		- rostopic hz -> display publishing rate of topic
		- rostopic info -> print information about active topic
		- rostopic list -> list active topics
		- rostopic pub -> publish data to topic
		- rostopic type -> print topic or field type

