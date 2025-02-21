# creo lista vuota
lista: list[int] = []

# utilizzo il ciclo FOR e la funzione .APPEND per far inserire un numero dopo l'altro fino al raggiungimento dell'obiettivo
for loop in range(1, 1000000+1):

    lista.append(loop)

print(lista)