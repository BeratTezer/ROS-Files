# ROS Files

### Tutorial Files
#### Creating a catkin package
1. Go to the path: "catkin_ws/src". If not exist, create manually.
2. Then write and run this line: "catkin_create_pkg beginner_tutorials std_msgs rospy roscpp"
3. Then the tutorial files will be created.

#### Creating Nodes in "roscore"
1. First write "roscore", it will start a master.
2. Then go to the new terminal
3. To create a turtle, write "rosrun turtlesim turtlesim_node"
4. Then go to new termial and write "rosrun turtlesim turtle_teleop_key". This terminal will read commands and rotate the turtle.
5. To visualize the connection as a graph, write "rosrun rqt_graph rqt_graph"
6. Getting the list of publishers and subsricbers "rostopic list -v"
7. Getting the type of a node "rostopic type /turle1/cmd_vel" (cmd rostopic type {node name})
8. To getting the data outputs of nodes write "rosmsg show geometry_msgs/Twist" (rosmsg show {node type})

#### Create Catkin Workspace and Create Packages
1. Start by giving the source"source /opt/ros/melodic/setup.bash"
2. Configurations the bash script "gedit ~/.bashrc"
3. "echo "source /opt/ros/melodic/setup.bash" >> ~/.bashrc" thus this line you don't have to write "source /opt/ros/melodic/setup.bash" again and again.(It automatically source our ros enviroment when terminal starts)
4. Ready to setup our workspace.
5. Create a directory and sub-directory. (mkdir -p my_ros_project/src)
6. Go to the directory and write "catkin_make"
7. Give the path of setup.bash under devel file. "source ~/Desktop/ROS_Files/my_workspace_ros/devel/setup.bash"
8. Verify our workspace overlays the ROS workspace. Type "echo $ROS_PACKAGE_PATH" then if there is a result like "~/Desktop/ROS_Files/my_workspace_ros/src:/opt/ros/melodic/share" that means its okay.
9. Write "echo "source ~/Desktop/ROS_Files/my_workspace_ros/devel/setup.bash" >> ~/.bashrc" to won't give the source again and again as we perviously do in step 3.
10. Check the code "gedit ~/.bashrc". If there is the line we wrote at the bottom that means its alright. If you are going to DELETE your workspace, don't forget to clean "bashrc" file.
11. Now we are ready to create ros packages. Go to the under src file. Start with the following line "catkin_create_pkg new_package_ros"
12. Then go to the upper directory and write "catkin_make" 
13. Final step: Add workspace to the ROS environmet ". ~/Desktop/ROS_Files/my_workspace_ros/devel/setup.bash"

### Creating Publisher and Subscriber Nodes and Their Connection
#### Through a Topic in Python (File: Subscriber-and-Publisher-Nodes)
1. "gedit ~/.bashrc" check the ROS environment is sourced. At the end you must see "source /opt/ros/melodic/setup.bash". If you don't, add manually or go to step 2 in previous section.
2. Create workspace. "mkdir -p {full path or go to your main file and create new file like ros workspace}testros/src" (testros is the name of our workspace)
3. Go to the file. Write "catkin_make"
4. Then add the source "source ~/Desktop/ROS_Files/testros/devel/setup.bash"
5. Check the "echo $ROS_PACKAGE_PATH"
6. Then go to sub directory "src". To create the package, write "catkin_create_pkg test_ros std_msg rospy roscpp". In this line you can change the "test_ros" part.
7. This step might be unneccessariy. But the documents use this way.
8. Go to orinigal directory, I mean our main file (go back to the workspace). Write "catkin_make" again.
9. We will see a line we didn't see before. (Processing catkin package: '{file-name}'", this name going to be same as we gave in step 6)
10. Add the source again. ". devel/setup.bash". At this step, I was in directory we create in 2. step.
11. Go to the sub directory: "cd src/test_ros". It's under the testros file.
12. Then create a sub folder named "python_script". To do it write this: "mkdir python_script". Go to the file we created. Write "gedit publisher_node.py"
13. Fill the "publisher_node.py". I added the example code with same name.
14. Change the access and executable rights, make the file executable. "chmod +x publisher_node.py" for this code.
15. Edit the "CMakeLists.txt" file. To do this, write "gedit CMakeLists.txt".
16. Find these lines.
	<p>
		## Mark executable scripts (Python etc.) for installation<br>
		## in contrast to setup.py, you can choose the destination<br>
		# catkin_install_python(PROGRAMS<br>
		#&nbsp&nbsp&nbspscripts/my_python_script<br>
		#&nbsp&nbsp&nbspDESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}<br>
		# )<br>
	</p>
