somma = 0
num_voti = 0

while True:

    opzione: str = str(input("Vuoi inserire un voto? "))

    if opzione == "si":

        voto: int = int(input("inserisci un voto positivo "))

        if voto >= 0:

            somma += voto
            num_voti += 1
        else:

            print("Inserire un voto maggiore o uguale a 0!")

    elif opzione == "no":

        if num_voti > 0:

            print(f"La media è: {somma / num_voti}")
        else:

            print("Errore, non sono stati inseriti voti")

        break

    else:
        
        print(f"opzione non valida")