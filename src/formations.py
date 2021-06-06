from sub_functions import *

def set_triang_formation(distance,drone_number,init_point,altitude,rotation):
    desired_matrix = np.zeros((3,3))
    line1 = np.zeros((0,3))
    line2 = np.zeros((0,3))
    line3 = np.zeros((0,3))
    d = distance
    point_a = [0,d/m.sqrt(3),altitude]
    point_b = [-d*m.sin(m.pi/6),-d*m.cos(m.pi/6)+d/m.sqrt(3),altitude]
    point_c = [d*m.sin(m.pi/6),-d*m.cos(m.pi/6)+d/m.sqrt(3),altitude]
    desired_matrix[0] = np.array(point_a)
    desired_matrix[1] = np.array(point_b)
    desired_matrix[2] = np.array(point_c)
  
    i=3
    while i<drone_number:
        if(i%3==0):
            line1 = re_construct_line(point_a, point_b, len(line1), altitude)
        elif(i%3==1):
            line2 = re_construct_line(point_b, point_c, len(line2), altitude)
        elif(i%3==2):
            line3 = re_construct_line(point_c, point_a, len(line3), altitude)
        i+=1

    
    desired_matrix = np.concatenate((desired_matrix,line1,line2,line3))
    
    transformed_matrix = np.zeros( (drone_number,3) )
    droneIndex=0
    while(droneIndex < drone_number):
        transformed_matrix[droneIndex] = transformation_2d(desired_matrix[droneIndex], rotation, init_point,altitude)  
        transformed_matrix[droneIndex][2] = altitude
        droneIndex+=1
    
    return transformed_matrix
    
#print(set_triang_formation(5, 5,[1,1,5],3))


def set_square_formation(distance, drone_number, init_point,altitude,rotation):
    desired_matrix = np.zeros((4, 3))
    line1 = np.zeros((0,3))
    line2 = np.zeros((0,3))
    line3 = np.zeros((0,3))
    line4 = np.zeros((0,3))
    d = distance/2
    point_a = [-d, d, altitude]
    point_b = [d, d, altitude]
    point_c = [d ,-d, altitude]
    point_d = [-d ,-d, altitude]
    desired_matrix[0] = np.array(point_a)
    desired_matrix[1] = np.array(point_b)
    desired_matrix[2] = np.array(point_c)
    desired_matrix[3] = np.array(point_d)

    i = 4
    while i < drone_number:
        if (i % 4 == 0):
            line1 = re_construct_line(point_a, point_b, len(line1), altitude)
        elif (i % 4 == 1):
            line2 = re_construct_line(point_b, point_c, len(line2), altitude)
        elif (i % 4 == 2):
            line3 = re_construct_line(point_c, point_d, len(line3), altitude)
        elif(i%4 == 3):
            line4 = re_construct_line(point_d, point_a, len(line4), altitude)
        i += 1
    
    desired_matrix = np.concatenate((desired_matrix,line1,line2,line3,line4))
    transformed_matrix = np.zeros( (drone_number,3) )
    droneIndex=0
    while(droneIndex < drone_number):
        transformed_matrix[droneIndex] = transformation_2d(desired_matrix[droneIndex], rotation, init_point,altitude)  
        transformed_matrix[droneIndex][2] = altitude
        droneIndex+=1
    
    return transformed_matrix
    
#print(set_square_formation(12, 4,[0,0,0], 3))

def set_v_formation(distance,yaw_angle,drone_number,init_point,altitude,rotation):
    desired_matrix = np.zeros( (drone_number,3) )
    relative_origin = np.array([0,0,altitude])
    desired_matrix[0] = relative_origin
    droneIndex=1
    layer=1
    while(droneIndex<=drone_number-1):
        desired_matrix[droneIndex] = np.array([relative_origin[0] + (m.sin(yaw_angle/2)*distance*layer ) , relative_origin[1] - m.cos(yaw_angle/2)*distance*layer , altitude])
        if(drone_number%2 == 0 and droneIndex==drone_number-1):
            break
        droneIndex+=1
        desired_matrix[droneIndex] = np.array([relative_origin[0]-(m.sin(yaw_angle/2)*distance*layer ) , relative_origin[1] - m.cos(yaw_angle/2)*distance*layer , altitude])
        droneIndex+=1
        layer+=1
    
    transformed_matrix = np.zeros( (drone_number,3) )
    droneIndex=0
    while(droneIndex < drone_number):
        transformed_matrix[droneIndex] = transformation_2d(desired_matrix[droneIndex], rotation, init_point,altitude)  
        transformed_matrix[droneIndex][2] = altitude
        droneIndex+=1
    
    return transformed_matrix

