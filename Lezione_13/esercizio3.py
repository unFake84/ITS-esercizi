'''
Il fattoriale di un intero non negativo n, scritto n!, è il prodotto

n * (n-1) * (n-2) * ... * 1

con 1! uguale a 1 e 0! definito come 1.
Si scriva una funzione ricorsiva recursiveFactorial che dato un numero n calcoli n!.
'''

def recursiveFactorial( n: int ) -> int | None:

    if n < 0 or not isinstance( n, int ):
        print("Non valido!")
        return None

    elif n == 0 or n == 1:
        return 1

    else:
        return n * recursiveFactorial( n - 1 )

if __name__ == "__main__":

    result: int | None = recursiveFactorial( 5 )
    print( f"Il risulato è : { result if result is not None else 'Errore' }" )