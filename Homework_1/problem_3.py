# name: YANGCHENG
# finish date: 1/18
# These codes are used to approximate the value of Pi

# This fuction is used to approximate the value of Pi by running different iterations times.
def get_pi(number_of_iterations):
    upper = 1
    bottom = 1
    Pi_div_fr = 0
    #using a for loop to ontrol the numbers of iterations.
    for i in range (1, int(number_of_iterations)+1):
        #calculate for odd iteration
        if i % 2 != 0:
            Pi_div_fr = Pi_div_fr + upper / bottom
            #calculate for even iteration
        else:
            Pi_div_fr = Pi_div_fr - upper / bottom
        #add 2 to bottom part of fraction after each iterations
        bottom += 2
    # times 4 to get the  Pi value
    sum = 4 * Pi_div_fr
    return sum


'''
get_pi(55)
Outputs looks like: 3.1597729697623063
'''


