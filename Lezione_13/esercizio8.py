'''
Si scriva una funzione ricorsiva vowelsCounter che conti il numero di vocali in una stringa.

Suggerimento: ogni volta che si effettua una chiamata ricorsiva,
si utilizzi lo slicing per ottenere una nuova stringa formata dai caratteri compresi tra
il secondo e l'ultimo della stringa originale.
L'ultima chiamata ricorsiva avverrà quando la stringa non contiene caratteri.
'''

def vowelsCounter( s: str ) -> int | None:

    if not isinstance( s, str ):
        print( f"{ s } <- Not a String" )
        return None

    elif s == "":
        return 0

    elif s[ 0 ].lower() in ( "a", "e", "i", "o", "u" ):
        return 1 + vowelsCounter( s[ 1: ] )

    else:
        return vowelsCounter( s[ 1: ] )

if __name__ == "__main__":
    print( vowelsCounter( "Stringa" ) )