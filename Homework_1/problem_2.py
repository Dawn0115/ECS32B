# A fuction used to calculate the distance a ball travel when it hits ground
# Author of code: YANGCHENG
# Completed date: 1/18

# This function is used to calculate when the ball drops, the distance it will travel.

def bounce(initial_height, index, number_of_bounce):
    H = initial_height
    Distance = initial_height
    #i used a for loop to add up different distance the ball travel after bounce.
    for i in range(number_of_bounce):
        height = H * index
        H = height
        # adding up each time the ball travels
        Distance = Distance + height * 2
    Distance = Distance - height
    return Distance
'''
bounce(10, 0.6, 3)
Outputs looks like: 31.359999999999996
'''
