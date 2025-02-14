posti_max: int = int(input("inserisci posti max: "))

posti_liberi = posti_max


while True:

    opzione: str = str(input("inserisci un opzione: "))
    


    if opzione == "ingresso":

        if posti_liberi > 0:
            posti_liberi -= 1
        else:
            print("Il parcheggio è pieno")



    elif opzione == "uscita":

        if posti_liberi < posti_max:
            posti_liberi += 1
        else:
            print("Il parcheggio è vuoto")


    
    elif opzione == "stato":

        print(f"I posti liberi sono: {posti_liberi}")
        print(f"I posti occupati sono: {posti_max-posti_liberi}")



    elif opzione == "esci":
        
        break