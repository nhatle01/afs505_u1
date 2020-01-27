from sys import argv

script, filename = argv # Scrip is the ex15.py file. Using argv to run the file name along with the script.

txt = open(filename) #using command open to open a filename.

print(f"Here's your file {filename}:")
print(txt.read()) #called function on txt named read. You give a file a command by using .command(parameters).
print(txt.close())

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())
print(txt_again.close())
