favorite_places: dict[str, str] = {
    "Dioni": ["Salisburg", "Vienna", "Hallstat"],
      "Uccia": ["Cawa", "Hallstat!", "Cogne"],
        "Piglet": ["Kennel", "BowlCat", "Sofa"]
}

cont = 1

print("-----------------------------------------------------------------------")
print("FAVORITE PLACES")
print("-----------------------------------------------------------------------")

for name in favorite_places:

    for list in range(len(favorite_places[name])):

        print(f"The {cont}° list of {name} is {favorite_places[name][list]}")
        cont += 1
    
    cont -= 3
    print("-----------------------------------------------------------------------")