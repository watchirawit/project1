def main():
    cities = ['New York', 'Boston','Atlanta','Dallas']
    outfile = open('cities.txt','w')

    outfile.writelines(cities)

    outfile.close()

main()