def reverse_name(first,last):
    print(last[::-1],first[::-1])
def main():
    first_name = input('Enter your first name: ')
    last_name = input('Enter your last name: ')
    print('your name reversed is')
    reverse_name(first_name,last_name)
main()