#print("v form call")

def set_pentagon_formation(distance,drone_number,init_point,altitude,rotation):
    desired_matrix = np.zeros((5,3))
    line1 = np.zeros((0,3))
    line2 = np.zeros((0,3))
    line3 = np.zeros((0,3))
    line4 = np.zeros((0,3))
    line5 = np.zeros((0,3))
    d = distance

    point_a = [0,d*0.85,altitude]
    point_b = [-d*m.sin(m.pi/3.333),-d*m.cos(m.pi/3.333)+d*0.85,altitude]
    point_c = [-((m.sqrt(5)*d+d)/2)*m.sin(m.pi/10),-((m.sqrt(5)*d+d)/2)*m.cos(m.pi/10)+d*0.85,altitude]
    point_d = [((m.sqrt(5)*d+d)/2)*m.sin(m.pi/10),-((m.sqrt(5)*d+d)/2)*m.cos(m.pi/10)+d*0.85,altitude]
    point_e = [d*m.sin(m.pi/3.333),-d*m.cos(m.pi/3.333)+d*0.85,altitude]
    
    desired_matrix[0] = np.array(point_a)
    desired_matrix[1] = np.array(point_b)
    desired_matrix[2] = np.array(point_c)
    desired_matrix[3] = np.array(point_d)
    desired_matrix[4] = np.array(point_e)
  
    i=5
    while i<drone_number:
        if(i%5==0):
            line1 = re_construct_line(point_a, point_b, len(line1), altitude)
        elif(i%5==1):
            line2 = re_construct_line(point_b, point_c, len(line2), altitude)
        elif(i%5==2):
            line3 = re_construct_line(point_c, point_d, len(line3), altitude)
        elif(i%5==3):
            line4 = re_construct_line(point_d, point_e, len(line4), altitude)
        elif(i%5==4):
            line5 = re_construct_line(point_e, point_a, len(line5), altitude)
        i+=1

    
    desired_matrix = np.concatenate((desired_matrix,line1,line2,line3,line4,line5))
    
    transformed_matrix = np.zeros( (drone_number,3) )
    droneIndex=0
    while(droneIndex < drone_number):
        transformed_matrix[droneIndex] = transformation_2d(desired_matrix[droneIndex], rotation, init_point,altitude)  
        transformed_matrix[droneIndex][2] = altitude
        droneIndex+=1
    
    return transformed_matrix
    
