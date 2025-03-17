# creo dizionario cercando di rispettare il PEP8
glossario: dict[str, str] = {
                    "if": "if true enters the instruction block",
                        "while": "allows a loop to be started, thanks to the use of a counter",
                            "for": "allows automatic iteration, without the use of a counter",
                                "Any": "allows any type of data to be inserted in lists, sets and dictionaries ",
                                    ".pop()": "allows the removal of elements in lists, sets and dictionaries",
}
# utilizzo un contatore per tenere traccia dell'indice
i = 1

# umb
print("-----------------------------------------------------------------------")

# stesso sistema per ottenere i valori dentro un dizionario ad ogni iterazione di 'key', 'value'
for key, value in glossario.items():

    print(f"{i}) {key}:\n{value}")
    print("-----------------------------------------------------------------------")
    # aggiorno contatore
    i += 1