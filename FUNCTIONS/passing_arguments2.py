def main():
    print('The sum of first number and last number is')
    num1 = int(input('Enter your first number: '))
    num2 = int(input('Enter yuor last number: '))
    show_sum(num1,num2)
def show_sum(num1,num2):
    result = num1 + num2
    print(result)
main()