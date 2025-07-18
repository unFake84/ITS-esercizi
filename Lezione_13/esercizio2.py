'''
Si supponga di voler calcolare l'ammontare del denaro depositato su
un conto bancario ad interesse composto.
Se m è la somma depositata sul conto,
la somma disponibile alla fine del mese sarà 1.005 volte m.
Scrivere una funzione ricorsiva compoundInterest che
calcoli la somma presente sul conto dopo
t mesi data una somma di partenza m.
'''

def compoundInterest( m: float, t: int,r: float = 1.005 ) -> float | None:

    '''
    m: Stipendio
    t: mesi
    r: rateo=1.005 Default
    '''

    if m < 0 or t < 0:
        print( "\nInsert valid input" )
        return None

    elif t == 0:
        return m

    else:
        return compoundInterest( m, t -1 ) * r

if __name__ == "__main__":

    result: float | None = compoundInterest( 5224, 5 )

    if result is not None:
        print( f"{ round( result ) } €" )

    else:
        print( "\nErrore\n" )