# dato che i dizionari hanno anche valori INT importo ANY
from typing import Any

# creo dizionario
info: dict[str, Any] = {"first_name": "Dioni", "last_name": "Manon", "age": 40, "city": "Rome"}

print("-----------------------------------------------------------------------")

# utilizzo ciclo FOR con 2 iteratori per mostrare(print) la chiave(KEYS) e i valori(VALUES).
for keys, values in info.items():

    print(keys, values)
    
print("-----------------------------------------------------------------------")

# salvo ogni elemento in 'first_name'(Dioni) dentro una variabile(value_key1)
value_key1: list[str] = info["first_name"]
print(value_key1)
print("-----------------------------------------------------------------------")

# stessa cosa per il cognome
value_key2: list[str] = info["last_name"]
print(value_key2)
print("-----------------------------------------------------------------------")

# e per l'età
value_key3: list[Any] = info["age"]
print(value_key3)
print("-----------------------------------------------------------------------")

# o si può stampare anche senza creare una 'variabile'
print(info["age"])
print("-----------------------------------------------------------------------")

print(info["city"])
print("-----------------------------------------------------------------------")

# avendo salvato i 'valori' in una variabile, posso "evocarli" in una frase formattata 'f'
print(f"My first name is {value_key1} and my last name is {value_key2}")
print("-----------------------------------------------------------------------")

# manca una variabile per la città
value_key4: list[str] = info["city"]
# così posso utilizzarla in quest'altra frase
print(f"I ve {value_key3} years old and im living in {value_key4}")
print("-----------------------------------------------------------------------")