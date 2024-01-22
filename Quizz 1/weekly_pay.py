def wage():
    hourly_wage = float(input('Please enter the hourly wage of employee: '))
    regu_hour = float(input('Please enter the regular hours employee worked: '))
    over_time = float(input('Please enter the over time hours emplyee worked: '))
    total_wage = regu_hour * hourly_wage + over_time * 1.5 * hourly_wage
    return total_wage

print(wage())

'''
With input: 10, 10, 5
Output is
Please enter the hourly wage of employee: 10
Please enter the regular hours employee worked: 10
Please enter the over time hours emplyee worked: 5
175.0
With input: 20, 23, 2
Output is: 
Please enter the hourly wage of employee: 20
Please enter the regular hours employee worked: 23
Please enter the over time hours emplyee worked: 2
520.0
'''
