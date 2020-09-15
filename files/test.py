gg = 0
print('choes the menu 1 ro 2\n1.is read file\n2.is add text in file')
yes_or_no = 'Y'
inputnumber = int(input('Enter the menu: '))
while yes_or_no == "Y" or yes_or_no == "y":
    if inputnumber == 1:
        infile = open('friends.txt','r')
        file_contents = infile.read()
        infile.close()
        print(file_contents)
    if inputnumber == 2:
        boss = open('friends.txt','a')
        boss.write('\n' + str(input('Enter you str: ')))
        boss.close()
    if inputnumber == 3:
        boss1 = open('friends.txt','r')
        input_you_del = input('Enter you line to  del: ')
        boss2 = open('friends.txt','r')
        for count in boss1:
            gg = gg + 1
            
            print(str(gg) + '.' + count)
        
            
            boss1.close()
    yes_or_no = input('Do you want to choes the menu again y or n: ')
    if yes_or_no == "Y" or yes_or_no == "y":
        print('choes the menu 1 ro 2\n1.is read file\n2.is add text in file')
        inputnumber = int(input('Enter the menu: '))