17. Change the code as I do below.
	<p>
		## Mark executable scripts (Python etc.) for installation<br>
		## in contrast to setup.py, you can choose the destination<br>
		catkin_install_python(PROGRAMS<br>
		&nbsp&nbsp&nbsppython_script/publisher_node.py # {this is your python scripts path. Better you give the full path}<br>
		&nbsp&nbsp&nbspDESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}<br>
		)<br>
	</p>
18. Test the publisher node. Now we need to run our master ros. Go to a new terminal and type "roscore".
19. Go to the new terminal and go to test_ros path. Then type the test python script. Write "rosrun test_ros publisher_node.py" (If it says "Error: package 'test_ros' not found" write this and try again: "source ~/testros/devel/setup.bash
")
20. Then go to the new terminal. Each we go to the new terminal, we gotta give our source again and again for our current project. Write "source ~/testros/devel/setup.bash".
21. We check the rostopics. Type "rostopic list" and check your list. Now we should see /information, /rosout and /rosout_agg. Last two of them are created with "roscore" but the new one, I mean /information, it's our publisher_node.py file. If we check, we can see the "topicName" inside of the publisher file. That mean we can easily change it's name but we won't do that. Let's create a subsricber for our publisher.
22. Go to the "python_scripts" folder. Write "gedit subscriber_node.py" then copy the content of shared file above.
23. Make the subscriber_node.py rights the executable too -> "chmod +x subscriber_node.py"
24. Now we will update the "CMakeLists.txt". Write "gedit CMakeLists.txt", add the subscriber python script.
	<p>
		## Mark executable scripts (Python etc.) for installation<br>
		## in contrast to setup.py, you can choose the destination<br>
		catkin_install_python(PROGRAMS<br>
		&nbsp&nbsp&nbsppython_script/publisher_node.py # {this is your python scripts path. Better you give the full path}<br>
		&nbsp&nbsp&nbsppython_script/subscriber_node.py # {this is your python scripts path. Better you give the full path}<br>
		&nbsp&nbsp&nbspDESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}<br>
		)<br>
	</p>
25. TESTING: Do these.
	* roscore
	* Go to new terminal. Write "source ~/testros/devel/setup.bash"
	* Then write "rosrun test_ros publisher_node.py"
	* Go to new terminal. Write "source ~/testros/devel/setup.bash"
	* Then write "rosrun test_ros subscriber_node.py"
	* In the last terminal, we will see each received messages.
	


### ROS and OpenCV
#### Robotics and Computer Vision in Python
1. Make sure your camera is working.
2. Open a terminal, type "ls /dev/|grep video". If we can see video0 output, its how it should be.
3. Write "sudo apt install ros-melodic-usb-cam". This willl install ROS cam files.
4. Write "sudo apt install ros-melodic-perception". This willl install ROS OpenCV and some perception files.
5. Verify ROS environment is sourced. Write "gedit ~/.bashrc". Go to the end of the file and see this "source /opt/ros/melodic/setup.bash". If you can't see, add manually and save the file.
6. Create a workspace. Write following lines step by step.
	* "mkdir -p ~/ros_open_cv_ws/src"
	* "cd ~/ros_open_cv_ws"
	* "catkin_make"
	* "source ~/ros_open_cv_ws/devel/setup.bash"
	* "echo $ROS_PACKAGE_PATH" (~/ros_open_cv_ws/src:/opt/ros/melodic/share)
