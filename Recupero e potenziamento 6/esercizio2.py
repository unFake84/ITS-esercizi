'''

Scrivere un programma in Python che legga dall’utente una serie di nomi di persona (stringhe).
L'inserimento dei nomi deve terminare quando l’utente inserisce un nome già inserito in precedenza,
oppure sono stati inseriti 30 nomi distinti.

Inoltre, si deve porre il vincolo che ciascun nome sia una stringa di lunghezza
inferiore a 20 caratteri e che non venga inserita una stringa vuota.

Al termine dell'inserimento, il programma deve:
- stampare quanti nomi sono stati inseriti in totale;
- stampare il nome più lungo tra quelli inseriti;
- stampare la lunghezza del nome più lungo.

Se ci sono più nomi con la stessa lunghezza massima, puoi scegliere uno qualsiasi tra quelli più lunghi.

Esempio:
Inserisci un nome: Dora
Inserisci un nome: Marcella
Inserisci un nome: Teresa
Inserisci un nome: Valentina
Inserisci un nome: Dora

Hai inserito 4 nomi distinti.
Il più lungo è Valentina con 9 caratteri.

'''

def checkNome( nome:str ) -> bool:

    if not isinstance ( nome,str )\
    or nome.strip() == ""\
    or len( nome ) >= 20\
    or len( nome ) < 2:
        return False

    try:
        eUnNum: float = float( nome.strip() )
        return False

    except ValueError:
        ver_approf: str = nome

        return _validName( ver_approf )

def _validName( valid:str, numbers:str = "0123456789" ) -> bool:

    if valid == "":
        return True

    if valid[ 0 ] in numbers:
        return False

    else:
        return _validName( valid[ 1: ] )

if __name__ == "__main__":

    setDiNomi: set[ str ] = set()
    slots: int = 0
    user: str = ""
    nomeProvv: str = ""
    check: bool = False
    nomePiuLungo: str = ""
    conQuantiCaratt: int = 0

    while slots < 30:

        print( """
Inserire fino ad un massimo di 30 nomi.
Ripetere un nome già inserito in precedenza per chiudere il programma.
Al termine verrà mostrato quanti nomi sono stati inseriti (senza duplicati), e
da quanti caratteri è composto il nome più lungo inserito.""" if len( setDiNomi ) == 0 else "-" * 30 )
        print( f"\nUltimo inserito: { nomeProvv if setDiNomi else '- >' }" )
        print( "Lista di nomi: ", * setDiNomi if setDiNomi else "->" )

        user = input( f"\nInserisci { slots + 1 }/30° nome: " )
        check = checkNome( user )
        
        if check:
            nomeProvv = user

            if user not in setDiNomi:
                setDiNomi.add( user )

                if len( user ) >= len( nomePiuLungo ):
                    nomePiuLungo = user
                    conQuantiCaratt = len( nomePiuLungo )

            else:
                break

            slots += 1

    print( "\nFine Programma" )
    print( f"Hai inserito { len( setDiNomi ) } nomi distinti." )
    print( f"Il più lungo è { nomePiuLungo } con { conQuantiCaratt } caratteri." )