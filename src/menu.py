import numpy as np
from pycrazyswarm import *
from sub_functions import *
from formations import *
from swarm_class import *
import random




print("""
---- Çoban-Z Swarm Drone Algorithms Control Module ----
---------------------------------------------------------
Attention !! There is a minimum number of drones for each formation

Triangle --> 3 
Square --> 4 
V --> 5
Pentagon --> 5
Crescent --> 6
Star --> 10

""")
    
drone_number = int(input("Please enter how many drones you want to start with : "))
print("------------------------------------------------")
print("------------------------------------------------")
take_off_type = int(input("""If you want simultaneous take off of drones --> 1 
Teker teker kalkmalarını istiyorsanız --> 2 : 
"""))
hight = float(input("how many meters high?:  "))
distance = float(input("enter the distance between elements :  "))

swarm = Crazyswarm()
timeHelper = swarm.timeHelper
allcfs = swarm.allcfs
swarm.allcfs.takeoff(0,0)
crazyflies = allcfs.crazyflies[0:drone_number]
swarm2 = Swarm(crazyflies,timeHelper,allcfs)

if take_off_type == 1 :
    swarm2.takeoff_ascyn(hight, 5)
elif take_off_type == 2:
    swarm2.takeoff_scyn(hight, 5)
else :
    print("you entered wrong")



if drone_number == 3:
    print("formations to choose from : ")
    print("1 --> Triangle ")
elif drone_number ==4 :
    print("formations to choose from : ")
    print("1 --> Triangle ")
    print("2 --> Square ")
elif drone_number ==5 :
    print("formations to choose from : ")
    print("1 --> Triangle ")
    print("2 --> Square ")
    print("3 --> V formation ")
    print("4 --> Pentagon formation ")
elif drone_number == 6 :
    print("formations to choose from : ")
    print("1 --> Triangle ")
    print("2 --> Square ")
    print("3 --> V formation ")
    print("4 --> Pentagon formation ")
    print("5 --> Crescent formation ")
    
elif drone_number > 6 :
    print("formations to choose from : ")
    print("1 --> Triangle ")
    print("2 --> Square ")
    print("3 --> V formation ")
    print("4 --> Pentagon formation ")
    print("5 --> Crescent formation ")
    print("6 --> Star formation")

    
formation_id = int(input("enter formation number : "))


if formation_id == 1:
    swarm2.take_formation(distance,formation_id,hight,0,0)
elif formation_id == 2:
    swarm2.take_formation(distance,formation_id,hight,0,0)
elif formation_id == 3:
    swarm2.take_formation(distance,formation_id,hight,0,0)
elif formation_id == 4:
    swarm2.take_formation(distance,formation_id,hight,0,0)
elif formation_id == 5:
    swarm2.take_formation(distance,formation_id,hight,0,0)
elif formation_id == 6:
    swarm2.take_formation(distance,formation_id,hight,0,0)
elif formation_id == 7:
    swarm2.take_formation(distance,formation_id,hight,0,0)

cur_x = 0
cur_y = 0

while True :
    print("""To update the formation --> 1
For Ascension or Descent --> 2  
For  rotation  --> 3
For navigation --> 4
For swarm separation  --> 5
For Turning Navigation --> 6
For sequential landing --> 7
""")
    selection = int(input("Selection : "))
    if selection == 1 :
        print(""" to add an element --> 1
        to remove element --> 2
        to update the distance between elements --> 3
        to change formation --> 4
        for adding elements while in square formation --> 5
        """)
        selection2 = int(input("Selection : "))

        if selection2 == 1 :
            swarm2.add_crazyflie(allcfs.crazyflies[drone_number])
            timeHelper.sleep(5)
            drone_number +=1
            swarm2.take_formation(distance,formation_id,hight,cur_x,cur_y)
        elif selection2 == 2 :
            rastgele = random.randint(0,drone_number-1)
            print("randomly removing element ...")
            swarm2.remove_crazyflie(swarm2.crazyflies[rastgele])
            drone_number = drone_number -1 
            swarm2.take_formation(distance,formation_id,hight,cur_x,cur_y)
        elif selection2 == 3 :
            aralık = int(input("Enter the distance you want between the elements : "))
            distance = aralık
            swarm2.take_formation(aralık,formation_id,hight,cur_x,cur_y)
        elif selection2 == 4 :
            print("formations to choose from : ")
            print("1 --> Triangle ")
            print("2 --> Square ")
            print("3 --> V formation ")
            print("4 --> Pentagon formation ")
            print("5 --> Crescent formation ")
            print("6 --> Star formation")
            print("7 --> Circle formation")

            selection3 = int(input("Selection : "))
            formation_id = selection3
            swarm2.change_formation(selection3,distance,cur_x,cur_y)
            
    elif selection  == 2 :
        vertical_move = float(input("To what height do you want to move the Swarm : "))
        swarm2.takeoff_ascyn(vertical_move, 5)
        hight = vertical_move    

    elif selection  == 3 :
        rot = int(input("How many degrees do you want to rotate? : "))
        print(cur_x)
        print(cur_y)
        swarm2.rotasyon_3(rot,cur_x, cur_y, hight,distance)
        

    elif selection  == 4 :
        x = float(input("Enter the x coordinate of the point you want to navigate : " ))
        y = float(input("Enter the y-coordinate of the point you want to navigate : " ))
        swarm2.navigation_2([x,y,hight],10)
        cur_x = x 
        cur_y = y
        
    elif selection  == 5 :
        print("There must be a minimum of 6 UAVs to make a swarm separation ")
        if drone_number > 5 :
            print("A triangle for testing and another pattern we want :  ")
            sep_swarm = int(input("Please enter the other formation you want "))
            crazyflies_1 = allcfs.crazyflies[0:3]
            crazyflies_2= allcfs.crazyflies[3:drone_number]
            swarm_3,swarm_4 = swarm2.swarm_separate(crazyflies_1, crazyflies_2)
            swarm_3.takeoff_ascyn(hight+1, 10)
            swarm_4.takeoff_ascyn(hight-1, 10)
            swarm_3.take_formation(distance, 1, hight+1, 0, 0)
            swarm_4.take_formation(distance, sep_swarm, hight-1, 0, 0)
            swarm_3.navigation_2([-4,-4,hight+1], 10)
            swarm_4.navigation_2([4,4,hight-1], 10)

            print("Reunification is taking place....")
            timeHelper.sleep(10)
            swarm2.take_formation(distance,sep_swarm, hight, 0, 0)
    #not working like expected
    elif selection == 6 :
        point_x = float(input("x : "))
        point_y = float(input("y : "))
        angle = m.atan((point_y-cur_y)/(point_x-cur_x))
        angle = -angle*180/m.pi
        swarm2.rotasyon_3(swarm2.sum_rot+angle, cur_x, cur_y, hight, distance)
        swarm2.navigation_2([point_x,point_y,hight], 10)
        cur_x = point_x
        cur_y = point_y
    elif selection == 7:
        swarm2.takeoff_scyn(0, 5)
        hight = 0
        


timeHelper.sleep(10)

swarm2.change_formation(1)


timeHelper.sleep(10)



