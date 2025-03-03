# creo un dizionario dove all'interno dei 'valori' inserisco una lista
favorite_places: dict[str, str] = {
    "Uccio": ["Salisburg", "Vienna", "Hallstat"],
      "Uccia": ["Cawa", "Hallstat!", "Cogne"],
        "Piglet": ["Kennel", "BowlCat", "Sofa"],
}

# creo contatore per tenere traccia degli indici
cont = 1

# mezzo umb mezzo UI
print("-----------------------------------------------------------------------")
print("FAVORITE PLACES")
print("-----------------------------------------------------------------------")

# utilizzo ciclo FOR per iterare il dizionario
for name in favorite_places:

    # utilizzo secondo ciclo FOR per iterare la lista dentro il dizionario
    for list in range(len(favorite_places[name])):

        print(f"The {cont}° list of {name} is {favorite_places[name][list]}")
        cont += 1
    
    # resetto contatore alla fine di ogni 'valore'
    cont -= 3
    print("-----------------------------------------------------------------------")