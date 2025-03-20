'''
1. Copy the code and print the age of
bob (using the dot notation)
2. Create an if-statement that prints
the name of the oldest of the two
Persons
3. Create three other Persons. Make
a list called people with all 5
Persons.
4. Make a loop that finds and prints
the youngest person’s name
'''

from typing import Any

class Person:

    def __init__(self, name, age):

        self.name = name
        self.age = age

alice = Person("Alice W.", 45)
bob = Person("Bob M.", 36)

# 1.
print(bob.age)

# 2.
if bob.age < alice.age:

    print(f"Alice is {alice.age} years old, so compared to Bob, {bob.age}, she is older than him.")

# 3.
charlie = Person("Charlie B.", 47)
delta = Person("Delta A.", 87)
echo = Person("Echo F.", 25)

people: list[Any] = []

people.append(alice)
people.append(bob)
people.append(charlie)
people.append(delta)
people.append(echo)

# 4.
for i in people:

    if min(people):

        print("Banana")