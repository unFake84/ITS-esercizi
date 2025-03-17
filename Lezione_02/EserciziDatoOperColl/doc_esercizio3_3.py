'''
Your Own List:
Think of your favorite mode of transportation,
such as a motorcycle or a car, and make a list that stores several examples.
Use your list to print a series of statements about these items,
such as “I would like to own a Honda motorcycle.”
'''

moto: list = ["Ducati", "Yamaha", "Honda"]

for i in range(len(moto)):

    print(f"La {moto[i]}, è la mia {i+1}° preferita")

# print(f"La mia moto preferita in assoluto è, {moto[0]}")
# print(f"La mia seconda moto preferita è, {moto[1]}")
# print(f"La mia terza moto preferita è, {moto[2]}")


dream_list:list[str] = ["Honda Civic", "BMW m2", "Aprilia"]

print("Vorrei una " + dream_list[0])
print("Vorrei un " + dream_list[1])
print("Vorrei una " + dream_list[2])