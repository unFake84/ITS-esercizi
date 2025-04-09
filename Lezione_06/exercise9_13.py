'''
Dice: 

1.
    Make a class Die with one attribute called sides, which has a default value of 6.
    
2.
    Write a method called roll_die() that prints a random number between 1 and the number of sides the die has.

3.
    3a.
        Make a 6-sided die and roll it 10 times.
    
    3b.
        Make a 10-sided die and a 20-sided die.
    
    3c.
        Roll each die 10 times.

'''

import random

# 1.
class Die:

    def __init__(self, sides: int = 6):

        self.sides = sides

    # 2.
    def roll_die(self) -> int:
        
        die: int = random.randint(1, self.sides)

        print("-"*10, "\n" , f"Risultato: [{die}]", "\n" ,"-"*10)

# 3
if __name__ == "__main__":

    # 3a.
    lancio1: Die = Die(6)

    lanci: int = 1
    print("\n\t", "WHILE <=")
    while lanci <= 10:
    
        print(f"lancio n: {lanci}")
        lancio1.roll_die()
        lanci += 1

    # 3b.

    lancio2: Die = Die(10)
    lancio3: Die = Die(20)
    
    # 3c.
    print("\n\t", "10sides FOR in RANGE")
    for dadi2 in range(1, 11):

        print(f"lancio n: {dadi2}")
        lancio2.roll_die()
    
    print("\n\t", "20sides FOR in RANGE")
    for dadi3 in range(1, 11):

        print(f"lancio n: {dadi3}")
        lancio3.roll_die()