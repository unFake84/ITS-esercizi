'''
Si scriva un programma in python che computi la statistica di otto lanci di una moneta.
Per ciascuno dei lanci effettuati, l'utente inserisce "t" o "T" se è uscito "testa", mentre inserisce "c" o "C" se è uscito "croce".
Il programma deve mostrare in output il numero totale e la percentuale dei risultati "testa" e "croce".

NOTA.
Le percentuali devono essere mostrate in output obbligatoriamente con 2 cifre decimali.
Usare il match statement.
'''

monete: list[str] = []
count_t: int = 0
count_c: int = 0

while len(monete) < 8:

    user: str = (input("Inserire testa o croce: ").lower())
    
    if user == "t":

        monete.append(user)
        count_t += 1
        
    elif user == "c":

        monete.append(user)
        count_c += 1

    else:

        print("Errore inserire 'c' o 't'!.")       

print(count_t)
print(count_c)
print(f"{((count_t / 8) * 100):.2f}")
print(f"{((count_c / 8) * 100):.2f}")