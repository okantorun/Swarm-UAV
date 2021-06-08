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