7. Create a catkin package and nodes.
	* "cd ~/ros_open_cv_ws/src"
	* "catkin_create_pkg ros_opencv image_transport cv_bridge sensor_msgs rospy roscpp std_msgs" (After the ros_opencv, rest of them are dependenies of the package. First thing we write is our command, and the second one is our package name which is ros_opencv)
	* Go to inside of the "ros_opencv" file
	* "mkdir python_scripts"
	* "cd python_scripts"
	* "gedit camera_publisher.py" (You can copy and paste it from ROS-OpenCV-Capture-Publisher file)
	* "chmod +x camera_publisher.py"
	* "gedit camera_subscriber.py" (You can copy and paste it from ROS-OpenCV-Capture-Publisher file)
	* "chmod +x camera_subscriber.py"
	* "gedit CMakeLists.txt" (Add the python scripts under Installation)
	* Go to "cd ~/ros_open_cv_ws" and type "catkin_make"
8. Testing.
	* Close all terminals and open a new one. Write "roscore"
	* Go to new terminal, "source ~/ros_open_cv_ws/devel/setup.bash"
	* "rosrun ros_opencv camera_publisher.py"
	* "rosrun ros_opencv camera_subscriber.py"
	* Then you will see the video frame from your camera.

### ROS and Arduino
#### How to start with ROS and Arduino
1. Install the neccessary libraries. Go to the terminal and write these; 
	* "sudo apt install ros-melodic-rosserial"
	* "sudo apt install ros-melodic-rosserial-arduino"
	* "sudo apt install ros-melodic-rosserial-python"
2. Download the Arduino sofware. In Ubuntu, you can download it from Ubuntu Software. 
3. Specify a folder to save whole Arduino sketchs and libraries. Open the Arduino sofware. Folder->Preferences->Sketchbook Location->/home/{username}/ArduinoSketches(you can create the folder manually)->Ok
4. Install the Arduino ROS Communication Library. Go to the Arduino Software again. Sketch->Include Library->Manage Libraries->Search->"rosserial"->Rosserial Arduino Libray->Install
5. Let's see the examples. File->Examples->Rosserial Arduino Library->HeloWorld. Then the example file will open automatically.
6. There is a fix we need to do. Go to the path in file explorer "/home/{username}/ArduinoSketches/libraries/Rosserial_Arduino_Library/src/ros" and open the "msg.h" file.
	* Replace "#include <cstring>" line with this: "#include <string.h>". 
	* (Line 68) Replace "std::memcpy(&val, &f, sizeof(val));" to "memcpy(&val, &f, sizeof(val));"
	* (Line 182) Replace "std::memcpy(f, &val, sizeof(val));" to "memcpy(f, &val, sizeof(val));"
7. Set the porper permissions for our communication port. Go to the terminal, write "sudo chmod 666 /dev/ttyACM0". To check the port we will communicate; go to the Arduino. Tools->Port->/dev/ttyACM0. If you can see this, that's mean it will work.
8. Go to terminal and run "rosrun rosserial_python serial_node.py /dev/ttyACM0"
9. Now it's working. To see that, run "rostopic echo /chatter"

#### Python ROS Publisher and Subscriber Nodes and Interface with Arduino
 Nodes | Python Publisher | ROS | Arduino | ROS | Python Subscriber |
--- | --- | --- | --- |--- |---
Explanation | Python script publishes integer to topic as "information" | -> | Arduino subscribes and receives integers from topic "information". Arduino multiplies integers by 2 and publishs the results to topic "info_back" | -> | Python script subscribes to topic "info_back" and prints the results on the screen | 
1. Open a terminal
	* "mkdir ~p ~/ros_arduino_ws/src"
	* "cd ~/ros_arduino_ws"
2. Create package
	* "catkin_make"
	* "source ~/ros_arduino_ws/devel/setup.bash"
	* "cd ~/ros_arduino_ws/src"
	* "catkin_create_pkg arduino_test_comm std_msgs rospy roscpp"
3. Create publisher and subscriber files
	* "cd ~/ros_arduino_ws/src/arduino_test_comm/src"
	* "gedit publisherArduino.py"
	* "gedit subscriberArduino.py"
	* Now we will write the code. You can easily copy and paste it from Arduino-Interface-Communication folder.
	* Set the execution privileges for both files
		- "chmod +x publisherArduino.py"
		- "chmod +x subscriberArduino.py"
	* Create a new Arduino Sketch named "arduino_communication" and fill the file.
		- You can also find it in README.md file in Arduino-Interface-Communication folder.
