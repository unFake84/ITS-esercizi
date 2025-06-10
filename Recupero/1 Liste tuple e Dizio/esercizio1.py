'''Liste, Tuple e Dizionari
1) Scrivi una funzione che converta una lista di tuple (chiave, valore) in un dizionario. Se
la chiave è già presente, somma il valore al valore già associato alla chiave.
'''

# from typing import Any

# lista_di_tuple: tuple[Any, ...] = (("a", 1), ("b", 2), ("c", 3), ("d", 4), ("e", 5), ("b", 2))
# dizio: dict[Any, Any] = {}
# for key, value in enumerate(lista_di_tuple):
#     dizio[key] = value
#     print(value)
# print(dizio)

from typing import Any

lista_tuple: list[tuple] = [(1, "a"), (2, "b"), (3, "c")]

def convert(lista: list[tuple]) -> dict:
    dizio: dict[Any, Any] = {}

    for element in lista:
        key, value = element[0], element[1]

        if key in dizio:
            dizio[key] += value

        else:
            dizio[key] = value

    return dizio

def convert2(lista: list[tuple]) -> dict:
    dizio: dict[Any, Any] = {}

    for key, value in lista:
        if key in dizio:
            dizio[key] += value

        else:
            dizio[key] = value

    return dizio

print(convert(lista_tuple))