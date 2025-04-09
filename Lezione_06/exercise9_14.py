'''
Lottery:

1.
    Create a class LotteryMachine that holds a list containing a series of 10 numbers and 5 letters.
    
2.
    Implement a method to randomly select 4 items (numbers or letters) from this list to draw a winning ticket.
    
3.
    Finally, implement a method to display a message saying that any ticket matching the winning 4 items wins a prize.

'''

import random

# 1.
class LotteryMachine:

    def __init__(self, lista: list[str, int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "a", "e", "i", "o", "u"]):

        self.lista = lista

    # 2.
    def randomly(self) -> list:

        winning_ticket: list[str, int] = []
 
        for _ in range(4):

            drawer: int = random.choice(self.lista)
            winning_ticket.append(drawer)

        return winning_ticket

    # 3.
    def display(self) -> None:

        print(f"I numeri vincenti sono: {self.randomly()}")