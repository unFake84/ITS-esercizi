oggetti: list[str] = []

for _ in range(3):

    user: str = (input("Inserire un oggetto: "))
    oggetti.append(user.lower())

match user:

    case user if user == "penna" and user == "matita" and user == "quaderno":

        print("Materiale scolastico")

    case user if user == "pane" and user == "latte" and user == "uova":

        print("Prodotti alimentari")


    case user if user == "sedia" and user == "tavolo" and user == "armadio":

        print("Mobili")

    case user if user == "telefono" and user == "computer" and user == "tablet":

        print("Dispositivi elettronici")

    case _:

        print("Categoria Sconosciuta")