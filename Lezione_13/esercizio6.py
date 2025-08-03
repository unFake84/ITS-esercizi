'''
Una produttoria è definita come il prodotto di un certo numero n di fattori,
con n intero positivo. Sia Pi una produttoria definita come segue:
Pi = (0 + 2) * (1 + 2) * (2 + 2) * ... * (n + 2).  

Calcolare il valore della produttoria Pi se n = 7.
'''

def produttoria( n: int ) -> int | None:

    if n < 0 or not isinstance( n, int ):
        print( f"{ n } <- Not a integer" )
        return None

    elif n == 0:
        return 2

    else:
        return ( n + 2 ) * produttoria( n - 1 )

if __name__ == "__main__":
    print( produttoria( 7 ) )