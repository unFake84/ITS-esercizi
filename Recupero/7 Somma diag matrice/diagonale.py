'''
Somma delle Diagonali di una Matrice (Quadrata o
Rettangolare)
Data una matrice 2D (lista di liste) di interi con dimensioni n X n, scrivi due funzioni:
1. sum_primary_diagonal(matrix) che restituisce la somma della “diagonale
primaria” (dall’angolo in alto a sinistra verso il basso a destra).
2. sum_secondary_diagonal(matrix) che restituisce la somma della “diagonale
secondaria” (dall’angolo in alto a destra verso il basso a sinistra).
Requisiti:
● Entrambe le funzioni accettano una lista di liste.
● Restituisci un intero per ciascuna funzione.
Esempi:
mat1 = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]
]
sum_primary_diagonal(mat1) # restituisce 1 + 5 + 9 = 15
sum_secondary_diagonal(mat1) # restituisce 3 + 5 + 7 = 15
'''

def sum_primary_diagonal(matrix: list[list[int]]) -> int:

    sommatore: int = 0
    indice_min: int = 0

    for lista in matrix:
        sommatore += lista[indice_min]
        indice_min += 1

    return sommatore

def sum_secondary_diagonal(matrix: list[list[int]]) -> int:

    sommatore: int = 0
    indice_max: int = len(matrix) -1

    for lista in matrix:
        sommatore += lista[indice_max]
        indice_max -= 1

    return sommatore

if __name__ == "__main__":

    mat1 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
    ]

    primaria = [mat1[i][i] for i in range(len(mat1))]
    secondaria = [mat1[i][len(mat1) -1 -i] for i in range(len(mat1))]

    print("Matrice:\n\n",*[str(lista)+"\n" for lista in mat1])

    print(f"Risultato di {primaria} = {sum_primary_diagonal(mat1)}")
    print(f"Risultato di {secondaria} = {sum_secondary_diagonal(mat1)}")







    #   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    #   @ provafor = [indice for indice in mat1] @
    #   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@





    # # prima versione, accetta solo una matrice 3x3
    # sommatore: int = 0
    # indice: int = 0

    # for listacorrente in matrix:

    #     if indice == 0:
    #         sommatore += listacorrente[0]
    #         indice += 1

    #     elif indice == 1:
    #         sommatore += listacorrente[1]
    #         indice += 1

    #     else:
    #         sommatore += listacorrente[2]

    # return sommatore
    #----------------------------------------------
    #     sommatore: int = 0
    # indice: int = 0

    # for listamadre in matrix:

    #     if indice == 0:
    #         sommatore += listamadre[2]
    #         indice += 1

    #     elif indice == 1:
    #         sommatore += listamadre[1]
    #         indice += 1

    #     else:
    #         sommatore += listamadre[0]

    # return sommatore