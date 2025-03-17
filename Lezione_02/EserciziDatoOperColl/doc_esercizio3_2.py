'''
Greetings:
Start with the list you used in Exercise 3-1,
but instead of just printing each person’s name, print a message to them.
The text of each message should be the same,
but each message should be personalized with the person’s name
'''

names: list = ["a", "b", "c", "d", "e"]

for name in names:

    print(f"{name}, no f")

names: list = ["a", "b", "c"]

print("ciao " + names[0])
print("ciao " + names[1])
print("ciao " + names[2])