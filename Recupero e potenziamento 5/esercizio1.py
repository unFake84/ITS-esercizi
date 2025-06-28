'''
Data una matrice quadrata di dimensione m x m,
il carico di una posizione (r,c), indicato con k(r,c),
è dato dalla differenza tra la somma degli elementi della riga r e la somma degli elementi della colonna c.

Ad esempio, data la seguente matrice:
 
1   2   1   1
0   0   0   1
1   1   2   0
2   0   0   0
 
alcuni dei carichi sono:

c(0,0) = 1

c(1,0) = -3

c(3,3) = 0


Implementare i seguenti punti in python: 
'''

import random

def genera(dim: int) -> list[list[int]]:
    '''
    1.A Scrivere una funzione genera(),
    che data in input la dimensione dim della matrice genera una matrice quadrata di dimensione dim x dim,
    ovvero una matrice che ha dim righe e dim colonne.
    Ogni elemento di questa matrice è un numero random tra 0 e 13.
    Inoltre, in ogni riga, ogni elemento della riga deve essere diverso dal primo elemento della riga stessa.
    '''
    if not isinstance(dim, int):
        raise ValueError("Non è un intero")

    # return [random.sample(range(0,14), dim) for _ in range(dim)]  <<-- genera si numeri diversi dal primo elemento, ma non sono ripetibili tra loro
    mat: list[list[int]] = []

    for r in range(dim):

        row: list[int] = []
        for c in range(dim):

            while True:

                x: int = random.randint(0,13)

                if c == 0:
                    row.append(x)
                    break

                if x != row[0]:
                    row.append(x)
                    break

        mat.append(row)

    return mat

def printMAT(mat: list[list[int]]) -> None:
    '''
    1.B Scrivere una funzione printMAT(),
    che data in input una matrice, la stampa in output,
    in modo tale che ogni elemento della matrice occupi in output 5 caratteri.
    '''
    # [<<espressione_if_true>> if condizione else <<espressione_if_false>> for elemento in iterabile]
    # [espressione for elemento1 in sequenza1 for elemento2 in sequenza2 (if condizione)]

    for r in range(len(mat)):

        for c in range(len(mat[r])):

            print(f"{mat[r][c]:<5}", end="")

        print("\n")

def calcolaCarico(mat: list[list[int]], r: int, c: int) -> int:
    '''
    1.C Scrivere una funzione calcolaCarico(),
    che dati in input una matrice,
    un indice riga r ed un indice colonna c,
    calcola e restituisce il carico della matrice k(r,c) per la riga r e la colonna c. 
    '''
    sommaR: int = sum(mat[r])
    sommaC: int = 0
    for colonna in range(len(mat)):
        sommaC += mat[colonna][c]   

    return sommaR - sommaC

def caricoNullo(mat: list[list[int]]) -> list[tuple[int, int]]:
    '''
    1.D Scrivere una funzione caricoNullo(),
    che data in input una matrice,
    restituisce una lista di tuple,
    dove ogni tupla rappresenta una coppia di indici (r,c) per cui il carico della matrice è nullo.
    Ovvero, dovete trovare tutte le righe r e le colonne c per cui il carico della matrice k(r,c)=0
    e memorizzare ogni coppia (tupla) in una lista.
    '''
    lista_diTuple: list[tuple] = []

    for j in range(len(mat)):
        for k in range(len(mat)):

            nullo: int = calcolaCarico(mat, j, k)

            if nullo == 0:
                lista_diTuple.append((j, k))

    return lista_diTuple

def caricoMax(mat: list[list[int]]) -> tuple[int, int]:
    '''
    1.E Scrivere una funzione caricoMax(),
    che data in input una matrice restituisce una tupla di indici r e c
    per i quali si ha il carico massimo della matrice.
    Ovvero, dovete trovare la coppia di indice riga r e indice colonna c per cui il carico k(r,c) ha valore massimo.
    Prima di restituire la tupla di indici (r,c) stampare il valore del carico massimo.
    '''
    confronta: int = calcolaCarico(mat, 0, 0)
    tupla_finale: tuple[int, int] = (0, 0)

    for j in range(len(mat)):
        for k in range(len(mat)):

            carico: int = calcolaCarico(mat, j, k)

            if carico >= confronta:
                confronta = carico
                tupla_finale = (j, k)
    print(confronta)
    return tupla_finale

