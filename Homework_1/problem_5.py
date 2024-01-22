# name: YANGCHENG
# finish date: 1/18
# Gather and making a table for employees' name, work hours, and hourly wages

def wage():
    # ask input from user to get namw, wage and hours worked 
    name = input("Please enter the list of all employees' names: ")
    wage = input("Please enter the list of each employee's hourly wage: ")
    hour = input("Please enter the list of employees' hours worked: ")
    #print out the header of table
    print('{:>4}{:>4}{:>4}'.format('<last name>', '<hourly wage>', '<hours worked>'))
    #split the list that entered by user
    name = name.split(",")
    wage = wage.split(",")
    hour = hour.split(",")
    # print list out in order
    for a,b,c in zip(name,wage,hour):
        print(a,"       ",b,"        ",c)
wage()
'''
wage()
Outputs looks like:
Please enter the list of all employees' names: bill,howar,anna
Please enter the list of each employee's hourly wage: 100,600,500
Please enter the list of employees' hours worked: 12,12,12
<last name><hourly wage><hours worked>
bill         100          12
howar         600          12
anna         500          12
'''