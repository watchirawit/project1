import random
HEADS = 1
TAILS = 2
TOSSES = 5
total_h = 0
total_t = 0
def main():
    global total_h
    global total_t
    for boss in range(TOSSES):
        if random.randint(HEADS,TAILS) == HEADS:
            print('Heads')
            total_h = total_h + 1
            
        else:
            print('Tails')
            total_t = total_t + 1
    print('Total Heads',total_h)
    print('Total Tails',total_t)
    print('TOSSES',TOSSES)


main()
