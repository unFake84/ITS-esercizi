'''
Scrivi una funzione che accetti un dizionario di prodotti con i relativi prezzi e
restituisca un nuovo dizionario con solo i prodotti che hanno un prezzo inferiore a 50, ma
con i prezzi aumentati del 10% e arrotondati a due cifre decimali.
'''

dizio_di_oggetti: dict[str, float] = {"Penna": 2, "Libro": 55, "Astuccio": 10}

def aumenta(dizio: dict[str, float]) -> dict:
    dizio_aumentato: dict[str, float] = {}

    for oggetto, prezzo in dizio.items():
        if prezzo < 50:
            prezzo_aumentato: float = prezzo * 1.10
            dizio_aumentato[oggetto] = round(prezzo_aumentato, 2)

    return dizio_aumentato

print(aumenta(dizio_di_oggetti))