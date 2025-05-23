'''
Lottery Analysis: Extend the LotteryMachine class you created in Exercise 9-14.

1.
    Add a method called simulate_until_win(self, my_ticket) that:

        1a.
        Accepts a ticket (a list of 4 items).

        1b.
        Repeatedly draws random tickets using the draw_ticket() method.

        1c.
        Keeps count of how many attempts it takes until a randomly drawn ticket matches my_ticket.

        1d.
        Returns the number of attempts and the winning ticket.

2.
    Create a ticket called my_ticket with 4 numbers or letters from the pool.

3.
    Use the simulate_until_win() method to simulate how many draws it would take for your ticket to win.

4.
    Print a message showing:

        4a.
        Your ticket

        4b.
        The winning ticket
        
        4c.
        How many attempts it took to win

'''

import random
from typing import Any

class LotteryMachine:

    def __init__(self, lista: list[Any] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "a", "e", "i", "o", "u"]):

        self.lista = lista

    def randomly(self) -> list:

        winning_ticket: list[Any] = []
        winning_ticket = random.choices(self.lista, k = 4)

        return winning_ticket

    def display(self) -> str:

        print(f"I numeri vincenti sono: {', '.join(map(str, self.randomly()))}")

    # 1.
    def simulate_until_win(self, my_ticket: list[Any] = [1, 7, "a", 8]):

        # 1a.

        if len(my_ticket) != 4:

            return "Biglietto non valido."
        
        # 1c.
        contatore: int = 0

        # 1b.
        while True:

            win_ticket = self.randomly()

            if my_ticket != win_ticket:

                print(f"Nulla, riprova.")
                contatore += 1

            else:

                contatore += 1
                # 1d. + 4a.b.c.
                print(f"Vittoria!\nHai tentato {contatore} volte!\nNumero vincente: {win_ticket}")
                break

if __name__ == "__main__":

    # 2.
    slot: LotteryMachine = LotteryMachine()
    my_ticket: list[Any] = [9, 2, "a", "e"]
    
    # 3.
    slot.simulate_until_win(my_ticket)