4. Check the port name. It should be "/dev/ttyACM0"
5. TESTING:
	* Go to the terminal and write "roscore"
	* Open a new one and run "sudo chmod 666 /dev/ttyACM0"
	* Then run "rosrun rosserial_python serial_node.py /dev/ttyACM0" this start the "serial_node.py"
	* Then open a new terminal then run "rosrun arduino_test_comm publisherArduino.py"
	* Start the subscriber node. Open a new terminal; "source ~/ros_arduino_ws/devel/setup.bash" and write "rosrun arduino_test_comm subscriberArduino.py"

### ROS Tutorial on Remote Control and Remote Sensing of Differential Wheeled Robot by Using Arduino and Bluetooth
 Nodes | Python Publisher | ROS | Arduino | ROS | Python Subscriber |
--- | --- | --- | --- |--- |---
Explanation | Python script publishes velocity commands to the topic: "left_motor_velocity" and "right_motor_velocity" | -> | Arduino subscribes to the topics "left_motor_velocity" and "right_motor_velocity" and receives velocity commands. It runs the motors. Arduino publishes encoder readings to the topics: "left_encoder_pulses" and "right_encoder_pulses" | -> | Python script subscribes to the topics: "left_encoder_pulse" and "right_encoder_pulses" and prints the encode readings to the screen |
1. Create a Wrokspace and Create a Package
	* "mkdir -p ~/ros_remote_ws/src"
	* "cd ~/ros_remote_ws"
	* "catkin_make"
	* "source ~/ros_remote_ws/devel/setup.bash"
	* "cd ~/ros_remote_ws/src"
	* "catkin_create_pkg ros_remote_pkg std_msgs rospy roscpp"
2. Create the publisher and subscriber files
	* "cd ~/ros_remote_ws/src/ros_remote_pkg/src"
		- "gedit publisherArduino.py" then save.
		- "gedit publisherArduino.py" save it too. You can find scripts in README.md files.
	* Set the execution privileges.
		- "chmod +x publisherArduino.py"
		- "chmod +x subscriberArduino.py"
3. Write the Arduino Code.
	* "cd ~/ros_remote_ws/src/ros_remote_pkg/src"
	* "gedit arduino_communication.ino" then save.
	* Go to the file explorer and fill the code. You can also find the code in README.md
4.  Initialize the Bluetooth conneciton from a Linux terminal
	* "sudo rdcomm connect /dev/rfcomm0 98:DA:60:08:2F:9F"
		- "/dev/rfcomm0" is device name
		- "/98:DA:60:08:2F:9F" is the adress of the device that etablishing the Bluetooth connection.
	* If you cannot connect to the device, you should run this command "sduo rfcomm release 0". This will reset the communication port.
5. Open Rosserial Communication
	* Open a new terminal. Write "roscore"
	* Open a new terminal, "rosrun rosserial_python serial_node.py _port=/dev/rfcomm=_baud:=9600"
		- Baud rate must match the baud rate specified in Arduino
	* Open a new terminal and tpye "rostopic list". You should see these:
		- /diagnostics
		- /left_encoder_pulses
		- /left_motor_velocity
		- /right_encoder_pulses
		- /right_motor_velocity
		- /rosout
		- /rosout_agg
6. Start the subscriber and publisher nodes.
	* To start the subscriber node, open a new terminal and type:
		- "source ~/ros_remote_ws/devel/setup.bash"
		- "rosrun ros_remote_pkg subscriberArduino.py"
	* To start the publisher node, open a new terminal and type:
		- "source ~/ros_remote_ws/devel/setup.bash"
		- "rosrun ros_remote_pkg publisherArduino.py"

### Control of Two-Wheeled Robot in RVIZ
1. Create the file and workspace
	* "mkdir -p control_of_two_wheeled_robot/src"
	* "cd control_of_two_wheeled_robot/"
	* "catkin_make"
	* "source ~/control_of_two_wheeled_robot/devel/setup.bash"
	* "cd src"
	* "catkin_create_pkg control_of_two_wheeled_robot std_msgs rospy roscpp tf2 geometry_msgs urdf rviz joint_state_publisher_gui xacro"
	* "cd ~/control_of_two_wheeled_robot"
	* "catkin_make"
	- Source again
	* "source ~/control_of_two_wheeled_robot/devel/setup.bash"
