def sum_digit(number):
    target = int(number)
    # raise an error to make sure the target number is positive
    if target < 0:
        return ValueError
    if target == 0:
        return 0
    elif target < 10:
        return target
    else:
        # we can calculate each number by target % 10, after that call this function it self to do it again.
        return(target % 10) + sum_digit(target//10)

print(sum_digit(12345))

'''
With input 12345
output is 15

With input 38765
output is 29
'''
