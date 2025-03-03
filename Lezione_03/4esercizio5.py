# creo lista vuota
lista: list[int] = []

# utilizzo il ciclo FOR e la funzione .APPEND per far inserire un numero dopo l'altro fino al raggiungimento dell'obiettivo
for loop in range(1, 1000001):

    lista.append(loop)

# print(lista) # commentato per velocizzare l'esecuzione

# utilizzo la funzione MIN dentro PRINT per stampare il primo numero della lista
print(min(lista))

# utilizzo la funzione MAX dentro PRINT per stampare l'ultimo numero della lista
print(max(lista))

# utilizzo la funzione SUM per sommare tutti i numeri da 1 a 1mil. e controllare la velocità di calcolo(?)
print(sum(lista))
# quick!