2. Create the robot.
	* "cd ~/control_of_two_wheeled_robot/src/control_of_two_wheeled_robot"
    * "mkdir urdf"
    * "mkdir launch"
    * "cd urdf"
    * "gedit material_color.xacro". You can find the content in related README.md
    * "gedit robot.xacro". You can find the content in related README.md
	* "cd ~/control_of_two_wheeled_robot/src/control_of_two_wheeled_robot/launch"
	* "gedit robot_xacro.launch" You can find the content in related README.md
	- Return the original workspace
	* "cd ~/control_of_two_wheeled_robot"
	* "catkin_make"
3. Create the script files
	* "cd src/control_of_two_wheeled_robot"
	- Create the script file
	* "mkdir python_scripts"
	* "cd python_scripts"
	* "gedit publisher_node.py" (You can find the content in related Readme.md file)
	- Give the rights of the script
	* "chmod +x publisher_node.py"
4. Change the CMAKE file
	* "cd .."
	* "gedit CMakeLists.txt"
	- Find these lines.
		<p>
			## Mark executable scripts (Python etc.) for installation<br>
			## in contrast to setup.py, you can choose the destination<br>
			# catkin_install_python(PROGRAMS<br>
			#&nbsp&nbsp&nbspscripts/my_python_script<br>
			#&nbsp&nbsp&nbspDESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}<br>
			# )<br>
		</p>
	- Change the code as I do below.
		<p>
			## Mark executable scripts (Python etc.) for installation<br>
			## in contrast to setup.py, you can choose the destination<br>
			catkin_install_python(PROGRAMS<br>
			&nbsp&nbsp&nbsppython_script/publisher_node.py # {this is your python scripts path. Better you give the full path}<br>
			&nbsp&nbsp&nbspDESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}<br>
			)<br>
		</p>
5. Test the script.
	- Go to a new terminal
	* "roscore"
	- Go to another new terminal and give the source again
	* "source ~/control_of_two_wheeled_robot/devel/setup.bash"
	* "rosrun control_of_two_wheeled_robot publisher_node.py"
	- If you can see "Success" in the end of the line, that mean it is okay. 
6. Another python script.
	- Return to the script file
	* "cd ~/control_of_two_wheeled_robot/src/control_of_two_wheeled_robot/python_scripts"
	* "gedit subscriber_node.py" (You can find the content in related Readme.md file)
	- Give the rights of the script
	* "chmod +x subscriber_node.py"
7. Change the CMAKE file again.
	* "cd .."
	* "cd .."
	* "gedit CMakeLists.txt"
	- Find these lines
		<p>
			## Mark executable scripts (Python etc.) for installation<br>
			## in contrast to setup.py, you can choose the destination<br>
			catkin_install_python(PROGRAMS<br>
			&nbsp&nbsp&nbsppython_scripts/publisher_node.py<br>
			DESTINATION ${(Path of the src file which contain the python_scripts file)}<br>
			)
		</p>
	- Change the code as I do
		<p>
			## Mark executable scripts (Python etc.) for installation<br>
			## in contrast to setup.py, you can choose the destination<br>
			catkin_install_python(PROGRAMS<br>
			&nbsp&nbsp&nbsppython_scripts/publisher_node.py<br>
			&nbsp&nbsp&nbsppython_scripts/subscriber_node.py<br>
			DESTINATION ${(Path of the src file which contain the python_scripts file)}<br>
			)
		</p>
8. TESTING: Do these.
	* roscore
	* Go to new terminal. Write "source ~/control_of_two_wheeled_robot/devel/setup.bash"
	* Then write "rosrun control_of_two_wheeled_robot publisher_node.py"
	* Go to new terminal. Write "source ~/control_of_two_wheeled_robot/devel/setup.bash"
	* Then write "rosrun control_of_two_wheeled_robot subscriber_node.py"
	* In the last terminal, we will see each received messages.

### Move robot with the pilz_command_planner
1. Install Pilz robot package
	- Open a terminal
	* "sudo apt update"
	* "sudo apt install ros-melodic-pilz-robots"
	- Test it before next step
	* "roslaunch prbt_moveit_config moveit_planning_execution.launch" This must be working properly.
