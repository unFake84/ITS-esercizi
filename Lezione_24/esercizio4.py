'''

Scrivi una funzione che, data una lista, ritorni un dictionary che mappa ogni elemento alla sua frequenza nella lista.

For example:
Test 	                                                Result

print(frequency_dict(['mela', 'banana', 'mela']))       {'mela': 2, 'banana': 1}
'''

def frequency_dict(elements: list) -> dict:

    dizio: dict[str, int] = {}
    for elemento in elements:

        if elemento not in dizio:
            dizio[elemento] = 1

        else:
            dizio[elemento] += 1

    return dizio