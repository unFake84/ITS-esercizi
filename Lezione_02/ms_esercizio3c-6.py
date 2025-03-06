mammiferi: list[str] = ["cane", "gatto", "cavallo", "elefante", "leone", "balena", "delfino"]
rettili: list[str] = ["serpente", "lucertola", "tartaruga", "coccodrillo"]
uccelli: list[str] = ["aquila", "pappagallo", "gufo", "falco", "cigno", "anatra", "gallina", "tacchino"]
pesci: list[str] = ["squalo", "trota", "salmone", "carpa"]

user: str = (input("Inserire un'animale: "))

user2: str = (input("Inserire l'habitat in cui vive l'animale: "))

animal_type: str

if user in mammiferi or user in rettili or user in uccelli or user in pesci:

    if user in mammiferi:

        animal_type = "mammiferi"

    elif user in rettili:

        animal_type = "rettili"

    elif user in uccelli:

        animal_type = "uccelli"

    else:

            animal_type = "pesci"

else:

    animal_type = "unknow"

habitat: list[str] = ["terra", "aria", "acqua"]

dizionario: dict[str, int] = {}
dizionario[user] = {"animal_type": animal_type, "habitat": user2}

match user.lower():

    case user if user in mammiferi:

        print(f"{user.upper()} appartiene alla categoria dei Mammiferi")

        match user2.lower():
             
            case user2 if user2 == "terra":
                
                if user == "delfino" or user == "balena":

                    print(f"{user.title()} è sì un mammifero ma vive prevalentemente nell'acqua!")

                #else:
                    
                    #print(f"L'animale {user} è uno dei {dizionario[user]['animal_type']} che può vivere sulla {dizionario[user]['habitat']}!")

            case user2 if user2 == "acqua":

                  print(f"L'animale {user} appartiene ai {dizionario[user]['animal_type']}, il suo habitat è l'{dizionario[user]['habitat']}")

            case user2 if user2 == "aria":
                  
                  print(f"L'animale {user} appartiene ai {animal_type.upper()}, non può vivere qui, se non per saltare!")

            case _:
                  print(f"L'animale {user} è dei {animal_type.upper()}, non vive qui, forse l'hai sognato o letto in un libro fantasy! :)")
        

    case user if user in rettili:

        print(f"{user.upper()} appartiene alla categoria dei Rettili")


    case user if user in uccelli:

        print(f"{user.upper()} appartiene alla categoria dei Uccelli")

    case user if user in pesci:

        print(f"{user.upper()} appartiene alla categoria dei Pesci")

    case _:

        print(f"Non so dire in quale categoria classificare l'animale '{user.upper()}'")

# for _ in mammiferi, rettili, uccelli, pesci:

#     dizionario["nome"] = mammiferi + rettili + pesci
#     dizionario["habitat"] = habitat
#     dizionario["animal_type"] = animal_type

#print(dizionario)

# dizionario: dict[str, str] = {
#     "mammiferi": {"mammiferi": "habitat_mammiferi"},
#         "rettili": {"rettili": "habitat_rettili"},
#             "uccelli": {"uccelli": "habitat_uccelli"},
#                 "pesci": {"pesci": "habitat_pesci"},
# }

# print(animal_type)
# print(user)
# print(dizionario)
# print(generale)