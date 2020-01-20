types_of_people = 10
x = f"There are {types_of_people} types of people."
# Assign string value by using "string". Quotations are not required for numerical values.
binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."
# Use f"string{string}" for a string that contains a string
print(x)
print(y)

print(f"I said: {x}")
print(f"I also said: '{y}'")
# Using ".format()" when the statement is made up of 2 variables and not a string statement. No need to use quotes for True/False.

hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

print(joke_evaluation.format(hilarious))
# w means "write" which starts the statement and e means "end" that is why when you add w + e it combines w and e for a full statement.
w = "This is the left side of..."
e = "a string with a right side."

print(w + e)
