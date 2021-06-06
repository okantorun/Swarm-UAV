import numpy as np
from scipy.optimize import linear_sum_assignment
import math as m


#theta angle is positive throught to CW.
def transformation_2d(relative_loc,theta,translation,Z):      
    relative_matrix = relative_loc
    relative_matrix[2] = Z
    relative_matrix = relative_matrix.transpose()
    rotation_matrix = np.array( [[m.cos(theta),-m.sin(theta),translation[0]] , [m.sin(theta),m.cos(theta),translation[1]],[0,0,1]]) 
    absolute_matrix = np.matmul(rotation_matrix,relative_matrix)
    return absolute_matrix

def inverse_transformation_2d(absolute_loc,theta,translation,Z):      
    absolute_matrix = absolute_loc
    absolute_matrix[2] = Z
    
    rotation_matrix = np.linalg.inv(np.array( [[m.cos(theta),-m.sin(theta),translation[0]] , [m.sin(theta),m.cos(theta),translation[1]],[0,0,1]])) 
    relative_matrix = np.matmul(rotation_matrix,absolute_matrix)
    
    return relative_matrix

mat = [[1,1,1],[1+m.sqrt(2),1+m.sqrt(2),1],[1+2*m.sqrt(2),1,1],[1+m.sqrt(2),1-m.sqrt(2),1]]
i=0
while i<4:
    print(inverse_transformation_2d(mat[i],m.pi/4,[1+m.sqrt(2),1,1], 1))
    i+=1
#dronların mevcut konumlarından, istenilen diğer konumlara minumum maaliyet ile
#gitmesini sağlayan fonskiyonlar.

def cost_for_move(current_loc,desired_loc):
    return m.sqrt(  pow(desired_loc[0]-current_loc[0],2)  + pow(desired_loc[1]-current_loc[1],2) + pow(desired_loc[2]-current_loc[2],2))

def hungarian_assigment(current_locs,desired_locs): #np array ver  
    cost_matrix = np.zeros(shape=(current_locs.shape[0],current_locs.shape[0]))
    i=0
    j=0
    while i < current_locs.shape[0]:
        while j < desired_locs.shape[0]:
            cost_matrix[i][j] = cost_for_move(current_locs[i],desired_locs[j])
            j+=1
        i+=1
        j=0

    row_ind,col_ind = linear_sum_assignment(cost_matrix)
    opt_ass = col_ind 
    drons_is_going = np.zeros((desired_locs.shape[0],desired_locs.shape[1])) 
    j=0
    print("current")
    print(current_locs)
    print("desired_locs")
    print(desired_locs)
    while j < current_locs.shape[0]:
        drons_is_going[j] = desired_locs[opt_ass[j]]
        j+=1
    return drons_is_going 


#a ve b noktaları arasında bir doğru olduğunu düşünelim:
#bu doğru üzerindeki eleman sayısı number_of_particle paremetresiyle alınır
#fonksiyon bize aynı doğru üzerinde number_of_particle+1 adet nokta bulunan 
#eşit aralıkların konumlarını verir.  1 boyutlu düşünecek olursak a=0 ,b =6
#ve number_of_particle=0 ise fonksiyon bize 3 noktasını verir . eğer number_of_particle=1
#ise 2 ve 4 noktalarını verir.
def re_construct_line(a_point, b_point, number_of_particle, altitude):
    points = np.zeros((number_of_particle + 1, 3))
    i = 0
    while i < number_of_particle + 1:
        j = i + 1
        points[i] = [a_point[0] + (j * ((b_point[0] - a_point[0]) / (number_of_particle + 2))),
                     a_point[1] + (j * ((b_point[1] - a_point[1]) / (number_of_particle + 2))), altitude]
        i += 1
    return points
#this for just symetric shapes this is not working exactly etc poligon
def calc_center(points):
    x = []
    y = []
    z = points[0][2]
    aralar = []
    edges = []
    i=0
    while i< len(points):
        x.append(points[i][0])
        y.append(points[i][1])
        i+=1
    maximum_x = max(x)
    minimum_x = min(x)
    maximum_y = max(y)
    minimum_y = min(y)
    i=0
    while i<len(points):
        if ((points[i][0]!= maximum_x and points[i][0]!= minimum_x) and (points[i][1]!= maximum_y and points[i][1]!=minimum_y)):
            aralar.append(points[i])
        else:
            edges.append(points[i])
        i+=1
    return [sum(x)/len(x),sum(y)/len(y),z]

def calc_center_3points(point1,point2,point3):
    # Initialize the lists for the abscissae and the ordinates
    x_l=[point1[0],point2[0],point3[0]]
    y_l=[point1[1],point2[1],point3[1]]
    nop = len(x_l)                          # number of points

    # Primary raw material
    x = np.array(x_l)                       #numpy array
    y = np.array(y_l)                       #numpy array

    x_y = np.multiply(x,y)                  #elementwise multiplication
    x_2 = np.square(x)                      #elementwise square
    y_2 = np.square(y)                      #elementwise square

    # Secondary raw material
    x_2_plus_y_2 = np.add(x_2,y_2)          #elementwise addition
    x__x_2_plus_y_2 = np.multiply(x,x_2_plus_y_2)   #elementwise multiplication
    y__x_2_plus_y_2 = np.multiply(y,x_2_plus_y_2)   #elementwise multiplication

    # Summations (by default the result of summation is integer)
    sum_x = x.sum(dtype=float)
    sum_y = y.sum(dtype=float)
    sum_x_2 = x_2.sum(dtype=float)
    sum_y_2 = y_2.sum(dtype=float)
    sum_x_y = x_y.sum(dtype=float)
    sum_x_2_plus_y_2 = x_2_plus_y_2.sum(dtype=float)
    sum_x__x_2_plus_y_2 = x__x_2_plus_y_2.sum(dtype=float)
    sum_y__x_2_plus_y_2 = y__x_2_plus_y_2.sum(dtype=float)

    # Comment the line below; don't delete. Use for debugging.
    # print sum_x,sum_y,sum_x_2,sum_y_2,sum_x_y,sum_x_2_plus_y_2,sum_x__x_2_plus_y_2,sum_y__x_2_plus_y_2

    m3b3 = np.array([[sum_x_2,sum_x_y,sum_x],
            [sum_x_y,sum_y_2,sum_y],
            [sum_x,sum_y,nop]])
    invm3b3 = np.linalg.inv(m3b3)
    m3b1 = np.array([sum_x__x_2_plus_y_2,sum_y__x_2_plus_y_2,sum_x_2_plus_y_2])
    A=np.dot(invm3b3,m3b1)[0]
    B=np.dot(invm3b3,m3b1)[1]
    C=np.dot(invm3b3,m3b1)[2]
    CenterX = A/2
    CenterY = B/2
    Radius = np.sqrt(4*C+A**2+B**2)/2
    return [CenterX,CenterY,Radius]
calc_center_3points([-1,0],[1,0],[m.cos(m.pi/3),m.sin(m.pi/3)])

