from sys import argv

script, input_file = argv
#Define the file f, f is just like a variable in other functions but in this case it's a file.
def print_all(f):
    print(f.read())
#seek(0) means moving to the start of a file. seek() function deals in bytes, not line, and it moves the file to 0 byte (first bite) in the file.
def rewind(f):
    f.seek(0)
#readline means reading one line at a time.
def print_a_line(line_count, f):
    print(line_count, f.readline())

current_file = open(input_file)

print("First let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print three lines:")
#current_line is the variable assigned for line_count in print_a_line function.
current_line = 1 #current_line = 1
print_a_line(current_line, current_file)

current_line += 1 #current_line = 2
print_a_line(current_line, current_file)

current_line += 1 #current_line = 3
print_a_line(current_line, current_file)
