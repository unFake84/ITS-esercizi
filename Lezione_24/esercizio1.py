'''
Scrivi una funzione che unisce due dizionari.
Se una chiave è presente in entrambi, somma i loro valori.
For example:
Test 	                                                Result

print(merge_dictionaries({'x': 5}, {'x': -5}))          {'x': 0}
'''

def merge_dictionaries(dict1: dict, dict2: dict) -> dict:

    dizio_uniti: dict = dict1

    for chiave, valore in dict2.items():

        if chiave in dict1:
            dizio_uniti[chiave] = dict1[chiave] + valore

        else:
            dizio_uniti[chiave] = valore
    
    return dizio_uniti

if __name__ == "__main__":

    print(merge_dictionaries({'x': 5, 'y': 2}, {'x': -5}))

    print(merge_dictionaries({'a': 1, 'b': 2}, {'b': 3, 'c': 4}))   # {'a': 1, 'b': 5, 'c': 4}  no
    print(merge_dictionaries({}, {'a': 10, 'b': 20}))               # {'a': 10, 'b': 20}        ok
    print(merge_dictionaries({'x': 5}, {'x': -5}))                  # {'x': 0}                  ok
    print(merge_dictionaries({}, {}))                               # {}                        ok
    print(merge_dictionaries({'a': 3}, {'b': 4}))                   # {'a': 3, 'b': 4}          no