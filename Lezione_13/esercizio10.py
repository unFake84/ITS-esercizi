'''
Si scriva una funzione ricorsiva charDuplicator che
consenta di duplicare ogni carattere in una stringa e
restituisca il risultato sotto forma di una nuova stringa.

Ad esempio, se la stringa "libro" viene data in input a charDuplicator,
la funzione ricorsiva deve produrre in output la stringa "lliibbrroo".
'''

def charDuplicator( s: str ) -> str | None:

    if not isinstance( s, str ):
        print( f"{ s } <- Not a String" )
        return None

    return ( s[ 0 ] * 2 ) + charDuplicator( s[ 1: ] ) if s != "" else ""

if __name__ == "__main__":

    print( charDuplicator( "libro" ) )