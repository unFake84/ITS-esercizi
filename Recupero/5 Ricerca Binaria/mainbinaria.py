'''
Ricerca Binaria
Implementa una funzione che effettua la ricerca binaria in una lista di numeri interni ordinati
e ritorna True se il numero è all’interno del della lista, altrimenti False
'''

def ricerca(lista: list[int], numero: int) -> bool:
    inizio: int = 0
    fine: int = len(lista) -1

    while True:
        centro: int = (inizio + fine) // 2

        if inizio > fine:
            return False

        elif numero == lista[centro]:
            return True

        elif numero < lista[centro]:
            fine = centro - 1

        elif numero > lista[centro]:
            inizio = centro + 1

        else:
            return False

print(ricerca([1, 2, 3, 4, 5, 6, 7, 8, 9], 10))
lista_di_test: list[int] = [
    2, 4, 7, 9, 11, 13, 17, 19, 24, 27,
    31, 34, 38, 41, 45, 48, 52, 56, 59, 63,
    67, 71, 75, 78, 82, 86, 89, 93, 97, 100
    ]
lista_di_test2: list[int] = [2, 5, 8, 12, 16 ,23, 38, 45, 56, 72, 91]
print(ricerca(lista_di_test2, 72))

# PROF va fuori range con lista di test2
def bin_search(x, y):

    # i, j = 0, -1
    # mid = len(x)//2

    # if x[mid] == y:
    #     return True

    # if x[mid] > y:
    #     j = mid

    #     bin_search(x[i:j], y)

    # else:
    #     i = mid +1

    #     bin_search(x[i:j], y)
    j = -1
    mid = len(x)//2
    
    if x[mid] == y:
        return True

    else:
        return bin_search(x[mid:j], y) if x[mid] > y else bin_search(x[mid+1:j], y)

print(bin_search(lista_di_test2, 72))