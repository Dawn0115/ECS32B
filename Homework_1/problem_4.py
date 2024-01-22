# name: YANGCHENG
# finish date: 1/17
# This function is used to creat a table to calculate how much to pay when we do financing to buy a computer.
def payment_plan():
    # ask input from user to get the original price of computer
    price = float(input("Please enter the price of computer: "))
    down_payment_rate = 0.1
    annual_ir = 0.12
    mon_pay_rate = 0.05
    month = 1
    # amount of down_payment need to pay
    original_balance = price - (price * down_payment_rate)
    # money to pay in a month
    monthly_pay = original_balance * mon_pay_rate
    monthly_ir = annual_ir / 12
    # print the header
    print('{:>4}{:>20}{:>40}{:>40}{:>20}{:>40}'.format('Month', 'Total balance', 'Interest for that month', 'Principal for that month', 'Payment', 'Balance remaining' ))
    # determine whether the customer pay off balance
    while original_balance>0:
        if monthly_pay > original_balance:
            need_to_pay = original_balance
            monthly_pay = original_balance
            pay_interest = 0
        else:
            pay_interest = monthly_pay * monthly_ir
            need_to_pay = monthly_pay - pay_interest
        after_pay_balance = original_balance - need_to_pay
        # print these information continously by using while loop.
        print(f'{month:>4}{original_balance:>20}{pay_interest:>40}{need_to_pay:>40}{monthly_pay:>20}{after_pay_balance:>40}')
        original_balance = after_pay_balance
        month +=1
payment_plan()

'''
If input is 1000
Outputs looks like:
Month       Total balance                 Interest for that month                Principal for that month             Payment                       Balance remaining
   1               900.0                                    0.45                                   44.55                45.0                                  855.45
   2              855.45                                    0.45                                   44.55                45.0                       810.9000000000001
   3   810.9000000000001                                    0.45                                   44.55                45.0                       766.3500000000001
   4   766.3500000000001                                    0.45                                   44.55                45.0                       721.8000000000002
   5   721.8000000000002                                    0.45                                   44.55                45.0                       677.2500000000002
   6   677.2500000000002                                    0.45                                   44.55                45.0                       632.7000000000003
   7   632.7000000000003                                    0.45                                   44.55                45.0                       588.1500000000003
   8   588.1500000000003                                    0.45                                   44.55                45.0                       543.6000000000004
   9   543.6000000000004                                    0.45                                   44.55                45.0                      499.05000000000035
  10  499.05000000000035                                    0.45                                   44.55                45.0                      454.50000000000034
  11  454.50000000000034                                    0.45                                   44.55                45.0                      409.95000000000033
  12  409.95000000000033                                    0.45                                   44.55                45.0                       365.4000000000003
  13   365.4000000000003                                    0.45                                   44.55                45.0                       320.8500000000003
  14   320.8500000000003                                    0.45                                   44.55                45.0                       276.3000000000003
  15   276.3000000000003                                    0.45                                   44.55                45.0                      231.75000000000028
  16  231.75000000000028                                    0.45                                   44.55                45.0                      187.20000000000027
  17  187.20000000000027                                    0.45                                   44.55                45.0                      142.65000000000026
  18  142.65000000000026                                    0.45                                   44.55                45.0                       98.10000000000026
  19   98.10000000000026                                    0.45                                   44.55                45.0                       53.55000000000027
  20   53.55000000000027                                    0.45                                   44.55                45.0                        9.00000000000027
  21    9.00000000000027                                       0                        9.00000000000027    9.00000000000027                                     0.0
'''