def caricoMin(mat: list[list[int]]) -> tuple[int, int]:
    '''
    1.F Scrivere una funzione caricoMin(),
    che data in input una matrice restituisce una tupla di indici r e c
    per i quali si ha il carico minimo della matrice.
    Ovvero, dovete trovare la coppia di indice riga r e indice colonna c per cui il carico k(r,c) ha valore minimo.
    Prima di restituire la tupla di indici (r,c) stampare il valore del carico minimo.
    '''
    confronta: int = calcolaCarico(mat, 0 ,0)
    tupla_finale: tuple[int, int] = (0, 0)

    for j in range(len(mat)):
        for k in range(len(mat)):

            carico: int = calcolaCarico(mat, j, k)

            if carico <= confronta:
                confronta = carico
                tupla_finale = (j, k)
    print(confronta)
    return tupla_finale

if __name__ == "__main__":
    '''
    1.G Scrivere un codice driver che:

    I. 
    richiamando la funzione genera(),
    genera una matrice di dimensione 5 x 5
    e richiamando la funzione printMAT()
    stampa tale matrice a schermo;

    II.
    individua quante posizioni sono a carico nullo e quali sono,
    stampandole a schermo, ricorrendo alla funzione caricoNullo();

    III.
    stampi a schermo gli indici riga rmax e colonna cmax per cui si ha il carico massimo della matrice.
    Ricorrendo alla funzione calcolaCarico(),
    stampare il carico della matrice k(rmax, cmax)
    per verificare che tale carico sia uguale a quello stampato in output dalla funzione caricoMax();

    IV.
    stampi a schermo gli indici riga rmin e colonna cmin per cui si ha il carico minimo della matrice.
    Ricorrendo alla funzione calcolaCarico(),
    stampare il carico della matrice k(rmin, cmin)
    per verificare che tale carico sia uguale a quello stampato in output dalla funzione caricoMin().
    '''
    # I.
    matrice = genera(5)
    print("\n\tMATRICE")
    printMAT(matrice)

    # II.
    print("\nCARICO NULLO NELLA MATRICE")
    trovato_carico: int = caricoNullo(matrice)
    if trovato_carico:
        print(
            f"E\' stato trovato un carico nullo,\nnei seguenti indici (riga, colonna): "\
                if len(trovato_carico) < 2 else\
                    f"Sono stati trovati {len(trovato_carico)} carichi nulli,\nnei seguenti indici (riga, colonna): ",\
                trovato_carico
        )
    else:
        print("Non è stato trovato nessun carico nullo")

    # III.
    print("\nCARICO MAX")
    carico_max: tuple[int, int] = caricoMax(matrice)
    print(f"E\' stato trovato nelle seguenti righe, colonne: {carico_max[0]}, {carico_max[1]}")


    # IV.
    print("\nCARICO MIN")
    carico_min: tuple[int, int] = caricoMin(matrice)
    print(f"E\' stato trovato nelle seguenti righe, colonne: {carico_min[0]}, {carico_min[1]}")

    # # EXTRA.
    # print("\nCARICO MATRICE")
    # print(f"Il carico della matrice r2 c2 è: {calcolaCarico(matrice, 2 ,2)}")





















    

    # caricoMin
    # return f"Carico min = {confronta} trovato nelle seguenti righe, colonne = {tupla_finale}"

    # caricoMax
    # return f"Carico max = {confronta} trovato nelle seguenti righe, colonne = {tupla_finale}"

    # caricoNullo
    # trovatouno: str = "E\' stato trovato un carico nullo,\nnei seguenti indici (riga, colonna): "
    # piudiuno: str = "Sono stati trovati più di un carico nullo,\nnei seguenti indici (riga, colonna): "
    # nessuncarico: str = 'Non è stato trovato nessun carico nullo'

    # return f"{piudiuno if len(lista_diTuple) > 1 else trovatouno} {lista_diTuple}" if lista_diTuple else nessuncarico













    # somma_riga: int = 0
    # somma_colonna: int = 0
    # for riga in range(len(mat)):
    #     print(f"entra riga {riga}")
        
    #     print(mat[riga])

    #     for colonna in range(len(mat)):
    #         print(f"entra colonna {colonna}")

    #         somma_colonna = 0
    #         lunghezza: int = len(mat[colonna])
    #         somma_colonna += mat[colonna][0]
    #         print(mat[colonna][0])

    #         print(f"esce colonna {colonna}")

    #     print(f"esce riga {riga}")
    #     print(f"somma colonna {somma_colonna}")









    # lista_dituple: list[tuple[int, int]] = []
    # somma_colonna: int = 0
    # somma_riga: int = 0
    # print("inizio ciclo generale")
    # for riga in range(len(mat)):
    #     print(f"inizio riga {riga}")
    #     #print(mat[riga][0])
        
    #     somma_riga = sum(mat[riga])
    #     print(f"somma riga = {somma_riga}")
    #     print(f"Lista riga ->{mat[riga]}")
    #     print("fine riga")

        
        
    #     for colonna in range(len(mat)):
    #         print(f"inizio colonna {colonna}")
    #         somma_colonna = 0
            
    #         # summ = sum(mat[colonna])
    #         # print(f"summ{summ}")
    #         # somma_colonna += mat[colonna][riga]

    #         #print(mat[colonna][riga])

    #         somma_colonna += mat[colonna][riga]
    #         print(f"somma colonna {mat[colonna][riga]} = {somma_colonna}")

    #         # somma_colonna = sum(mat[colonna])
    #         # print(f"Somma colonna = {somma_colonna}")
    #         # print(f"colonna ->{mat[colonna]}")
    #         print("fine colonna")
            
        
    #     print("inizio confronto?")
    #     carico = somma_riga - somma_colonna
    #     print(f"\nR{somma_riga} - C{somma_colonna} = Carico '{carico}'\n")
    #     if carico == 0:
    #         print("!!!!!!!!!!!listatuplaetc!!!!!!!!!!!!!!!")
    #     print("fine confronto")
    # print("Fine ciclo generale")



    # somma_riga: int = 0
    # somma_colonna: int = 0
    # carico: int = 0    
    # lista_dituple: list[tuple[int, int]] = []

    # for riga in range(len(matrice)):
    #     somma_riga = sum(matrice[riga])
    #     for colonna in range(len(matrice[0])):
    #         somma_colonna += matrice[colonna]
    #         carico = somma_riga - somma_colonna
    #         if carico == 0:
    #             tupla_singola: tuple[int, int] = (riga, colonna)
    #             lista_dituple.append(tupla_singola)


    # lista_dituple: list[tuple[int, int]] = []

    # r: int = 0
    # c: int = 0
    # carico: int = 0
    # sommaR: int = 0
    # sommaC: int = 0

    # while range(len(mat)):
    #     sommaR = sum(mat[r])
    #     sommaC = 0
    #     for colonna in range(len(mat)):
    #         sommaC += mat[colonna][c]
    #     carico = sommaR - sommaC
    #     if carico == 0:
    #         tupla_singola: tuple[int, int] = (r, c)
    #         lista_dituple.append(tupla_singola)
    #     r += 1 if len(mat) else 0
    #     c += 1


    # #risultatonullo = True if sommaR - sommaC == 0 else False
    

    # return carico if carico else "Non è stato trovato nessun carico nullo"
    # # for riga in range(len(mat)):
    # #     for colonna in range(len(mat)):
    # #         pass#mat[]
    # # pass
