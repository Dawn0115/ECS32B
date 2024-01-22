import math
import sys
#avoid recursive error
sys.setrecursionlimit(10**6)
#n is the recursive time to evaluate pi
def approximate_pi(n, a=math.sqrt(2), b=0):
    #if n reach 0, return the result
    if n == 0:
        return 2 / a
    else:

        b = math.sqrt(2 + b)
        a *= b / 2
        PI = 2 / a
        #check if the difference between result and real pi is small enough
        if abs(math.pi - PI) < 0.000000005:
            return PI
        else:
            #recursive to run this function
            return approximate_pi(n - 1, a, b)

# Example usage:
PI = approximate_pi(1000)
#round to 8 decimal of the pi value
print(round(PI, 8))

