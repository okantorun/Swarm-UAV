import numpy as np
from pycrazyswarm import *
from sub_functions import *
from formations import *
from swarm_class import *
import random




print("""
---- Çoban-Z Sürü Drone Algoritmaları Kumanda Modülü ----
---------------------------------------------------------
Dikkat !!  Her formasyon için minimum bir drone sayısı vardır 

Üçgen --> 3 
Kare --> 4 
V --> 5
Beşgen --> 5
Hilal --> 6
Yıldız --> 10

""")
    
drone_number = int(input("Lütfen kaç drone ile başlamak istediğinizi giriniz : "))
print("------------------------------------------------")
print("------------------------------------------------")
take_off_type = int(input("""Dronların eşzamanlı kaldırılmasını istiyorsanız --> 1 
Teker teker kalkmalarını istiyorsanız --> 2 : 
"""))
hight = float(input("kaç metre yüksekliğe çıkılsın :  "))
distance = float(input("elemanlar arasındaki mesafeyi giriniz :  "))

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
    print("hatalı giris yaptiniz")



if drone_number == 3:
    print("seçebileceğiniz formasyonlar : ")
    print("1 --> Üçgen ")
elif drone_number ==4 :
    print("seçebileceğiniz formasyonlar : ")
    print("1 --> Üçgen ")
    print("2 --> Kare ")
elif drone_number ==5 :
    print("seçebileceğiniz formasyonlar : ")
    print("1 --> Üçgen ")
    print("2 --> Kare ")
    print("3 --> V formasyonu ")
    print("4 --> Beşgen formasyonu ")
elif drone_number == 6 :
    print("seçebileceğiniz formasyonlar : ")
    print("1 --> Üçgen ")
    print("2 --> Kare ")
    print("3 --> V formasyonu ")
    print("4 --> Beşgen formasyonu ")
    print("5 --> Hilal formasyonu ")
    
elif drone_number > 6 :
    print("seçebileceğiniz formasyonlar : ")
    print("1 --> Üçgen ")
    print("2 --> Kare ")
    print("3 --> V formasyonu ")
    print("4 --> Beşgen formasyonu ")
    print("5 --> Hilal formasyonu ")
    print("6 --> Yıldız fprmasyonu")

    
formation_id = int(input("formasyon numarasını giriniz : "))


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
    print("""Formasyonu güncellemek için --> 1
Yükselme veya Alçalma için --> 2  
Rotasyon yaptırmak için  --> 3
Navigasyon yaptırmak için --> 4
Sürü ayrılması için  --> 5
Dönerek Navigasyon için --> 6
Sıralı iniş için --> 7
""")
    selection = int(input("seçiminiz : "))
    if selection == 1 :
        print(""" eleman eklemek için --> 1
        eleman çıkarmak için --> 2
        elamanlar arası mesafeyi güncellemek için --> 3
        formasyon değiştirmek için --> 4
        kare formasyonundayken eleman ekleme için --> 5
        """)
        selection2 = int(input("seçiminiz : "))

        if selection2 == 1 :
            swarm2.add_crazyflie(allcfs.crazyflies[drone_number])
            timeHelper.sleep(5)
            drone_number +=1
            swarm2.take_formation(distance,formation_id,hight,cur_x,cur_y)
        elif selection2 == 2 :
            rastgele = random.randint(0,drone_number-1)
            print("rastgele eleman çıkarılıyor ...")
            swarm2.remove_crazyflie(swarm2.crazyflies[rastgele])
            drone_number = drone_number -1 
            swarm2.take_formation(distance,formation_id,hight,cur_x,cur_y)
        elif selection2 == 3 :
            aralık = int(input("elemanlar arasındaki istediğiniz mesafeyi giriniz : "))
            distance = aralık
            swarm2.take_formation(aralık,formation_id,hight,cur_x,cur_y)
        elif selection2 == 4 :
            print("seçebileceğiniz formasyonlar : ")
            print("1 --> Üçgen ")
            print("2 --> Kare ")
            print("3 --> V formasyonu ")
            print("4 --> Beşgen formasyonu ")
            print("5 --> Hilal formasyonu ")
            print("6 --> Yıldız formasyonu")
            print("7 --> Daire formasyonu")

            selection3 = int(input("seçiminiz : "))
            formation_id = selection3
            swarm2.change_formation(selection3,distance,cur_x,cur_y)
            
    elif selection  == 2 :
        vertical_move = float(input("Sürüyü hangi yüksekliğe hareket ettirmek istersiniz : "))
        swarm2.takeoff_ascyn(vertical_move, 5)
        hight = vertical_move    

    elif selection  == 3 :
        rot = int(input("kac derece rotasyon yaptırmak istiyorsunuz : "))
        print(cur_x)
        print(cur_y)
        swarm2.rotasyon_3(rot,cur_x, cur_y, hight,distance)
        

    elif selection  == 4 :
        x = float(input("navigasyon yapmak istediğiniz noktanın x kordinatını giriniz : " ))
        y = float(input("navigasyon yapmak istediğiniz noktanın y kordinatını giriniz : " ))
        swarm2.navigation_2([x,y,hight],10)
        cur_x = x 
        cur_y = y
        
    elif selection  == 5 :
        print("sürü ayrılması yapmak için minimum 6 iha bulunmalıdır ")
        if drone_number > 5 :
            print("test için  bir üçgen ve istediğimiz başka bir formasyon :  ")
            sep_swarm = int(input("lütfen istediğiniz diğer formasyonu giriniz "))
            crazyflies_1 = allcfs.crazyflies[0:3]
            crazyflies_2= allcfs.crazyflies[3:drone_number]
            swarm_3,swarm_4 = swarm2.swarm_separate(crazyflies_1, crazyflies_2)
            swarm_3.takeoff_ascyn(hight+1, 10)
            swarm_4.takeoff_ascyn(hight-1, 10)
            swarm_3.take_formation(distance, 1, hight+1, 0, 0)
            swarm_4.take_formation(distance, sep_swarm, hight-1, 0, 0)
            swarm_3.navigation_2([-4,-4,hight+1], 10)
            swarm_4.navigation_2([4,4,hight-1], 10)

            print("tekrar birleşim yapılıyor....")
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