def set_star_formation(distance,drone_number,init_point,altitude,rotation):
    desired_matrix = np.zeros((10,3))
    line1 = np.zeros((0,3))
    line2 = np.zeros((0,3))
    line3 = np.zeros((0,3))
    line4 = np.zeros((0,3))
    line5 = np.zeros((0,3))
    line6 = np.zeros((0,3))
    line7 = np.zeros((0,3))
    line8 = np.zeros((0,3))
    line9 = np.zeros((0,3))
    line10 = np.zeros((0,3))
    d = distance

    point_a = [0,d*0.526,altitude]
    point_b = [d*0.526*m.sin(m.pi/(180/72)),d*0.526*m.cos(m.pi/(180/72)),altitude]
    point_c = [d*0.526*m.cos(m.pi/(180/54)),-d*0.526*m.sin(m.pi/(180/54)),altitude]
    point_d = [-d*0.526*m.cos(m.pi/(180/54)),-d*0.526*m.sin(m.pi/(180/54)),altitude]
    point_e = [-d*0.526*m.cos(m.pi/(180/18)),d*0.526*m.sin(m.pi/(180/18)),altitude]

    point_f = [0,-d*1.376,altitude]
    point_g = [-d*1.376*m.sin(m.pi/(180/72)),-d*1.376*m.cos(m.pi/(180/72)),altitude]
    point_h = [-d*1.376*m.cos(m.pi/(180/54)),d*1.376*m.sin(m.pi/(180/54)),altitude]
    point_y = [d*1.376*m.cos(m.pi/(180/54)),d*1.376*m.sin(m.pi/(180/54)),altitude]
    point_z = [d*1.376*m.cos(m.pi/(180/18)),-d*1.376*m.sin(m.pi/(180/18)),altitude]
    
    desired_matrix[0] = np.array(point_a)
    desired_matrix[1] = np.array(point_b)
    desired_matrix[2] = np.array(point_c)
    desired_matrix[3] = np.array(point_d)
    desired_matrix[4] = np.array(point_e)

    desired_matrix[5] = np.array(point_f)
    desired_matrix[6] = np.array(point_g)
    desired_matrix[7] = np.array(point_h)
    desired_matrix[8] = np.array(point_z)
    desired_matrix[9] = np.array(point_y)

    i=10
    while i<drone_number:
        if(i%10==0):
            line1 = re_construct_line(point_a, point_h, len(line1), altitude)
        elif(i%10==1):
            line2 = re_construct_line(point_h, point_b, len(line2), altitude)
        elif(i%10==2):
            line3 = re_construct_line(point_b, point_g, len(line3), altitude)
        elif(i%10==3):
            line4 = re_construct_line(point_g, point_c, len(line4), altitude)
        elif(i%10==4):
            line5 = re_construct_line(point_c, point_f, len(line5), altitude)
        elif(i%10==5):
            line6 = re_construct_line(point_f, point_d, len(line6), altitude)
        elif(i%10==6):
            line7 = re_construct_line(point_d, point_y, len(line7), altitude)
        elif(i%10==7):
            line8 = re_construct_line(point_y, point_e, len(line8), altitude)
        elif(i%10==8):
            line9 = re_construct_line(point_e, point_z, len(line9), altitude)
        elif(i%10==9):
            line10 = re_construct_line(point_z, point_a, len(line10), altitude)
        i+=1


        desired_matrix = np.concatenate((desired_matrix,line1,line2,line3,line4,line5,line6,line7,line8,line9,line10))
    
    transformed_matrix = np.zeros( (drone_number,3) )
    droneIndex=0
    while(droneIndex < drone_number):
        transformed_matrix[droneIndex] = transformation_2d(desired_matrix[droneIndex], rotation, init_point,altitude)  
        transformed_matrix[droneIndex][2] = altitude
        droneIndex+=1
    
    return transformed_matrix

def set_crescent_formation(radius,gap_angle,drone_number,init_point,altitude,rotation):
    center_point=np.array([0,0,0])
    point1 = np.array([radius*m.cos(gap_angle/2),radius*m.sin(gap_angle/2),altitude])
    point2 = np.array([radius*m.cos(gap_angle/2),radius*m.sin(-gap_angle/2),altitude])

    desired_matrix = np.zeros((drone_number,3))
    desired_matrix[0] = point1
    desired_matrix[1] = point2 
    
    i=0
    while i<drone_number-2:
       desired_angle = (i+1)*((m.pi*2-gap_angle)/(drone_number-1)) + gap_angle/2
       desired_point = [radius*m.cos(desired_angle),radius*m.sin(desired_angle),altitude]
       desired_matrix[i+2] = desired_point
       i+=1
    transformed_matrix = np.zeros( (drone_number,3) )
    droneIndex=0
    while(droneIndex < drone_number):
        transformed_matrix[droneIndex] = transformation_2d(desired_matrix[droneIndex], rotation, init_point,altitude)  
        transformed_matrix[droneIndex][2] = altitude
        droneIndex+=1
    
    return transformed_matrix

def set_circle_formation(radius,drone_number,init_point,altitude,rotation):
    center_point=np.array([0,0,altitude])
    point1 = np.array([radius,0,altitude])    
    desired_matrix = np.zeros((drone_number,3))
    desired_matrix[0] = point1
    i=0
    while i<drone_number-1:
       desired_angle = (i+1)*((m.pi*2/(drone_number))) 
       desired_point = [radius*m.cos(desired_angle),radius*m.sin(desired_angle),altitude]
       desired_matrix[i+1] = desired_point
       i+=1
    
    transformed_matrix = np.zeros( (drone_number,3) )
    droneIndex=0
    while(droneIndex < drone_number):
        transformed_matrix[droneIndex] = transformation_2d(desired_matrix[droneIndex], rotation, init_point,altitude)  
        transformed_matrix[droneIndex][2] = altitude
        transformed_matrix[droneIndex][0] = transformed_matrix[droneIndex][0] - (init_point[0]*2)
        transformed_matrix[droneIndex][1] = transformed_matrix[droneIndex][1] - (init_point[1]*2)
        droneIndex+=1
    
    return transformed_matrix

print("dsf")
print(set_circle_formation(3,3,[3,3,0],3,0))