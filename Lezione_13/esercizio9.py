'''
Si scriva una funzione ricorsiva vowelRemover che
elimini tutte le vocali da una stringa data e restituisca sotto forma di
una nuova stringa la stringa originale ma senza le vocali.

Suggerimento: utilizzare l'operatore + per
realizzare la concatenazione di stringhe al fine di costruire la stringa da restituire.
'''

def vowelRemover( s: str ) -> str | None:

    if not isinstance( s, str ):
        print( f"{ s } <- Not a String" )
        return None

    if s == "":
        return ""

    elif s[ 0 ].lower() not in ( "a", "e", "i", "o", "u" ):
        return s[ 0 ] + vowelRemover( s[ 1: ] )

    else:
        return vowelRemover( s[ 1: ] )

if __name__ == "__main__":

    print( vowelRemover( "Stringa" ) )