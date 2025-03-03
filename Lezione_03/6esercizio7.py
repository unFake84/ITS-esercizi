# importo ANY
from typing import Any

# 1 dizionario
info: dict[str, Any] = {
    "first_name": "Dioni",
      "last_name": "Manon",
        "age": 40,
          "city": "Rome",
}

# 2 dizionario
info2: dict[str, Any] = {
    "first_name": "Pino",
      "last_name": "Maial",
        "age": 9,
          "city": "Myhouse"
}

# 3 dizionario
info3: dict[str, Any] = {
    "first_name": "Fede",
      "last_name": "Uccia",
        "age": 38,
          "city": "Rome",
}

# creo LISTA vuota
people: list[Any] = []

# aggiungo i dizionari dentro la lista 'people'
people.append(info)
people.append(info2)
people.append(info3)

print("-----------------------------------------------------------------------")

# ciclo FOR per iterare la lista 'people'
for i in people:

    # creo una lista con stringa per memorizzare tutti i 'valori' dentro una frase formattata.
    frase: list[Any] = f"{i['first_name']} ha {i['age']} anni e vive a {i['city']}."
    print(frase)

print("-----------------------------------------------------------------------")