# Assign variables names and values associated with it.Can be numerical values or a function.
cars = 100
space_in_a_car = 4
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

# Print the sentence and seperate variables by "," (comma). Python will replace variable names with real numerical values.
print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")

#When using 4 instead of 4.0 the only difference is the result for "we can transport" that it is no longer a floating point number but 120.

x = 1
y = 2
z = 3
print("What is x * y * z?")
print (x * y * z)
