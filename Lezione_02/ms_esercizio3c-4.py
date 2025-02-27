mammiferi: list[str] = ["cane", "gatto", "cavallo", "elefante", "leone"]
rettili: list[str] = ["serpente", "lucertola", "tartaruga", "coccodrillo"]
uccelli: list[str] = ["aquila", "pappagallo", "gufo", "carpa"]
pesci: list[str] = ["squalo", "trota", "salmone", "carpa"]

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

        print(f"Non so dire in quale categoria classificare l'animale {user.upper()}")