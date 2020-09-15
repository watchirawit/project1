def main():
    try:
        
        a, b = map(int,input('Input 2 integer values: ').split())
        boss = divide(a, b)
        
    except Exception as err:
        print(err)
    #except ZeroDivisionError:
        #print("division by zero!")
    else:
        print("result is",boss)
    finally:
        print('executing finally clause')

def divide(x, y):
    result = x / y
    return result
    
    
main()