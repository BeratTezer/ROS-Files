# ROS_Files

## Creating a catkin Package
Go to the path: "catkin_ws/src". If not exist, create manually.<br>
Then write and run this line: "catkin_create_pkg beginner_tutorials std_msgs rospy roscpp"<br>
Then the tutorial files will be created.<br>

## Creating Nodes in "roscore"
First write "roscore", it will start a master.<br>
Then go to the new terminal<br>
To create a turtle, write "rosrun turtlesim turtlesim_node"<br>
Then go to new termial and write "rosrun turtlesim turtle_teleop_key". This terminal will read commands and rotate the turtle.<br>
To visualize the connection as a graph, write "rosrun rqt_graph rqt_graph"<br>
Getting the list of publishers and subsricbers "rostopic list -v"<br>
Getting the type of a node "rostopic type /turle1/cmd_vel" (cmd rostopic type {node name})<br>
To getting the data outputs of nodes write "rosmsg show geometry_msgs/Twist" (rosmsg show {node type})<br>

<br><br><br>

### Rosnode Commands:
	- rosnode list -> list active nodes
	- rosnode ping -> test connectivity to node
	- rosnode info -> print information about node
	- rosnode machine -> list nodes running on a particular machine or list machines
	- rosnode kill -> kill a running node
	- rosnode cleanup -> purge registration information of unreachable nodes

### Rostopic Commands:
	- rostopic bw -> display bandwidth used by topic
	- rostopic delay -> display delay of topic from timestamp in header
	- rostopic echo -> print messages to screen
	- rostopic find -> find topics by type
	- rostopic hz -> display publishing rate of topic
	- rostopic info -> print information about active topic
	- rostopic list -> list active topics
	- rostopic pub -> publish data to topic
	- rostopic type -> print topic or field type

