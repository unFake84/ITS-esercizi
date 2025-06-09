'''
Cifrario di Cesare
Il cifrario di Cesare è un antico metodo crittografico che rende alcune informazioni nascoste
a chi non possiede la chiave per decifrarle.
Immagina l’alfabeto come una lista ordinata di lettere (puoi importare la lista delle lettere
dell’alfabeto minuscole scrivendo from string import ascii_lowercase)
Ogni lettera ha una posizione in questa lista:
● a è 1
● b è 2
● j è 10
● e così via…
Il cifrario di Cesare nasconde l’informazione utilizzando una chiave, che è un numero intero
positivo, da sommare alla posizione della lettera originale: il risultato ottenuto corrisponde
alla posizione della lettera cifrata.
● a con key = 2 diventa c
Se la chiave porta oltre la fine dell’alfabeto, si ricomincia dal principio:
● a con key = 28 diventa c
Per decriptare (o “decifrare”) il messaggio, si applica la stessa procedura ma muovendosi
all’indietro nell’alfabeto. Devi fornire le funzioni:
caesar_cypher_encrypt(s, key)
caesar_cypher_decrypt(s, key)
dove:
● s è una stringa (lettera, parola, frase, ecc.).
● key è un numero intero positivo, la chiave del cifrario di Cesare.
La tua implementazione deve trasformare soltanto le lettere ASCII maiuscole e minuscole.
Caratteri speciali, numeri e lettere accentate non devono essere modificati.
Le funzioni non devono stampare nulla a schermo, ma restituire la stringa cifrata o
decifrata.
'''

from string import ascii_lowercase, ascii_uppercase

def caesar_cypher_encrypt(s: str, key: int) -> str:
    '''
    Il cifrario di Cesare nasconde l’informazione utilizzando una chiave, che è un numero intero
    positivo, da sommare alla posizione della lettera originale: il risultato ottenuto corrisponde
    alla posizione della lettera cifrata.
    '''

    if key <= 0:
        raise ValueError("The key must be positive!.")

    lower: str = ascii_lowercase
    upper: str = ascii_uppercase
    stringa_criptata: str = ""

    for char in s:
        if char in lower:
            indicelow: int = lower.index(char) + key
            stringa_criptata += lower[indicelow % 26]

        elif char in upper:
            indiceup: int = upper.index(char) + key
            stringa_criptata += upper[indiceup % 26]

        else:
            stringa_criptata += char

    return stringa_criptata

def caesar_cypher_decrypt(s, key) -> str:
    '''
    Per decriptare (o “decifrare”) il messaggio, si applica la stessa procedura ma muovendosi
    all’indietro nell’alfabeto.
    '''
    if key <= 0:
        raise ValueError("The key must be positive!.")

    lower: str = ascii_lowercase
    upper: str = ascii_uppercase
    stringa_decriptata: str = ""

    for char in s:
        if char in lower:
            indicelow: int = lower.index(char) - key
            stringa_decriptata += lower[indicelow % 26]

        elif char in upper:
            indiceup: int = upper.index(char) - key
            stringa_decriptata += upper[indiceup % 26]

        else:
            stringa_decriptata += char

    return stringa_decriptata

if __name__ == "__main__":

    print(caesar_cypher_encrypt("ahiaAh@1a!!#", 28))
    print(caesar_cypher_decrypt("cjkcCj@1c!!#", 28))






































    # res: str = ascii_lowercase
    # lista_alfabetica: list[str] = []

    # for lettera in res:
    #     lista_alfabetica.append(lettera)

    # lista_da_criptare: list[str] = []
    # for lettera2 in s:
    #     lista_da_criptare.append(lettera2)

    # lista_criptata: list[str] = []

    # for lettera3 in lista_da_criptare:
    #     for indice, lettera4 in enumerate(lista_alfabetica):

    #         if lettera4 == lettera3:
    #             indice += key
    #             lista_criptata.append(lista_alfabetica[indice %26])
    #             indice -= key



    #---------------------------------------------------------------
    # for indice, lettera3 in enumerate(lista_alfabetica, 1):
    #     print(indice, lettera3)
    #     if lettera3 in lista_da_criptare:
    #         indice += key
            
    #         lista_criptata.append(lista_alfabetica[indice -1])
    #         indice -= key
    #---------------------------------------------------------------