countries = ['Vietnam', 'China', 'Laos', 'Thailand'] #using [ ] instead of { } to keep the order.

for i, v in enumerate(countries): #position index and corresponding value can be retrieved at the same time.
    print(i, v)

capitals = ['Hanoi', 'Beijing', 'Vientiane', 'Bangkok']

for a, b in zip(countries, capitals):
    print(f"{a}\'s capital is {b}")

for a in sorted(set(countries)):
    print(a)