2. Create Application ROS Package
	* "mkdir -p ~/move_robot_with_pilz/src"
	* "cd ~/move_robot_with_pilz/src"
	* "catkin_create_pkg pilz_tutorial prbt_moveit_config"
	- Load the stl file
	* "cd ~/move_robot_with_pilz/src/pilz_tutorial"
	* "mkdir -p urdf/meshes"
	- Describe the robot
	* "cd ~/move_robot_with_pilz/src/pilz_tutorial/urdf"
	* "gedit my_first_application.xacro" Find the content in related Readme file
	- Create a launch file to start up the robot environment
	* "cd ~/move_robot_with_pilz/src/pilz_tutorial"
	* "mkdir launch"
	* "gedit launch/my_application.launch" Find the content in related Readme file
	- Complete the 
	* "cd ~/move_robot_with_pilz"
	* "catkin_make"
	- Cite the source
	* "source ~/move_robot_with_python/devel/setup.bash"
5. Run
	* "roslaunch pilz_tutorial my_application.launch"

### Move robot with the Python API
1. Install Pilz robot package
	- Open a terminal
	* "sudo apt update"
	* "sudo apt install ros-melodic-pilz-robots"
	* "sudo apt install ros-melodic-pilz-robot-programming"
	- Test it before next step
	* "roslaunch prbt_moveit_config moveit_planning_execution.launch" This must be working properly.
2. Create Application ROS Package
	* "mkdir -p ~/move_robot_with_python/src"
	* "cd ~/move_robot_with_python/src"
	* "catkin_create_pkg pilz_tutorial prbt_moveit_config"
	- Load the stl file
	* "cd ~/move_robot_with_python/src/pilz_tutorial"
	* "mkdir -p urdf/meshes"
	- Describe the robot
	* "cd ~/move_robot_with_python/src/pilz_tutorial/urdf"
	* "gedit my_first_application.xacro" Find the content in related Readme file
	- Create a launch file to start up the robot environment
	* "cd ~/move_robot_with_python/src/pilz_tutorial"
	* "mkdir launch"
	* "gedit launch/my_application.launch" Find the content in related Readme file
	- Create the script folder and script file
	* "cd ~/move_robot_with_python/src/pilz_tutorial"
	* "mkdir scripts"
	* "cd scripts"
	* "gedit python_script.py" Find the content in related Readme file
	* "chmod +x python_script.py"
	- Change the CMakeLists.txt in pilz_tutorial
	* "cd ~/move_robot_with_python/src/pilz_tutorial"
	* "gedit CMakeLists.txt"
	- Find these lines
		<p>
			## Mark executable scripts (Python etc.) for installation<br>
			## in contrast to setup.py, you can choose the destination<br>
			catkin_install_python(PROGRAMS<br>
			&nbsp&nbsp&nbsppython_scripts/publisher_node.py<br>
			DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}<br>
			)
		</p>
	- Change the code as I do
		<p>
			## Mark executable scripts (Python etc.) for installation<br>
			## in contrast to setup.py, you can choose the destination<br>
			catkin_install_python(PROGRAMS<br>
			&nbsp&nbsp&nbspcdscripts/python_script.py<br>
			DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}<br>
			)
		</p>
	- Complete the file 
	* "cd ~/move_robot_with_python"
	* "catkin_make"
	- Cite the source
	* "source ~/move_robot_with_python/devel/setup.bash"
5. Run
	* "roslaunch pilz_tutorial my_application.launch"
	- Go to a new terminal and run the script, before the script cite the source again
	* "source ~/move_robot_with_python/devel/setup.bash"
	* "rosrun pilz_tutorial python_script.py"

# Commands
#### Rosnode Commands:
	- rosnode list -> list active nodes
	- rosnode ping -> test connectivity to node
	- rosnode info -> print information about node
	- rosnode machine -> list nodes running on a particular machine or list machines
	- rosnode kill -> kill a running node
	- rosnode cleanup -> purge registration information of unreachable nodes

#### Rostopic Commands:
	- rostopic bw -> display bandwidth used by topic
	- rostopic delay -> display delay of topic from timestamp in header
	- rostopic echo -> print messages to screen
	- rostopic find -> find topics by type
	- rostopic hz -> display publishing rate of topic
	- rostopic info -> print information about active topic
	- rostopic list -> list active topics
	- rostopic pub -> publish data to topic
	- rostopic type -> print topic or field type