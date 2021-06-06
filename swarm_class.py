from pycrazyswarm import *
import numpy as np
from formations import *
from sub_functions import *

class Swarm :  
    def __init__(self,crazyflies,timeHelper,allcfs):
        self.crazyflies = crazyflies
        self.allcfs = allcfs
        self.numberOfCrazyflies = len(self.crazyflies)
        self.positions = []
        self.initial_positions = []
        self.init_pos(self.allcfs)
        self.formation_inventory = [set_triang_formation,set_square_formation,set_v_formation,set_pentagon_formation,set_crescent_formation,set_star_formation,set_circle_formation]
        self.formation =1
        self.rotation_angle = 0
        self.timeHelper = timeHelper
        self.sum_rot = 0

    def init_pos(self,allcfs):
        i=0
        while i<len(self.allcfs.crazyflies):
           self.initial_positions.append(allcfs.crazyflies[i].position())
           self.positions.append(allcfs.crazyflies[i].position()) 
           i+=1
        print(self.positions)

    def rotasyon_3(self,angle,x,y,Z,distance):

        radyan = angle*m.pi/180
        formation_number = self.formation
        print(x)
        print(y)
        print(Z)
        print(formation_number)
        #why /2  ?  this is from experiments
        if formation_number == 1:
            desired_locs = set_triang_formation(distance, self.numberOfCrazyflies,[x/2,y/2,Z], Z,radyan+self.sum_rot)
            
        elif formation_number == 2:
            desired_locs = set_square_formation(distance, self.numberOfCrazyflies,[x/2,y/2,Z], Z,radyan+self.sum_rot)
           
        elif formation_number == 4:
            desired_locs = set_pentagon_formation(distance, self.numberOfCrazyflies,[x/2,y/2,Z], Z,radyan+self.sum_rot)
            
        elif formation_number == 3:
            desired_locs = set_v_formation(distance,m.pi/3 ,self.numberOfCrazyflies,[x/2,y/2,Z], Z,radyan+self.sum_rot)
            
        elif formation_number == 5:
            desired_locs = set_crescent_formation(distance, 2*m.pi/3,self.numberOfCrazyflies,[x/2,y/2,Z], Z,radyan+self.sum_rot)

        elif formation_number == 6:
            desired_locs = set_star_formation(distance,self.numberOfCrazyflies,[x/2,y/2,Z], Z,radyan+self.sum_rot)
        elif formation_number == 7:
            desired_locs = set_circle_formation(distance,self.numberOfCrazyflies,[x/2,y/2,Z], Z,radyan+self.sum_rot)

     
        self.update(self.crazyflies)    
        self.sum_rot +=radyan 
        self.go(desired_locs,10)
    
    def change_formation(self,new_formation,distance,x,y):
        self.formation = new_formation
        self.update(self.crazyflies)
        if new_formation == 1 :
            self.take_formation(distance,1,self.crazyflies[0].position()[2],x,y)
        if new_formation == 2 :
            self.take_formation(distance,2,self.crazyflies[0].position()[2],x,y)
        if new_formation == 3 :
            self.take_formation(distance,3,self.crazyflies[0].position()[2],x,y)
        if new_formation == 4 :
            self.take_formation(distance,4,self.crazyflies[0].position()[2],x,y)
        if new_formation == 5 :
            self.take_formation(distance,5,self.crazyflies[0].position()[2],x,y)
        if new_formation == 6 :
            self.take_formation(distance,6,self.crazyflies[0].position()[2],x,y)
        if new_formation == 7 :
            self.take_formation(distance,7,self.crazyflies[0].position()[2],x,y)

        self.update(self.crazyflies)    
    
    def takeoff_scyn(self,Z,duration):
        i=0
        while i<self.numberOfCrazyflies:
            self.crazyflies[i].takeoff(0, 0)
            self.crazyflies[i].goTo([self.crazyflies[i].position()[0],self.crazyflies[i].position()[1],Z],0,duration)
            i+=1
            self.timeHelper.sleep(duration)
        self.update(self.crazyflies)

    def takeoff_ascyn(self,Z,duration):
        i=0
        while i<self.numberOfCrazyflies:
            self.crazyflies[i].takeoff(0, 0)
            self.crazyflies[i].goTo([self.crazyflies[i].position()[0],self.crazyflies[i].position()[1],Z],0,duration)
            i+=1
        self.timeHelper.sleep(duration)
        self.update(self.crazyflies)

    
    def take_formation(self,distance,formation_number,Z,x,y):
        if formation_number == 1:
            desired_locs = set_triang_formation(distance, self.numberOfCrazyflies,[x,y,Z], Z,self.sum_rot)
            i=0
            while i < self.numberOfCrazyflies:
                self.crazyflies[i].goTo(desired_locs[i],0,10)
                i+=1
            self.timeHelper.sleep(10)   
            self.update(self.crazyflies)
            self.formation = 1
        elif formation_number == 2:
            desired_locs = set_square_formation(distance, self.numberOfCrazyflies,[x,y,Z], Z,self.sum_rot)
            i=0
            while i < self.numberOfCrazyflies:
                self.crazyflies[i].goTo(desired_locs[i],0,10)
                i+=1
            self.timeHelper.sleep(10)   
            self.update(self.crazyflies)
            self.formation = 2
        elif formation_number == 4:
            desired_locs = set_pentagon_formation(distance, self.numberOfCrazyflies,[x,y,Z], Z,self.sum_rot)
            i=0
            while i < self.numberOfCrazyflies:
                self.crazyflies[i].goTo(desired_locs[i],0,10)
                i+=1
            self.timeHelper.sleep(10)   
            self.update(self.crazyflies)
            self.formation = 4
        elif formation_number == 3:
            desired_locs = set_v_formation(distance,m.pi/3 ,self.numberOfCrazyflies,[x,y,Z], Z,self.sum_rot)
            i=0
            while i < self.numberOfCrazyflies:
                self.crazyflies[i].goTo(desired_locs[i],0,10)
                i+=1
            self.timeHelper.sleep(10)   
            self.update(self.crazyflies)
            self.formation = 3
        elif formation_number == 5:
            desired_locs = set_crescent_formation(distance, 2*m.pi/3,self.numberOfCrazyflies,[x,y,Z], Z,self.sum_rot)
            i=0
            while i < self.numberOfCrazyflies:
                self.crazyflies[i].goTo(desired_locs[i],0,10)
                i+=1
            self.timeHelper.sleep(10)   
            self.update(self.crazyflies)
            self.formation = 5
        elif formation_number == 6:
            desired_locs = set_star_formation(distance,self.numberOfCrazyflies,[x,y,Z], Z,self.sum_rot)
            i=0
            while i < self.numberOfCrazyflies:
                self.crazyflies[i].goTo(desired_locs[i],0,10)
                i+=1
            self.timeHelper.sleep(10)   
            self.update(self.crazyflies)
            self.formation = 6

        elif formation_number == 7:
            desired_locs = set_circle_formation(distance,self.numberOfCrazyflies,[x,y,Z], Z,self.sum_rot)
            i=0
            while i < self.numberOfCrazyflies:
                self.crazyflies[i].goTo(desired_locs[i],0,10)
                i+=1
            self.timeHelper.sleep(10)   
            self.update(self.crazyflies)
            self.formation = 7

    def go(self,coordinats,duration):
        self.update(self.crazyflies)
        i=0
        while i<self.numberOfCrazyflies:
            self.crazyflies[i].goTo(coordinats[i],0,duration)
            i+=1 

        self.timeHelper.sleep(duration)
        self.update(self.crazyflies)
    def go_center(self,coordinats,duration):
        i=0
        self.update(self.crazyflies)
        
        while i<self.numberOfCrazyflies:
            self.crazyflies[i].goTo(coordinats,0,duration,True)
            i+=1 

        self.timeHelper.sleep(duration)
        self.update(self.crazyflies)

    def add_crazyflie(self,crazyflie):
        self.crazyflies = self.allcfs.crazyflies[0:self.numberOfCrazyflies+1]
        self.update(self.crazyflies)
        
    
    def remove_crazyflie(self,crazyflie):
        self.crazyflies.remove(crazyflie)
        self.update(self.crazyflies)
        crazyflie.goTo([0,0,0], 0, 5)   
        self.timeHelper.sleep(5)
        self.update(self.crazyflies)
    
    def navigation(self,points):
        self.update(self.crazyflies)
        cur_poss = np.array(self.positions)
        cur_poss = cur_poss[0:self.numberOfCrazyflies]
        self.update(self.crazyflies)
        if self.formation == 3 or self.formation == 5 :
            des_poss = self.formation_inventory[self.formation-1](0.5,m.pi/3, len(self.crazyflies),points,3,self.rotation_angle)
        else:
            des_poss = self.formation_inventory[self.formation-1](3, len(self.crazyflies), points,3,self.rotation_angle)
        target = hungarian_assigment(cur_poss, des_poss)
        self.go(target, 20)
        
    def navigation_2(self,point,duration):
        self.update(self.crazyflies)
        cur_poss = np.array(self.positions)
        cur_poss = cur_poss[0:self.numberOfCrazyflies]
        center = calc_center(cur_poss)
        target_vector = [point[0]-center[0],point[1]-center[1],point[2]-center[2]]
        if self.formation == 5:
            x,y,rad = calc_center_3points(self.positions[0],self.positions[1],self.positions[2])
            target_vector = [point[0]-x,point[1]-y,point[2]-center[2]]
        self.go_center(target_vector, duration)
        self.update(self.crazyflies)


    def swarm_separate(self,crazyflies_1,crazyflies_2):
        swarm_1 = Swarm(crazyflies_1, self.timeHelper,self.allcfs)
        swarm_2 = Swarm(crazyflies_2, self.timeHelper,self.allcfs)
        return [swarm_1,swarm_2]

    def swarm_join(self,crazyflies):
        return Swarm(crazyflies, self.timeHelper, self.allcfs)

    def get_positions(self):
        return self.positions

    def set_inventory():
        pass

    def update(self,crazyflies):
        self.crazyflies = crazyflies
        self.numberOfCrazyflies = len(self.crazyflies)
        i=0
        while i<self.numberOfCrazyflies:
            self.initial_positions[i] = self.crazyflies[i].initialPosition
            self.positions[i] = self.crazyflies[i].position()
            i+=1

