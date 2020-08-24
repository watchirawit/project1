keep_going = 'y' 
while keep_going == 'y' or keep_going == "Y":
    sales = float(input('Enter the amount of sales: '))
    comm_rate = float(input('Enter the  commission rate: '))
    commission = sales * comm_rate
    print('the commission is $' , \
        format(commission,',.2f'), sep='')
    keep_going = input('do you want to calcurate another' + \
        'commission (Enter y for yes):')
             