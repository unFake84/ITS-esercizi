# creo lista vuota
lista: list[int] = []

# utilizzo il ciclo FOR e la funzione .APPEND per far inserire un numero dopo l'altro,
# fino al raggiungimento dell'obiettivo.
for loop in range(1, 1000001):

    lista.append(loop)

# METODO 1
# utilizzo '*' per non mostare le parentesi [] 
print(*lista)

# METODO 2
# per stamapare la lista senza le parentesi {*lista->} e una sotto l'altra {->lista, sep= "\n"}
# print(*lista, sep = "\n")









# APPUNTI:
# il sep aiuta a dividere tutti gli elementi di una lista esempio = ,sep = "\n" quando la stampi per intero
# l'end aiuta a dividere gli elementi che vengono passati nel print durante un for o while