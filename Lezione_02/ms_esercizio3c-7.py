'''
Si scriva un programma in python che computi la statistica di otto lanci di una moneta.
Per ciascuno dei lanci effettuati, l'utente inserisce "t" o "T" se è uscito "testa", mentre inserisce "c" o "C" se è uscito "croce".
Il programma deve mostrare in output il numero totale e la percentuale dei risultati "testa" e "croce".

NOTA.
Le percentuali devono essere mostrate in output obbligatoriamente con 2 cifre decimali.
Usare il match statement.
'''
import os
import time

monete: list[str] = []
count_t: int = 0
count_c: int = 0
lancio: int = 1

while len(monete) < 8:

    user: str = (input(f"Inserire {lancio}° lancio,\n['t'/'T'-'c'/'C']\n  /^\     /^\ \n Testa o croce?: ").lower())

    match user:

        case user if user == 't' or user == 'T':

            monete.append(user)
            count_t += 1
            lancio += 1
            os.system('clear')
            

        case user if user == 'c' or user == 'C':

            monete.append(user)
            count_c += 1
            lancio += 1
            os.system('clear')

        case _:

            print("Errore inserire 'c', 'C' oppure 't', 'T'")
            time.sleep(2)
            os.system('clear')

print(f"Testa: {count_t}")
print(f"Croce: {count_c}")
print(f"Percentuale Testa = {((count_t / 8) * 100):.2f}")
print(f"Percentuale Croce = {((count_c / 8) * 100):.2f}")
time.sleep(5)
print("Grazie e arrivederci!") # os.system('clear') non si può inserire dentro un print se non si vuole far visualizzare '0' al suo posto.
time.sleep(2)
os.system('clear')



# esecuzione con IF 
#---------------------------------------------------------
#     if user == "t":

#         monete.append(user)
#         count_t += 1
        
#     elif user == "c":

#         monete.append(user)
#         count_c += 1

#     else:

#         print("Errore inserire 'c' o 't'!.")       

# print(count_t)
# print(count_c)
# print(f"{((count_t / 8) * 100):.2f}")
# print(f"{((count_c / 8) * 100):.2f}")