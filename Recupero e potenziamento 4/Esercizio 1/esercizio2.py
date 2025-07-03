'''
Elaborare uno schema che consenta di stampare in output
in maniera ricorsiva gli elementi di una lista in ordine inverso.

Una volta elaborato lo schema, appena consentitovi dal docente,
scrivere una funzione ricorsiva in Python, chiamata printListBackward()
che stampi in output gli elementi di una lista in ordine inverso, sfruttando la ricorsione.
Infine, scrivere un codice driver che,
date le seguenti liste,
stampi ogni lista in ordine inverso sfruttando la funzione ricorsiva implementata.

    lista1: 1, 2, 3, 4, 5

    lista2: "Armatura", "Bravura", "Cane", "Diamante", "Elefante", "Furfante"
'''

def printListBackward(lista: list) -> list[int]:

    lista_inv: list[int] = []

    if lista == []:
        return 
    
    print(lista[-1])
    lista_inv.append(lista[-1])
    lista.pop()
    printListBackward(lista)

if __name__ == "__main__":

    lista1: list[int] = [1, 2, 3, 4, 5]
    lista2: list[str] = ["Armatura", "Bravura", "Cane", "Diamante", "Elefante", "Furfante"]

    print(printListBackward(lista1))
    print(printListBackward(lista2))