#i = 0
#numbers = []

#while i < 6:
#    print(f"At the top i is {i}")
#    numbers.append(i)

#    i = i + 1
#    print("Numbers now: ", numbers)
#    print(f"At the bottom i is {i}")


#print("The numbers: ")

#for num in numbers:
#    print(num)

def while_loop(i, x, numbers):
    if i < x:
        print("At the top i is: ", i)
        numbers.append() # add numbers to the end of the list.

        i += 1
        print("Numbers now: ", numbers)
        print("At the bottom i is:", i)
        while_loop(i, x, numbers)
    return numbers

numbers = while_loop(0, 6, [])
for num in numbers:
    print(num)
