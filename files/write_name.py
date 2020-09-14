def main():
    print('Enter the names of three friends. ')
    name1 = input('Friends #1: ')
    name2 = input('Friends #2: ')
    name3 = input('Friends #3: ')

    myfile = open('friends.txt','w')

    myfile.write(name1 + '\n')
    myfile.write(name2 + '\n')
    myfile.write(name3 + '\n')

    myfile.close()
    print('The name were written to friends.txt')

main()