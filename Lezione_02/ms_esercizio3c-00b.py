nome:str = (str(input("Inserire il tuo nome:\n")))
genere:str = (str(input("Inserire il tuo genere\nSelezionare 'm' per maschio\nSelezionare 'f' per femmina:\n")))

match (genere):

    case ("m"):

        print(f"Nome: {nome}\nGender: Maschio")

    case ("f"):

        print(f"Nome: {nome}\nGender: Femmina")

    case _:
        print(f"Mi dispiace {nome},\nnon è possibile procedere con la generazione\ndi un docuemnto di identità!")