# creo lista vuota
lista: list[int] = []

# utilizzo il ciclo FOR e la funzione .APPEND per far inserire un numero dopo l'altro fino al raggiungimento dell'obiettivo
for loop in range(1, 10000001):

    lista.append(loop)

print(lista)

# print(*lista, sep = "\n") per stamapare la lista una sotto l'altra e senza le parentesi







# il sep aiuta a dividere tutti gli elementi di una lista esempio = ,sep = "\n" quando la stampi per intero
# l'end aiuta a dividere gli elementi che vengono passati nel print durante un for o while