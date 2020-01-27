def coke_and_pepsi(cans_of_coke, cans_of_pepsi):
    print(f"There are {cans_of_coke} cans of coke!")
    print(f"There are {cans_of_pepsi} cans of pepsi!")


print("First run:")
coke_and_pepsi(5,10)

print("Second run:")
coke = 2
pepsi = 4
coke_and_pepsi(coke, pepsi)

print("Third run:")
coke_and_pepsi(2 * 3, 2 * 4)

print("Fourth run:")
additional_one = 1
coke_and_pepsi(coke + additional_one, pepsi + additional_one)

print("Fifth run:")
print("Cans of coke:")
coke = int(input())
print(f"Cans of pepsi:")
pepsi = int(input())
coke_and_pepsi(coke, pepsi)

print("Sixth run:")
cokeandpepsi = coke_and_pepsi
cokeandpepsi(10,20)
