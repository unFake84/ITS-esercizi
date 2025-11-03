'''
Scrivi una funzione che prende una lista di numeri e
ritorna un dizionario che classifica i numeri in liste separate per numeri pari e dispari.

For example:
Test 	                                            Result

print(classifica_numeri([1, 2, 3, 4, 5, 6]))        {'pari': [2, 4, 6], 'dispari': [1, 3, 5]}

print(classifica_numeri([]))                        {'pari': [], 'dispari': []}
'''

def classifica_numeri(lista: int) -> dict[str:list[int]]:

    lista_para: list[int] = []
    lista_dispara: list[int] = []

    for num in lista:

        if num%2 == 0:
            lista_para.append(num)

        else:
            lista_dispara.append(num)

    return {'pari': lista_para, 'dispari': lista_dispara}