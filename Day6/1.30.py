# from sys import argv # global variable. We have to get it into main.
def main():
    from sys import argv
    script, filename = argv
    filehand = open(filename) # have to be indented otherwise it wont work because filename was defined locally so it won't work globally.

    count = 0
    line = filehand.readline()
    words = len(line.split()) #split the strings into a list.
    chars = len(line)
    while line:
        count += 1
        line = filehand.readline()
        words += len(line.split())
        chars += len(line)


    print(f"{count} {words} {chars} {filename}")

main()
