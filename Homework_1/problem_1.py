# name: YANGCHENG
# finish date: 1/17
# To calculate the data of a sphere with radiu
#this fuction is used to calculat all the data of a circle by using the different fomulas of sphere with known radius
import math
def sphere(r):
    # the diameter of radius
    D = 2 * r
    #calculate circumference
    circum = 2 * math.pi * r
    # calculate the surface area of sphere
    surface = 4 * math.pi * r * r
    # calculate the volume of sphere
    V = 4/3 * math.pi * r * r * r
    #using a list to collect all the data
    result = [D, circum, surface, V]
    return result

'''
Outupt example:
sphere(13)
outputs looks like: [26, 81.68140899333463, 2123.7166338267, 9202.7720799157]
'''