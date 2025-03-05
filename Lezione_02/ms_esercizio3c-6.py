mammiferi: list[str] = ["cane", "gatto", "cavallo", "elefante", "leone", "balena", "delfino"]
rettili: list[str] = ["serpente", "lucertola", "tartaruga", "coccodrillo"]
uccelli: list[str] = ["aquila", "pappagallo", "gufo", "falco", "cigno", "anatra", "gallina", "tacchino"]
pesci: list[str] = ["squalo", "trota", "salmone", "carpa"]

# generale: list[str] = []
# generale.extend(mammiferi + rettili + uccelli + pesci)

user: str = (input("Inserire un'animale: "))

match user.lower():

    case user if user in mammiferi:

        print(f"{user.upper()} appartiene alla categoria dei Mammiferi")

    case user if user in rettili:

        print(f"{user.upper()} appartiene alla categoria dei Rettili")


    case user if user in uccelli:

        print(f"{user.upper()} appartiene alla categoria dei Uccelli")

    case user if user in pesci:

        print(f"{user.upper()} appartiene alla categoria dei Pesci")

    case _:

        print(f"Non so dire in quale categoria classificare l'animale '{user.upper()}'")

animal_type: str

if user in mammiferi or rettili or uccelli or pesci:

    if user in mammiferi:

        animal_type = "mammiferi"

    elif user in rettili:

        animal_type = "rettili"

    elif user in uccelli:

        animal_type = "uccelli"

    elif user in pesci:

        animal_type = "pesci"

    else:

        animal_type = "unknow"

habitat: list[str] = ["terra", "aria", "acqua"]


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