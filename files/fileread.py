def main():
    infile = open('files/philosophers.txt','r')

    file_contents = infile.read()

    infile.close()

    print(file_contents)

main()