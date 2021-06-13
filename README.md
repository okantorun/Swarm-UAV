# Swarm-UAV 

## Installation
- This project is developed in crazyswarm (see: https://crazyswarm.readthedocs.io/en/latest/index.html)
- Firstly you should install Ros (see: https://www.ros.org/)
- Then you should install crazyswarm. We will use just python api.

### How to install Crazyswarm for just Python API 
(https://crazyswarm.readthedocs.io/en/latest/installation.html)

1- __Set enviroment veriable__
```
$ export CSW_PYTHON=[python2 or python3]
```
2- __Install depencies__
```
$ sudo apt install git make gcc swig lib${CSW_PYTHON}-dev ${CSW_PYTHON}-numpy ${CSW_PYTHON}-yaml ${CSW_PYTHON}-matplotlib
```
3- __Clone Repo__
```
$ git clone https://github.com/USC-ACTLab/crazyswarm.git
```
4- __Run build script__
```
$ cd crazyswarm
$ ./buildSimOnly.sh
```



## Simulation
<p align="center">
  <img src="media/square-formation.gif" width="280"> 
  <br />
  <img src="media/take-off-square.gif" width="280">
</p>




## Menu
- It is a control menu created to simulate the developed algorithms.

### How It Works ?
#### ![ss](https://i.hizliresim.com/j5cm3q1.png)
- First of all, choose drone number.
- Second, choose whether the drones will take off simultaneously or individually.
- Choose how many meters they will rise.
- Choose the distance between drones. 
#### ![ss1](https://i.hizliresim.com/eiz26zi.png)
-	The formation that can be entered is selected according to the number of drones. 
#### ![ss2](https://i.hizliresim.com/rdgj1p0.png)
- Different tasks can be performed with the specified numbers.


### Algorithms
#### -set_triang_formation                                                                                                                           

 
 
 The purpose of this function is to create a triangle formation with the UAVs in the system<br/>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;--Parameters the Function Takes Are<br/>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1- distance = is the distance between the two vertices of the triangle you want to form<br/>
	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2- drone_number = number of drones in the system<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3- init_point = center at the time the swarm members call a function<br/>
	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4- altitude = height of swarm members<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;5- rotation = angles of swarm members with respect to the main coordinate system<br/>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;--Description Of the Algorithm<br/>
 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Step 1 = 3x3 unit matrix named desired_matrix is created for the three corners of the triangle to be created. Where the rows represent UAVs. The 1st column represents the x-axis, the 2nd column represents the y-axis, and the 3rd column represents the z-axis.<br/><br/>
	 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;	Step 2 = 3 line arrays are created for the side lines of the triangle, but they are empty. Will be resized.<br/><br/>
 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;		Step 3 = On the relative coordinate system on which the swarm system is located, the corner points of the triangle are calculated using geometric relations and assigned to the desired_matrix.<br/><br/>
 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;		Step4 = If there are more than three UAVs in the swarm, they are placed on the border lines by editing the line variable with the re_construct_line function(The re_construct_line function will be explained later).<br/><br/>
 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;		Step5 = All of the specified coordinates are assigned to the desired_matrix variable and the transformed_matrix is created.<br/><br/>
	 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;	Step 6 = All coordinates are arranged according to the absolute frame with the transformation_2d function and transferred to the transformed_matrix.<br/><br/>


#### -set_square_formation:

The purpose of this function is to create a square formation with the UAVs in the system.<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;	--Parameters the Function Takes Are:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;		1- distance = is the distance between the two vertices of the square you want to form.<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;	  2- drone_number = number of drones in the system<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;		3- init_point = center at the time the swarm members call a function<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;		4- altitude = height of swarm members<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;		5- rotation = angles of swarm members with respect to the main coordinate system<br/>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;--Description Of the Algorithm:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;		Step 1 = 4x3 unit matrix named desired_matrix is created for the four corners of the square to be created. Where the rows represent UAVs. The 1st column represents the x-axis, the 2nd column represents the y-axis, and the 3rd column represents the z-axis.<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;		Step 2 = 4 line arrays are created for the side lines of the square, but they are empty. Will be resized.<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;		Step 3 = On the relative coordinate system on which the swarm system is located, the corner points of the square are calculated using geometric relations and assigned to the desired_matrix.<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;		Step4 = If there are more than four UAVs in the swarm, they are placed on the border lines by editing the line variable with the re_construct_line function(The re_construct_line function will be explained later).<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;		Step5 = All of the specified coordinates are assigned to the desired_matrix variable and the transformed_matrix is created.<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;		Step 6 = All coordinates are arranged according to the absolute frame with the transformation_2d function and transferred to the transformed_matrix.<br/>



#### -set_v_formation

The purpose of this function is to create a ‘v’ formation with the UAVs in the system.<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;	--Parameters the Function Takes Are:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;		1- distance = is the distance between the two vertices of the ‘v’ you want to form.<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;		2- yaw_angle = is the angle between two lines.<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;		3- drone_number = number of drones in the system<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;		4- init_point = center at the time the swarm members call a function<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;		5- altitude = height of swarm members<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;		6- rotation = angles of swarm members with respect to the main coordinate system<br/>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;--Description Of the Algorithm:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;		Step 1 = (drone_number)x3 unit matrix named desired_matrix is created for each element of the formation to be created. Where the rows represent UAVs. The 1st column represents the x-axis, the 2nd column represents the y-axis, and the 3rd column represents the z-axis.<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;		Step 2 = On the relative coordinate system on which the swarm system is located, the lines of the v formation are calculated using geometric relations and assigned to the desired_matrix.<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;		Step 3 = All of the specified coordinates are assigned to the desired_matrix variable and the transformed_matrix is created.<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;		Step 4 = All coordinates are arranged according to the absolute frame with the transformation_2d function and transferred to the transformed_matrix.<br/>



#### -set_pentagon_formation:

The purpose of this function is to create a pentagon formation with the UAVs in the system.<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;	--Parameters the Function Takes Are:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;		1- distance = is the distance between the two vertices of the pentagon you want to form.<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;		2- drone_number = number of drones in the system<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;		3- init_point = center at the time the swarm members call a function<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;		4- altitude = height of swarm members<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;		5- rotation = angles of swarm members with respect to the main coordinate system<br/>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;--Description Of the Algorithm:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;		Step 1 = 5x3 unit matrix named desired_matrix is created for the five corners of the pentagon to be created. Where the rows represent UAVs. The 1st column represents the x-axis, the 2nd column represents the y-axis, and the 3rd column represents the z-axis.<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;		Step 2 = 5 line arrays are created for the side lines of the pentagon, but they are empty. Will be resized.<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;		Step 3 = On the relative coordinate system on which the swarm system is located, the corner points of the pentagon are calculated using geometric relations and assigned to the desired_matrix.<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;		Step4 = If there are more than five UAVs in the swarm, they are placed on the border lines by editing the line variable with the re_construct_line function(The re_construct_line function will be explained later).<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;		Step5 = All of the specified coordinates are assigned to the desired_matrix variable and the transformed_matrix is created.<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;		Step 6 = All coordinates are arranged according to the absolute frame with the transformation_2d function and transferred to the transformed_matrix.<br/>

#### -set_star_formation:

The purpose of this function is to create a star formation with the UAVs in the system.<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;	--Parameters the Function Takes Are:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;		1- distance = is the distance between the two vertices of the star you want to form.<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;		2- drone_number = number of drones in the system<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;		3- init_point = center at the time the swarm members call a function<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;		4- altitude = height of swarm members<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;		5- rotation = angles of swarm members with respect to the main coordinate system<br/>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;--Description Of the Algorithm:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;		Step 1 = 10x3 unit matrix named desired_matrix is created for the ten corners of the star to be created. Where the rows represent UAVs. The 1st column represents the x-axis, the 2nd column represents the y-axis, and the 3rd column represents the z-axis.<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;		Step 2 = 10 line arrays are created for the side lines of the star, but they are empty. Will be resized.<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;		Step 3 = On the relative coordinate system on which the swarm system is located, the corner points of the star are calculated using geometric relations and assigned to the desired_matrix.<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;		Step4 = If there are more than ten UAVs in the swarm, they are placed on the border lines by editing the line variable with the re_construct_line function(The re_construct_line function will be explained later).<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;		Step5 = All of the specified coordinates are assigned to the desired_matrix variable and the transformed_matrix is created.<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;		Step 6 = All coordinates are arranged according to the absolute frame with the transformation_2d function and transferred to the transformed_matrix.<br/>

#### -set_crescent_formation:

The purpose of this function is to create a crescent formation with the UAVs in the system.<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;	--Parameters the Function Takes Are:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;		1-radius = determines the radius of the crescent that will be created<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;		2- gap_angle = represents the angle value of the part of the crescent that will be empty<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;		3- drone_number = number of drones in the system<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;		4- init_point = center at the time the swarm members call a function<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;		5- altitude = height of swarm members<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;		6- rotation = angles of swarm members with respect to the main coordinate system<br/>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;--Description Of the Algorithm:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;		Step1 = 2 endpoints of the crescent are determined <br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;		Step 2 = (drone_number)x3 unit matrix named desired_matrix is created to generate the crescent line. Where the rows represent UAVs. The 1st column represents the x-axis, the 2nd column represents the y-axis, and the 3rd column represents the z-axis.<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;		Step 3 =In the while loop, the coordinates of each UAV are calculated according to the angle values and transferred to the desired_matrix.<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;		Step4 = All of the specified coordinates are assigned to the desired_matrix variable and the transformed_matrix is created.<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;		Step5 = All coordinates are arranged according to the absolute frame with the transformation_2d function and transferred to the transformed_matrix.<br/>


#### -set_circle_formation:
The purpose of this function is to create a cicle formation with the UAVs in the system.<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;	--Parameters the Function Takes Are:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;		1-radius = determines the radius of the crescent that will be created<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;		2- drone_number = number of drones in the system<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;		3- init_point = center at the time the swarm members call a function<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;		4- altitude = height of swarm members<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;		5- rotation = angles of swarm members with respect to the main coordinate system<br/>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;--Description Of the Algorithm:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;		Step1 = The first point is passed to the variable point 1<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;		Step 2 = (drone_number)x3 unit matrix named desired_matrix  is created to generate the circle line. Where the rows represent UAVs. The 1st column represents the x-axis, the 2nd column represents the y-axis, and the 3rd column represents the z-axis.<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;		Step 3 = According to the radius value received and the number of UAVs, the positions to be reached in the while loop are calculated and transferred to the desired_matrix variable.<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;		Step4 = All of the specified coordinates are assigned to the desired_matrix variable and the transformed_matrix is created.<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;		Step5 = All coordinates are arranged according to the absolute frame with the transformation_2d function and transferred to the transformed_matrix.<br/>

