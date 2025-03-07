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

dizionario: dict[str, str] = {"name":user, "animal_type": animal_type, "habitat": user2}

match animal_type:

    case "mammiferi":

        print(f"{user.upper()} appartiene alla categoria dei Mammiferi!")

        match user2.lower():
             
            case "terra":
                
                match user:

                    case "cane" | "gatto" | "cavallo" | "elefante" | "leone":

                        print(f"{user.title()} è un mammifero che vive sulla terra!.")
                    
                    case "balena" | "delfino":

                        print(f"{user.title()} è si un mammifero ma vive sull'acqua!.")

            case "acqua":

                match user:
                    
                    case "balena" | "delfino":

                        print(f"{user.title()} è un mammifero che vive sull'acqua!.")

                    case "cane" | "gatto" | "cavallo" | "elefante" | "leone":

                        print(f"{user.title()} è si un mammifero ma vive sulla terra!.")

            case _:

                print(f"Non ho mai visto l'animale {user.title()} vivere in tale ambiente!.")

    case "rettili":

        print(f"{user.upper()} appartiene alla categoria dei Rettili!")

        match user2.lower():

            case "terra":

                match user:

                    case "lucertola" | "serpente" | "tartaruga" | "coccodrillo":

                        print(f"{user.title()} è un rettile che può anche vivere sulla terra!.")
                    
            case "acqua":

                match user:

                    case "serpente" | "tartaruga" | "coccodrillo":

                        print(f"{user.title()} è un rettile che può stare anche nell'acqua!.")
                    
                    case _:

                        print(f"La {user.title()} non ci vive ma può nuotarci!.")

            case _:

                print(f"L'animale {user.title()} puo solamente respirarla l'aria!.")

    case "uccelli":

        print(f"{user.upper()} appartiene alla categoria dei Rettili!.")

        match user2.lower():

            case "terra":

                match user:

                    case "gallina" | "tacchino":

                        print(f"{user.upper()}è si un uccello ma non può volare!.")

                    case _:

                        print(f"{user.upper()} e sì! ma il suo habitat ideale è l'aria!.")

            case "aria":

                match user:
                    
                    case "gallina" | "tacchino":

                        print(f"{user.upper()} è si un uccello ma non può volare!.")

                    case _:

                        print(f"L' animale {user.upper()} ha il suo habitat nell'aria!.")

    case "pesci":

        print(f"{user.upper()} appartiene alla categoria dei Pesci!.")

        match user2.lower():

            case "terra":

                match user:

                    case "squalo"| "trota" | "salmone" | "carpa":

                        print(f"L'animale {user.upper()} non può vivere sulla terra!.")

            case "aria":

                match user:

                    case "squalo"| "trota" | "salmone" | "carpa":

                        print(f"L'animale {user.upper()} non può vivere sull'aria!.")

            case _:

                print(f"L' animale {user.upper()} ha il suo habitat nell'acqua!.")