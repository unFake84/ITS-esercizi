# importo ANY
from typing import Any

# creo dizionario con all'interno altri DIZIONARI, la chiave è la citta ed i valori altre caratteristiche della città(chiave)
cities: dict[str, Any] = {
    "Rome": {
        "country": "Italy",
          "population": "2.752.000 approx.",
            "fact": "chaotic!"
              },
      "Salisburg": {
          "country": "Austria",
            "population": 154.211,
              "fact": "home of music"
                },
        "Home": {
            "country": "Uccland",
              "population": 3,
                "fact": "homy sweety homie"
                  }
}

# contatore per indice
i = 1

print("-----------------------------------------------------------------------")
# ciclo FOR per iterare 2 elementi dentro il dizionario
for key, dict in cities.items():

    print(f"{i}){key}:\n")
    i += 1

    # utilizo altro FOR per iterare il dizionario anidato
    for under_key, values in dict.items():

        print(f"{under_key.title()} = {values}")
        
    print()    
    print(dict)
    print("-----------------------------------------------------------------------")