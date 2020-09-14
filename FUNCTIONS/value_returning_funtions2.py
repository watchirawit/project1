def main():
    first_name, last_name = get_name()
    print('First name :',first_name,'Last name :',last_name)
    print(password2(first_name,last_name))

def get_name():
    first = input('Enter your first name: ')
    last = input('Enter your last name: ')
    return first,last

def password(f,l):
    if len(l) % 2 == 0:
        print('password',f[:3]+ (l)[(len(l)//2)-2:(len(l)//2) + 1])
    else:
        print('password',f[:3]+ (l)[(len(l)//2)-1:(len(l)//2) + 2])

def password2(f,l):
    if len(l) % 2 == 0:
        s = f[:3] + l[(len(l)//2)-2:(len(l)//2) + 1]
    else:
        s = f[:3]+ l[(len(l)//2)-1:(len(l)//2) + 2]
    return 'Password:' + s

main()


