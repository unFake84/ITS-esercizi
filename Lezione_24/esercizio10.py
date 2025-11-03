'''
Scrivi una funzione che prenda un dizionario e un valore,
e ritorni la prima chiave che corrisponde a quel valore,
o None se il valore non è presente.

For example:
Test 	                                                                Result

print(trova_chiave_per_valore({'a': 100, 'b': 200, 'c': 300}, 200))     b

print(trova_chiave_per_valore({'k1': 'v1', 'k2': 'v2'}, 'v3'))          None
'''

def trova_chiave_per_valore(dizionario: dict[str: int], valore: int) -> str:

    if valore in dizionario.values():
        chiave: str = str([k for k, v in dizionario.items() if v == valore][0])
        return chiave

    else:
        return None

if __name__ == "__main__":

    print(trova_chiave_per_valore({'a': 100, 'b': 200, 'c': 300}, 200))