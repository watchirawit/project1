num_employees = 6

def main():
    hours = [0] * num_employees

    for index in range(num_employees):
        print("Enter the hours worked by employee",\
            index + 1, ': ', sep='',end='')
        hours[index] = float(input())

    pay_rate = float(input('Enter the hourly pay rate: '))

    for index in range(num_employees):
        gross_pay = hours[index] * pay_rate
        print('Gross pay for employee',index + 1, ':$',\
            format(gross_pay,',.2f'),sep='')

main()