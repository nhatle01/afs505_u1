ten_things = "Apple Oranges Crows Telephone Light Sugar"

print("Wait there are not 10 things in that list. Let's fix that.")

stuff = ten_things.split(' ') # split the tring into a list.
more_stuff = ["Days", "Night", "Song", "Frisbee",
              "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop() # python does pop(more_stuff).Remove the item at the given position in the list, and return it. If no index is specified, a.pop() removes and returns the last item in the list.
    print("Adding: ",next_one)
    stuff.append(next_one) # python does append(stuff, next_one). Append move the item to the bottom of the list.
    print(f"There are {len(stuff)} items now.")

print("There we go: ", stuff)

print("Let's do some things with stuff.")

print(stuff[1])
print(stuff[-1])
print(stuff.pop())
print(' '.join(stuff)) # join a list of strings to a seperator. In this case, just 'space'
print('#'.join(stuff[3:5])) # stuff[3:5] extract a 'slice' from the stuff list that is from element 3 to element 4, meaning it does no include element 5. Similar to range (3,5)
