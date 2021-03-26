'''
This code returns a skyline contour from a give list of buildings. 
The input list contains Ri, Li, and Hi from every bulding and the output list
has the xi,yi coordinates that describe the skyline contour. 

Author:
Adrian Viveros Lúques. 
03.26.2021
'''
import os

if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')

def getSkyline(buildings):
    #This function returns a list with the coordinates of the skyline contour
    #Output: [[x1,y1],[x2,y2]....[xn,yn]]
    skyline = []
    n = len(buildings)
    if not buildings:
        return skyline
 
    skyline.append([buildings[0][0], buildings[0][2]])      #Insert the first building coordinates in the skyline output with height 0
    
    for i in range(1,n):
        diff = buildings[i][0] - buildings[i-1][1]
        
        if(diff <1):
            if(buildings[i][2] > buildings[i-1][2]):
                skyline.append([buildings[i][0], buildings[i][2]])
            elif(buildings[i][2] < buildings[i-1][2]):
                skyline.append([buildings[i-1][1],buildings[i][2]])
        else:
            #create the union when the buildings are not "wall-to-wall"
            skyline.append([buildings[i-1][1],0])
            skyline.append([buildings[i][0], buildings[i][2]])

    skyline.append([buildings[n-1][1],0])  #Insert the last bulding coordinate in the skyline output with height 0
    
    return skyline  


#List of buildings where each element is a building, with its coordinates
#[left x, right x, height y]
buildings = [[2,9,10],[3,6,15],[5,12,12],[13,16,10],[15,17,5]]
print(getSkyline(buildings)) #Expected Output [[2, 10], [3, 15], [6, 12], [12, 0], [13, 10], [16, 5], [17,0]]



