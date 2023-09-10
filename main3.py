def main():
    file = open('myfile.txt', 'r')
    line = int(file.read())
    number = int(input())
    x = line + number
    file = open('myfile.txt', 'w')
    file.write(str(x))
    print(f"{line} + {number} = {x}")
main()