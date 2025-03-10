'''
Exercise 3
Write a function print_numbers(), which takes a list of numbers as argument.
Using a for loop, print each number one by one.
'''

def print_numbers(lista: list[int]):

    for n in lista:

        print(n)

lista_n: list[int] = [1, 2, 3, 4, 5, 6, 7, 8 ,9, 10]

print_numbers(lista_n)