'''
Scrivi una funzione che moltiplica tutti i numeri interi di una lista che sono minori di un
dato valore intero definito threshold.
'''

lista_di_numeri: list[int] = [1, 2, 3, 4, 5, 6, 20, 46]# 7, 8, 9, 10]

def moltiplica(lista: list[int], threshold: int) -> int:
    prodotto: int = 1

    for controllo in lista:
        if controllo < threshold:
            prodotto *= controllo

    return prodotto

print(moltiplica(lista_di_numeri, 10))

#FATTORIALE
# n! -> n*n-1*n-2*.....*2

def fattoriale(n):
    # if n == 1:
    #     return 1
    
    # return n*fattoriale(n-1)
    return fattoriale(n-1) * n if n != 1 else 1