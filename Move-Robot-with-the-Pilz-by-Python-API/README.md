# Scripts:

## Python Script:
    #!/usr/bin/env python

    from geometry_msgs.msg import Pose, Point
    from pilz_robot_programming import *
    import math
    import rospy

    __REQUIRED_API_VERSION__ = "1"  # API version
    __ROBOT_VELOCITY__ = 0.5        # velocity of the robot

    # main program
    def start_program():
        print(r.get_current_pose()) # print the current position of thr robot in the terminal

    if __name__ == "__main__":
        # init a rosnode
        rospy.init_node('robot_program_node')

        # initialisation
        r = Robot(__REQUIRED_API_VERSION__)  # instance of the robot

        # start the main program
        start_program()

## Xacro File:
    <?xml version="1.0" ?>

    <robot name="prbt" xmlns:xacro="http://www.ros.org/wiki/xacro">

    <!-- macro definition of pilz lwa -->
    <xacro:include filename="$(find prbt_support)/urdf/prbt_macro.xacro" />

    <!-- coloring from the stl file -->
    <material name="yellow">
        <color rgba="1 1 0 1"/>
    </material>

    <!-- coloring from the table -->
    <material name="grey">
        <color rgba="0.75 0.75 0.75 1"/>
    </material>

    <!-- instantiate the robot -->
    <xacro:prbt prefix="prbt_"/>

    <link name="table">
        <visual>
        <origin rpy="0 0 0" xyz="0 -0.45 -0.03"/>
        <geometry>
            <box size="0.6 1.2 0.05"/>
        </geometry>
        <material name="grey"/>
        </visual>
    </link>

    <link name="pnoz">
        <visual>
        <origin rpy="1.5708 0 0" xyz="0 -0.5 0"/>
        <geometry>
            <mesh filename="package://pilz_tutorial/urdf/meshes/PNOZ.stl"
            scale="0.001 0.001 0.001"/>
        </geometry>
        <material name="yellow"/>
        </visual>
    </link>

    <joint name="table_joint" type="fixed">
        <parent link="table"/>
        <child link="prbt_base_link"/>
    </joint>

    <joint name="pnoz_joint" type="fixed">
        <parent link="table"/>
        <child link="pnoz"/>
    </joint>
    
    </robot>

## Launch File:
    <?xml version="1.0"?>
    <launch>

    <arg name="sim" default="true" />

    <!-- send urdf to param server -->
    <param name="robot_description"
        command="$(find xacro)/xacro '$(find pilz_tutorial)/urdf/my_first_application.xacro'"/>

    <include file="$(find prbt_moveit_config)/launch/moveit_planning_execution.launch">
        <arg name="load_robot_description" value="false"/>
        <arg name="sim" value="$(arg sim)"/>
    </include>

    </launch>