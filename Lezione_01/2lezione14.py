punteggio: int = 0

print("-----------------------------------------------------------------------")

while punteggio < 100:

    try:

        utente_d1: int = (int(input("Simulare 1° dado: ")))
        utente_d2: int = (int(input("Simulare 2° dado: ")))

        if utente_d1 > 0 and utente_d1 <= 6 and utente_d2 > 0 and utente_d2 <= 6:

            sum: int = utente_d1 + utente_d2

            if utente_d1%2 == 0 and utente_d2%2 == 0 and sum > 8:

               punteggio = 100
               print("Vittoria!")
               print(f"Il punteggio attuale è: {punteggio}")
               print("-----------------------------------------------------------------------")

            elif utente_d1 == 6 or utente_d2 == 6 or sum == 7:

                punteggio += 10
                print(f"Il punteggio attuale è: {punteggio}")
                print("-----------------------------------------------------------------------")

            else:

                punteggio = 0
                print("Sconfitta.")
                print(f"Il punteggio attuale è: {punteggio}")
                print("-----------------------------------------------------------------------")
                break
        else:

            print("Un dado ha sei facce.")
            print("-----------------------------------------------------------------------")

    except ValueError:

        print("Numero non riconoscibile, riprovare.")
        print("-----------------------------------------------------------------------")
        punteggio += 1

    sum: int = utente_d1 + utente_d2