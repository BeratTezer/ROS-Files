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
To getting the data outputs of nodes write "rosmsg show geometry_msgs/Twist" (rosmsg show {node type})<br><br><br>

### Create Catkin Workspace and Create Packages
1. Start by giving the source"source /opt/ros/melodic/setup.bash"
2. Configurations the bash script "gedit ~/.bashrc"
3. "echo "source /opt/ros/melodic/setup.bash" >> ~/.bashrc" thus this line you don't have to write "source /opt/ros/melodic/setup.bash" again and again.(It automatically source our ros enviroment when terminal starts)
4. Ready to setup our workspace
5. Create a directory and sub-directory. (mkdir -p my_ros_project/src)
6. Go to the directory and write "catkin_make"
7. Give the path of setup.bash under devel file. "source ~/Desktop/ROS_Files/my_workspace_ros/devel/setup.bash"
8. Verify our workspace overlays the ROS workspace. Type "echo $ROS_PACKAGE_PATH" then if there is a result like "~/Desktop/ROS_Files/my_workspace_ros/src:/opt/ros/melodic/share" that means its okay.
9. Write "echo "source ~/Desktop/ROS_Files/my_workspace_ros/devel/setup.bash" >> ~/.bashrc" to won't give the source again and again as we perviously do in step 3.
10. Check the code "gedit ~/.bashrc". If there is the line we wrote at the bottom that means its alright. If you are going to DELETE your workspace, don't forget to clean "bashrc" file.
11. Now we are ready to create ros packages. Go to the under src file. Start with the following line "catkin_create_pkg new_package_ros"
12. Then go to the upper directory and write "catkin_make" 
13. Final step: Add workspace to the ROS environmet ". ~/Desktop/ROS_Files/my_workspace_ros/devel/setup.bash"

### Creating Publisher and Subscriber Nodes and Connect
#### Through a Topic in Python



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


