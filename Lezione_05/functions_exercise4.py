'''
Exercise 4
Write a function check_each(), which takes a list of numbers as argument.
Using a for loop, iterate through the list.
For each number, print “bigger” if it’s bigger than 5, “smaller” if it’s smaller than 5, and “equal” if it’s equal to 5.
'''

def check_each(lista: list[int]):

    for i in lista:

        if i == 5:

            print("EQUAL")

        elif i > 5:

            print("BIGGER")

        else:

            print(f"SMALLER")

lista_n: list[int] = [1, 2, 3, 4, 5, 6, 7, 8 ,9, 10]

check_each(lista_n)