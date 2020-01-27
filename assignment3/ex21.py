def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b #return the addtion of a + b. Python adds 2 numbers, and when the functions ends, any line that runs it will be able to assign this a +b result to a variable.
def substract(a, b):
    print(f"SUBSTRACTING {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"MULTIPLYNG {a} * {b}")
    return a * b

def devide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b

print("Let's do some math with just functions!")

age = add(30, 5)
height = substract(78, 4)
weight = multiply(90, 2)
iq = devide(100, 2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")


#A puzzle for the extra credit, type it in anyway.
print("Here is a puzzle.")

what = add(age, substract(height, multiply(weight, devide(iq, 2))))
#what = (30 + 5) + ((78 - 4) - (90 * 2) * (100 / 2))
print("That becomes: ",what, "Can you do it by hand?")

#calculation = 24 + 34 / 100 - 1023
calculation = add(24, substract(devide(34, 100), 1023))
print(f"The result is: {calculation}")
