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

    1.D Scrivere una funzione caricoNullo(),
        che data in input una matrice,
        restituisce una lista di tuple,
        dove ogni tupla rappresenta una coppia di indici (r,c) per cui il carico della matrice è nullo.
        Ovvero, dovete trovare tutte le righe r e le colonne c per cui il carico della matrice k(r,c)=0
        e memorizzare ogni coppia (tupla) in una lista.

    1.E Scrivere una funzione caricoMax(),
        che data in input una matrice restituisce una tupla di indici r e c
        per i quali si ha il carico massimo della matrice.
        Ovvero, dovete trovare la coppia di indice riga r e indice colonna c per cui il carico k(r,c) ha valore massimo.
        Prima di restituire la tupla di indici (r,c) stampare il valore del carico massimo.

    1.F Scrivere una funzione caricoMin(),
        che data in input una matrice restituisce una tupla di indici r e c
        per i quali si ha il carico minimo della matrice.
        Ovvero, dovete trovare la coppia di indice riga r e indice colonna c per cui il carico k(r,c) ha valore minimo.
        Prima di restituire la tupla di indici (r,c) stampare il valore del carico minimo.

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

    # return [random.sample(range(0,14), dim) for _ in range(dim)]
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
    for riga in range(len(mat)):
        sommaC += mat[riga][c]   

    return sommaR - sommaC

if __name__ == "__main__":
    Matrice = genera(5)
    printMAT(Matrice)
    print(calcolaCarico(Matrice, 2 ,2))