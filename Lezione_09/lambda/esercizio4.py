'''

Ordinamento con sorted()

Hai una lista di tuple studenti = [("Luca", 21), ("Anna", 19), ("Marco", 22)].
Ordina la lista in base all’età (secondo elemento) usando sorted() e lambda.

'''

from typing import Any

studenti: list[Any] = [("Luca", 21), ("Anna", 19), ("Marco", 22)]

ordinata: list[Any] = sorted(studenti, key=lambda x: x[1])

print(ordinata)