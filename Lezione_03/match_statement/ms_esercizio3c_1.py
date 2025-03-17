numero:int = (int(input("Inserisci un voto da 1 a 10: ")))


match numero:
    
    case n if n == 10:

        print("Eccellente!")

    case n if n == 9 or n == 8:

        print(f"Molto buono!")

    case n if n == 7 or n == 6:

        print("Sufficiente!")

    case n if n == 5 or n == 4:

        print("Insufficiente!")

    case n if n == 3 or n == 2 or n == 1:

        print("Gravemente Insufficiente!")

    case _:

        print("Voto non valido!")