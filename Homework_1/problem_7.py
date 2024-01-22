# name: YANGCHENG
# finish date: 1/19
# this duction is used to find the greatest common divisior of two numbers.
def recursive_gcd(first_integer, second_integer):
    # compare which number is larger. And convert to correct order.
    if first_integer < second_integer:
        fst = second_integer
        sec = first_integer
    else:
        fst = first_integer
        sec =second_integer
        # when the smaller number becomes zero, exit this function and retrun the result.
    if sec == 0:
        return fst
    else:
        # use recursion to keep serching the GCD of these two numbers.
        return recursive_gcd(sec, fst % sec)
'''
recursive_gcd(300, 58)
Output is 2
'''
