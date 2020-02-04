the_count = [1, 2, 3, 4, 5]
fruits = ['apple', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters'] # mixed list

# this first kind of for-loop goes through a list
for number in the_count: # the variable "number" is defined by the for -loop when it starts, initializng it to the current element of the loop iteration each time through.
    print(f"This is the count {number}")

# same as above
for fruit in fruits:
    print(f"A fruit of type:{fruit}")

# also we can go through mixed lists too
for i in change:
    print(f"I got {i}")

# we can aslo build lists, first start with an empty one
elements = range(0, 6)

# then use the range function to do 0 to 5 counts
#for i in range(0, 6):
#    print(f"Adding {i} to the list.") # Only list 1 to 5 but not the last number 6.
    # append is a function that lists understand
#    elements.append(i) # appends to the end of the list.

# now we can print them out too
for i in elements:
    print(f"Element was: {i}")
