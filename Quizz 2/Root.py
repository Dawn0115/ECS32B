import cmath
import math
#a,b,c is the coefficience of x**2, x and constant
def quadratic(a, b, c):
    # Compute the discriminant by formula
    dis = b**2 - 4*a*c

    # determince the different value of discriminant 


    # two roots of this quadratice is real and equal

    if dis == 0:
        root1 = root2 = -b / (2*a)
        print('two real and equal roots: ', root1)
    # two real but unequal root
    elif dis > 0:
        # get each root's value by math formula
        root1 = (-b + math.sqrt(dis)) / (2*a)
        root2 = (-b - math.sqrt(dis)) / (2*a)
        print('two unequal root:', f'root 1 is{root1}', f'root 2 is{root2}')
    # if discriminant is less than 0, the quadratic has complex roots
    else:
        root1 = (-b + cmath.sqrt(dis)) / (2*a)
        root2 = (-b - cmath.sqrt(dis)) / (2*a)
        print("complex roots: ", root1, " and ", root2)

quadratic(1, 2, 1)
quadratic(1, 6, 7)
quadratic(1, 2, 5)


'''
Output looks like 
two real and equal roots: -1.0
two unequal root: root 1 is-1.5857864376269049 root 2 is-4.414213562373095
complex roots:  (-1+2j)  and  (-1-2j)
'''
