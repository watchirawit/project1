def main():
    value = 99
    print('The value is',value)
    chang_me(value)
    print('Back in main the value is',value)
def chang_me(arg):
    print('I am changing the value.')
    arg = 0
    print('Now the value is',arg)
main()