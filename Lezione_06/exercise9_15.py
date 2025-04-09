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

class LotteryMachine:

    def __init__(self, lista: list[str, int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "a", "e", "i", "o", "u"]):

        self.lista = lista

    def randomly(self) -> list:

        winning_ticket: list[str, int] = []
        winning_ticket = random.choices(self.lista, k = 4)

        return winning_ticket

    def display(self) -> str:

        print(f"I numeri vincenti sono: {', '.join(map(str, self.randomly()))}")