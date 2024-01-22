def expo(base, exponent):
    ini = base
    # determine whether the exponenter is negative number
    if exponent < 0:
        #if the exponent is a negative number, then return an error to function
        return ValueError
    else:
        #use a for loop to do a power executing
        for i in range(exponent-1):
            result = ini * base
            ini = result
    return result 

'''
print(expo(2,-1))
Output:<'Value Error'>

print(expo(2,3))
Output: 8

print(expo(3,3))
Output: 27

'''

'''
the computational complexity depends on the number of exponent, assume n is exponent, Big O notation is O(n)

'''

