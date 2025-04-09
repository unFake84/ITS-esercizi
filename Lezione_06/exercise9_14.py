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
        winning_ticket = random.choices(self.lista, k = 4)

        return winning_ticket

    # 3.
    def display(self) -> str:

        print(f"I numeri vincenti sono: {', '.join(map(str, self.randomly()))}")

if __name__ == "__main__":

    prova: LotteryMachine = LotteryMachine()

    prova.randomly()
    prova.display()