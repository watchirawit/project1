def main():
    filename = input('Enter a filename: ')

    try:

        infile = open(filename, 'r')

        contens = infile.read()

        print(contens)

        infile.close()

    except IOError:
        print('An error occurred trying to read')
        print('the file',filename)

main() 