'''
Scrivi una funzione che prenda una lista di numeri e ritorni un dizionario che
classifichi i numeri in liste separate per numeri positivi e negativi.
'''

lista_di_numeri: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -1, -2 , -3, -4, -5]

def ordina(lista: list[int]) -> dict:
    dizio: dict[str, list] = {"Positivi": [], "Negativi": []}
    for numero in lista:
        if numero >= 0:
            dizio["Positivi"].append(numero)

        elif numero < 0:
            dizio["Negativi"].append(numero)

    return dizio

print(ordina(lista_di_numeri))