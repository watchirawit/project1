def main():
    number = int(input('Enter a nonegative interger: '))
    fact = factorial(number)
    print('The factorial of',number,'is',fact)

def factorial(num):
    if num <= 1:
        return 1
    else:
        return num + factorial(num - 1)
main()