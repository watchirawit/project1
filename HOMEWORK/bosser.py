def main():
     yes_or_no = 'Y'
     string = input('Input sentence: ')
     string1 = string.split()
     while yes_or_no == 'Y' or yes_or_no == 'y':
           for i in string1:
          
               if i[0] != ('A' or 'E' or 'I' or 'O' or 'U') and i[-2] != 'A' and i[-1] != 'Y':
                    print(i[1:] + i[0] + 'AY',end=' ')
               elif  i[-3] == 'H' and i[-2] == 'A' and i[-1] == 'Y':
                    print(i[:-3],end=' ')
               elif i[-2] == 'A' and i[-1] == 'Y':
                    print(i[-3] + i[:-3],end=' ')
               elif i[0] == ('A' or 'E' or 'I' or 'O' or 'U') and i[-2] != 'A' and i[-1] != 'Y':
                    print(i + 'HEY',end=' ')
               else:
                    print(i[1:] + i[0] + 'AY',end=' ')

           yes_or_no = input('\nAny more sentence: ')
           if yes_or_no == 'Y' or yes_or_no == 'y':
               string = input('Input sentence: ')


   
          
main()