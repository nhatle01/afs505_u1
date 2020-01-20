formatter = "{} {} {} {}"
# Formatter is a varible that is made up of 4 {}. 6 tells python to print formatter 4 times which is why the result has 16 {}.
print(formatter.format(1, 2, 3, 4 ))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True)) #No need to put quotes around True or False because Python recognizes True and False as keywords representing the concept of true and false.
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))
