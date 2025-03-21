'''
Given is the class Animal. For each task, test your changes!
1. Create two realistic instances of Animals
2. Print the name of each object
3. Change the amount of legs of one object using the dot notation
4. Add a method setLegs() to set the legs of an object and repeat task 3 but
this time using the method.
5. Add a method getLegs() to return the amount of legs
6. Add a method named printInfo that prints all attributes of the Animal
'''

class Animal:

    def __init__(self, species: str, legs: int):

        self.species = species
        self.legs = legs

        # 4a.
    def set_legs(self, newlegs: int):

        self.legs = newlegs

    # 5.
    def get_legs(self):

        return self.legs
    
    # 6.
    def print_info(self) -> None:

        print(f"The {self.species}, composed of {self.legs} legs, lives on Earth.")

# 1.
gatto: Animal = Animal("Cat", 4)
umano: Animal = Animal("Human", 2)

# 2.
print(f"{gatto.species} has {gatto.legs} legs.")
print(f"{umano.species} has {umano.legs} legs.")

# 3.
umano.legs = 3
print(f"Some {umano.species}s has {umano.legs} legs sometimes in the morning.")

# 4b.
umano.set_legs(2)

# 6b.
gatto.print_info()
umano.print_info()