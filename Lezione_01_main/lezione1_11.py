liberi = 20


while True:

    opzione: str = str(input("inserisci un opzione: "))
    


    if opzione == "prenota":

        if liberi > 0:

            liberi -= 1

        else:

            print("Non ci sono posti disponibili")



    elif opzione == "libera":

        if liberi < 20:

            liberi += 1

        else:

            print("Tutti i posti sono già disponibili")


    
    elif opzione == "visualizza":

        print(f"I posti liberi sono: {liberi}")
        print(f"I posti occupati sono: {20-liberi}")



    elif opzione == "esci":
        
        break