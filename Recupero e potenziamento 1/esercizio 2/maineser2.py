'''
Scrivere un programma Python che legge in input prima un intero x positivo
e poi una sequenza di interi positivi. Se l'utente inserisce il numero 0, allora la sequenza deve terminare.

Per il numero x e per ogni numero della sequenza inserita,
effettuare il controllo che il numero inserito sia effettivamente un intero e
forzare l'utente ad inserire un numero intero positivo nel caso in cui questa condizione non venga rispettata.

Trovare una soluzione che eviti di scrivere codice duplicato per effettuare questa serie di controlli.
Suggerimento: per controllare che un numeri sia intero, usare la funzione is_integer().

Determinato il numero x e la sequenza di interi positivi, il programma deve produrre in output: 

    stampare la sequenza

    Il numero occ di occorrenze di x, ovvero  il numero di volte in cui appare x nella sequenza;

    La posizione pos del primo valore uguale a x.

    La somma di tutti i valori diversi da x;

Ad esempio, se l'utente inserisce come valore x il numero 3 e poi immette la sequenza: 7; 5; 1; 3; 3; 3; 11; 2; 3; 3; 0

il programma dovra' scrivere in output:

    stampare in output la sequenza

    Il numero 3 compare 5 volte nella sequenza (attenzione all'output se il numero compare 1 sola volta!)

    Il numero 3 compare per la prima volta in posizione 3 nella sequenza

    La somma dei valori della sequenza diversi da 3 e' 26
'''

import os

class PersonalError(Exception):
    pass


def isIntPositive(x: str) -> bool:

    try:
        x: int = int(x)
        return x > 0

    except ValueError:
        return False


def esegui(x: int, lista: list[int]) -> str:

    trovati: int = 0
    trovato_primoX: bool = False
    primoX: int = 0
    somma_noX: int = 0
    sequenza: str = '; '.join([str(n) for n in lista])
    stampami: str = ""
    stampami += sequenza + '\n\n'

    for i, trovami in enumerate(lista):

        if trovami == x:
            trovati += 1

            if trovato_primoX == False:
                primoX = i
                trovato_primoX = True

        if trovami != x:
            somma_noX += trovami

    if not trovato_primoX: 
        stampami += f"Il numero {x} non è presente nella lista\n"

    else: # elif primoX != 0 or trovati != 0:
        stampami += f"Il numero {x} compare {trovati} {'volta' if trovati == 1 else 'volte'} nella sequenza\n"
        stampami += f"Il numero {x} compare per la prima volta in posizione {primoX} nella sequenza\n"

    if somma_noX != 0:
        stampami += f"La somma dei valori della sequenza diversi da {x} è {somma_noX}"

    else:
        stampami += f"Impossibile calcolare la somma dei valori"

    return stampami


if __name__ == "__main__":

    erroreX: str = "inizia"
    erroreL: str = ""
    x: str = ""
    l: str = ""
    lista_di_l: list[int] = []
    controlla_x: bool = False
    controlla_l: bool = False
    trovato_x: bool = False
    conta_l: int = 0
    risultato: str = ""

    while True:

        os.system("clear")
        gui: str = f"""

Istruzioni:

1) Inserire un numero intero positivo.
        Verra chiamato il numero X

2) Inserire una sequenza di numeri.
        Determinato il numero x e la sequenza di interi positivi:
        a - verra stampato in output la sequenza
        b - Il numero occ di occorrenze di x,
            ovvero  il numero di volte in cui appare x nella sequenza.
        c - La posizione pos del primo valore uguale a x.
        d - La somma di tutti i valori diversi da x.

3) Premere 0 in qualsiasi momento,
    per terminare il programma.

{f'numero valido, hai inserito {x} come numero X, procedere con la lista:' if controlla_x is True else erroreX}
{erroreL if controlla_l is False else ''}

{lista_di_l if len(lista_di_l) < 15 else ''}
"""
        print(gui)

        if len(lista_di_l) == 15:
            risultato = esegui(x, lista_di_l)
            print(risultato)
            print("bYe")
            break

        if not controlla_x:
            x = input("Inserire il valore X: " ).strip()

        else:
            print(f"{conta_l}/15")
            l = input("Inserire un numero intero positivo: ").strip()

        if x == '0' or l == '0':
            risultato = esegui(x, lista_di_l)
            print(risultato)
            print("bYe")
            break

        controlla_l = False
        try:
            controlla_x = isIntPositive(x)
            controlla_l = isIntPositive(l)
            
        except PersonalError:
            if not controlla_x:
                controlla_x = False
            elif not controlla_l:
                controlla_l = False

        if not controlla_x:
            erroreX = f"Hai inserito >> {str(x) if x not in ('', ' ') else 'vuoto'}\nnon valido"

        if not controlla_l and trovato_x:
            erroreL = f"Hai inserito >> {str(l) if l not in ('', ' ') else 'vuoto'}\nnon valido"

        if controlla_x:
            x = int(x)
            trovato_x = True

        if controlla_l:
            l = int(l)
            conta_l += 1
            lista_di_l.append(l)

#################################################################################################################à










#         gui: str = f"""

#                                     Istruzioni:                         _________________________________________________________
#                                                                         |                                                       |
# 1) Inserire un numero intero positivo.                                  | Valore X: {str(x)+" "*helpGUI1+"|" if x else 'Da inserire'+" "*33+"|"}
#         Verra chiamato il numero X                                      |                                                       |
#                                                                         |                                                       |
# 2) Inserire una sequenza di numeri.                                     |                                                       |
#         Determinato il numero x e la sequenza di interi positivi:       |                                                       |
#         a - verra stampato in output la sequenza                        |                                                       |
#         b - Il numero occ di occorrenze di x,                           |                                                       |
#             ovvero  il numero di volte in cui appare x nella sequenza.  |                                                       |
#         c - La posizione pos del primo valore uguale a x.               |                                                       |
#         d - La somma di tutti i valori diversi da x.                    |                                                       |
#                                                                         |                                                       |
# 3) Premere 0 in qualsiasi momento,                                      |                                                       |
#     per terminare il programma.                                         |_______________________________________________________|
# {controlla_user if controlla_user else 'Inizia'}
# """
#         print(gui)

#         helpGUI1: int = 44 - len(x)














    #print(esegui(3, [7, 5, 1, 3, 3, 3, 11, 2, 3, 3]))








# def isIntPositive(x: int) -> bool:

#     if not isinstance(x, int) or x < 0:
#         return False

#     return True



# def checkX(x: str) -> bool:

#     xint: int

#     if isinstance(x, str):
#         try:
#             xint = int(x)
#         except ValueError:
#             return False

#     return True






# numeroX: int = 0

# while True:

#     os.system("clear")

#     print(
#         "\tIstruzioni:\n" \
#         "1) Inserire un numero intero positivo.\n"\
#         "2) Inserire una seguenza di numeri.\n"\
#         "3) Premere 0 per terminare il programma.\n"\
#     )
#     print(
#         f"Valore X: {numeroX if numeroX else 'Na'}\n"
#     )

#     try:
#         x: int = int(input("Inserire un numero intero positivo: "))
#         if x == 0:
#             print("bYe")
#             break
#     except FormulaError as riprova:
#         print(f"Hai inserito: {riprova}")





#     # if isinstance(x, int):
#     #     numeroX = int(x)
#     # elif x == 0:
#     #     print("bYe")
#     #     break
#     # else:
#     #     print(f"Hai inserito '{x}', non valido")

#     os.system("clear")