'''
Scrivi una funzione che converta una lista di tuple (chiave, valore) in un dizionario.
Se la chiave è già presente, aggiungi il valore alla lista di valori già associata alla chiave.

Test 	                                                            Result

print(lista_a_dizionario([('a', 1), ('b', 2), ('a', 3)]))           {'a': [1, 3], 'b': [2]}

print(lista_a_dizionario([]))                                       {}
'''

def lista_a_dizionario(tuples: list[tuple]) -> dict[str:list[int]]:

    dizio_da_ritornare: dict[str, list[int]] = {}

    for tupla in tuples:

        if tupla[0] not in dizio_da_ritornare:
            dizio_da_ritornare[tupla[0]] = [tupla[1]]

        else:
            dizio_da_ritornare[tupla[0]].append(tupla[1])

    return dizio_da_ritornare

if __name__ == "__main__":

    print(lista_a_dizionario([('a', 1), ('b', 2), ('a', 3)]))