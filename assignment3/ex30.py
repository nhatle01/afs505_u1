people = 30
cars = 40
trucks = 15

# If "if" is False then "else" will run. Elif is used in the block that when elif is true, python stops checking the other statements in that same "if" block. Meaning if there were 2 true elif statement, only one will get printed.
if cars > people:
    print("We should take the cars.")
elif cars < people:
    print("We should not take the cars.")
else:
    print("We can't decide.")

if trucks > cars:
    print("That's too many trucks.")
elif trucks < cars:
    print("Maybe we could take the trucks.")
elif trucks < people:
    print("There are less trucks are than people.") # This wont print even that it's true.
else:
    print("We still can't decide.")

if people > trucks:
    print("Alright, let's just take the trucks.")
else:
    print("Fine, let's stay home then.")

if cars > trucks and trucks < people or people < cars:
    print("Trucks rule.")
