'''
Frequenza di Parole Uniche con Normalizzazione
Scrivi una funzione che prende una stringa di testo (contenente eventualmente
punteggiatura, lettere maiuscole e minuscole, spazi bianchi) e restituisce un dizionario che
associa a ciascuna parola unica (in minuscolo, privata della punteggiatura iniziale/finale) il
numero di occorrenze.

        Requisiti:

● Suddividi l’input sugli spazi bianchi per ottenere i token.
● Normalizza ogni token:
        1. Converti in minuscolo.
        2. Rimuovi la punteggiatura iniziale e finale (ad esempio usando str.strip()
        con un insieme di caratteri di punteggiatura).
● Ignora qualsiasi token che diventa stringa vuota dopo la rimozione della
punteggiatura.
● Restituisci un dict dove le chiavi sono parole normalizzate e i valori sono conteggi
interi.

Esempio:
text = "Hello, world! Hello... PYTHON? world."
output = count_unique_words(text)
● # output == {'hello': 2, 'world': 2, 'python': 1}
'''

from string import ascii_lowercase

def count_unique_words(text: str) -> dict[str, int]:

    a__z: str = ascii_lowercase
    frase: str = ""
    lista_di_parole: list[str] = []
    dizio: dict[str, int] = {}

    for indice in text.lower():

        if indice in a__z:
            frase += indice

        if indice not in a__z:
            lista_di_parole.append(frase)
            frase = ""

        if "" in lista_di_parole:
            lista_di_parole.remove("")

    for parola in lista_di_parole:

        if parola not in dizio:
            dizio[parola] = 1

        elif parola in dizio:
            dizio[parola] += 1

    return dizio

print(count_unique_words("  ciao come stai? CIao! tutto bene  ciao ciaooo !##@ @ @ ciao tutto ciao @   beLL/aaa   ahaha aaa bene! 23ò12à3ò"))
print(count_unique_words("Hello, world! Hello... PYTHON? world."))




























    # minuscolo: str = text.lower().strip()
    # lista_di_parole: list[str] = []
    # car_speciali = string.punctuation
    # frase: str = ""
    # dizio: dict[str, int] = {}
    # contatore: int = 1

    # for i in minuscolo:

    #     if i == " ":
    #         lista_di_parole.append(frase.strip())
    #         frase = ""

    #     if i not in car_speciali:
    #         frase += i

    # lista_di_parole.append(frase.strip())

    # for key in lista_di_parole:

    #     if key in dizio:
    #         dizio[key] = contatore + 1

    #     if key not in dizio:
    #         dizio[key] = contatore 

    # print(minuscolo, "\n",lista_di_parole, "\n", dizio)