'''
Esercizio 1.

In biologia molecolare, le molecole di DNA possono essere viste come stringhe sull’alfabeto dei nucleotidi
A = adenina, C = citosina, G =guanina, T = timina.

Ad esempio: DNA: CAGCTGATCGATGCTAGCCTG.

Scrivere un programma in linguaggio Python che legge dall’utente due stringhe s1 e s2 corripondenti a frammenti di
DNA e verifica se s2 puo' essere sovrapposta su s1 in modo che una parte iniziale (prefisso) di s2 coincida con
una parte finale (suffisso) di s1.

Il programma dovra' dare la lunghezza della massima sovrapposizione (0 se non si possono sovrapporre).

Ad esempio, se l’utente ha inserito:
s1= CAGCTGATCGATGCTAGCCTG
s2= AGCCTGTTGCACCTAGA

Le due stringhe si sovrappongono come segue:
CAGCTGATCGATGCTAGCCTG
               AGCCTGTTGCACCTAGA

Il programma dovra' quindi stampare in output:

    le stringhe sovrapposte come nell'esempio.

    La massima lunghezza di sovrapposizione e' 6.


NOTA1:
il programma dovra' anche verificare la correttezza dell’input,
ovvero le stringhe inserite dall’utente devono essere effettivamente frammenti di DNA.
Suggerimento: scrivere una funzione isDNA() che, data in input una sequenza,
restituisca True se la sequenza passata è una valida sequenza del DNA formata dai soli caratteri
A, C, G o T, e che restituisca False altrimenti.
Può essere utile usare una regex.

Nota2: trovare una soluzione che eviti di scrivere codice replicato per inizializzare le sequenze s1 e s2.

Infine, verificare le seguenti coppie di frammenti di DNA:
- s1= TTGACCAGGTCA
- s2= AACCGGTTAA
La massima lunghezza è 1

- s1= GGTACCGTGA
- s2= CGTGAACCTT
La massima lunghezza è 5

- s1= AAGCTTACG
- s2= ACGTTCGA
La massima lunghezza è 3

- s1= TTACGAGTACGCTAGT
- s2= ACGCTAGTCCGA
La massima lunghezza è 8
 
- s1= AGCTAACG
- s2= AACGTTCGA
La massima lunghezza è 4
 
- s1= AAAA
- s2= AAAA
La massima lunghezza è 4
 
- s1= ACGT
- s2= ATGC
La massima lunghezza è 0

'''

def isDNA( seq:str ) -> bool:

    if not isinstance( seq, str ):
        return False

    for dna in seq:

        if dna not in ( "A", "C", "G", "T" ):
            return False

    return True

def fusionDNA( s1:str , s2:str ) -> str:

    slicer_s1: int = -1
    slicer_s2: int = 1
    max_length: int = 0

    for _ in s1:
        if s1[ slicer_s1: ] == s2[ :slicer_s2 ]:
            max_length = slicer_s2

        slicer_s1 -= 1
        slicer_s2 += 1

    final_string: str = f"\n{ s1[ :slicer_s1 ] }{ s1[ slicer_s1: ] }\n"\
                        f"{' ' * len( s1[ max_length: ] ) }"\
                        f"{ s2[ slicer_s2: ] }{ s2[ :slicer_s2 ] }\n"\
                        f"La massima lunghezza di sovrapposizione è: { max_length }.\n"

    return final_string

def testDNA() -> None:

    # TEST A
    dna_1a: str = "TTGACCAGGTCA"
    dna_2a: str = "AACCGGTTAA"

    # TEST B
    dna_1b: str = "GGTACCGTGA"
    dna_2b: str = "CGTGAACCTT"

    # TEST C
    dna_1c: str = "AAGCTTACG"
    dna_2c: str = "ACGTTCGA"

    # TEST D
    dna_1d: str = "TTACGAGTACGCTAGT"
    dna_2d: str = "ACGCTAGTCCGA"

    # TEST E
    dna_1e: str = "AGCTAACG"
    dna_2e: str = "AACGTTCGA"

    # TEST F
    dna_1f: str = "AAAA"
    dna_2f: str = "AAAA"

    # TEST G
    dna_1g: str = "ACGT"
    dna_2g: str = "ATGC"

    # TESTS EXEC
    print( fusionDNA( dna_1a, dna_2a ) , "-" * 50 ) # A
    print( fusionDNA( dna_1b, dna_2b ) , "-" * 50 ) # B
    print( fusionDNA( dna_1c, dna_2c ) , "-" * 50 ) # C
    print( fusionDNA( dna_1d, dna_2d ) , "-" * 50 ) # D
    print( fusionDNA( dna_1e, dna_2e ) , "-" * 50 ) # E
    print( fusionDNA( dna_1f, dna_2f ) , "-" * 50 ) # F
    print( fusionDNA( dna_1g, dna_2g ) , "-" * 50 ) # G

def dnaMain() -> None:
    user: str = ""
    sequences: list[ str ] = []
    checker: bool = False

    print( "Enter two valid DNA sequences (consisting only of A, C, G, T)." )

    while True:

        user = input( f"Insert { 'first' if len( sequences ) == 0 else 'second' } fragment of Dna: " ).upper()
        checker = isDNA( user )

        if not checker:
            print( "The portion of fragment is incorrect, please try again." )
            continue

        if checker:
            sequences.append( user )

            if len( sequences ) == 2:
                break

    print( fusionDNA( sequences[ 0 ], sequences[ 1 ] ) )
        

if __name__ == "__main__":

    #        val1 if cond1 else val2 if cond2 else val3

    choice: str = input( ">> 'test' or 'run' program?: " ).lower().strip()
    testDNA() if choice == 'test' else dnaMain() if choice == 'run' else print( "Choice not valid." )
    print( "Closing." )