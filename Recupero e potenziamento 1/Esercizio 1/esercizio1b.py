'''
Il Massimo Comun Divisore di due o più numeri è il più grande divisore comune dei numeri considerati.
Ad esempio, se consideriamo i numeri 12 e 18, il loro Massimo Comun Divisore è mcd(12,18) = 6.
Infatti,

    i divisori di 12 sono:

        12 = 1, 2, 3, 4, 6, 12

    i divisori di 18 sono:

        18 = 1, 2, 3, 6, 9, 18

il divisore più grande che 12 e 18 hanno in comune è 6.

Scrivere nel file frazione.py una funzione  mcd(int x, int y) per il calcolo del Massimo Comune Divisore.
 
Nel caso in cui esista un Massimo Comun Divisore tra i numeri x e y,
allora la funzione deve ritornarlo come numero intero.
Altrimenti, nel caso in cui non esista un massimo Comun Divisore tra i numeri x e y,
la funzione deve ritornare 1.
   

Suggerimento: per semplicità, per implementare la funzione richiesta,
trovare una soluzione che generalizzi l'esempio proposto e che tenga conto dei casi x > y e x < y
per evitare di replicare righe di codice.
'''

def mcd(x: int, y: int) -> int:

    numero_maggiore: int = min(x, y)

    while numero_maggiore >= 1:

        if x%numero_maggiore == 0 and y%numero_maggiore == 0:
            return numero_maggiore
        numero_maggiore -= 1

    else:
        return 1

if __name__== "__main__":

    print(mcd(12, 18))





















        # if x%numero_maggiore == 0:
        #     j = x // numero_maggiore
        #     numeri_x.append(j)
        #     print(j, "\n")

        # if y%numero_maggiore == 0:
        #     k = y // numero_maggiore
        #     numeri_y.append(k)
        #     print(k)

        # if j == k:
        #     mcd += j
        #     print(mcd, "mcd")

        # numero_maggiore -= 1

    # print(numeri_x, numeri_y)