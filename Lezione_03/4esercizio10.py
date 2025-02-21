# creo una lista da 1 a 10
lista: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# usato lo SLICE per printare i primi 3 elementi della lista
print(f"\nThe first three items in the list are: \n{lista[0:3]}")

# usato lo SLICE per printare gli elementi che si trovanp nella metà della lista
print(f"\nThree items from the middle of the list are: \n{lista[3:7]}")

# usato lo SLICE per printare gli ultimi 3 elementi della lista
print(f"\nThe last three items in the list are: \n{lista[7:]}")