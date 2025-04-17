'''

Doppio ordinamento

Hai una lista di dizionari:

studenti = [
    {"nome": "Anna", "media": 28},
    {"nome": "Luca", "media": 25},
    {"nome": "Marco", "media": 30}
]

Ordina la lista in ordine decrescente di media usando una funzione lambda.

'''

from typing import Any

studenti: list[Any] = [

    {"nome": "Anna", "media": 28},
    {"nome": "Luca", "media": 25},
    {"nome": "Marco", "media": 30}
    
]

ordinata: list[Any] = sorted(studenti, key=lambda x: x["media"], reverse= True)
print(ordinata)