# importo ANY
from typing import Any

# 1 dizionario
domestic: dict[str, Any] = {
    "race": "cat",
      "name": "Pino",
        "features": "piglet",
          "legs": 4,
}

# 2 dizionario
domestic1: dict[str, Any] = {
    "race": "Human",
      "name": "Dioni",
        "features": "gamer",
          "legs": 3,
}

# 3 dizionario
domestic2: dict[str, Any] = {
    "race": "human",
      "name": "Fede",
        "features": "Uccia",
          "legs": 2
}

# creo lista e aggiungo i 3 dizionari al suo interno
pet: list[Any] = [domestic, domestic1, domestic2]

print("-----------------------------------------------------------------------")

# creo 4 liste vuote, una per ogni chiave 'key'
race: list[str] = []
name: list[str] = []
features: list[str] = []
legs: list[int] = []

# avvio ciclo FOR dentro la lista con i dizionari all'interno
for i in pet:
    
    # e aggiungo ad ogni variabile(KEY) ogni valore della lista 'pet'
    race.append(i['race'])
    name.append(i['name'])
    features.append(i['features'])
    legs.append(i['legs'])


# in questo modo posso fare frasi(print) con le variabili che fungono da CHIAVE utilizzando l'index [*] per trovare le VARIABILI dentro esse
print(f"From a distance it looks like a {features[0]}, but if you get closer you see that it is a {race[0]}, with {legs[0]} paws, it is called {name[0]}'the{features[0]} ")
print("-----------------------------------------------------------------------")
print(f"The {race[1]} {name[1]} according to him self, he is a {features[1]}!, often gets up in the morning with {legs[1]} legs.")
print("-----------------------------------------------------------------------")
print(f"The {race[2]} {name[2]}, called {name[2]} with {legs[2]} paws, she likes to cuddle her {race[0]} called the {name[0]}'the{features[0]}.")
print("-----------------------------------------------------------------------")