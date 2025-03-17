nome_corso: str = str(input("inserire il nome del corso: "))
max_posti = 100

while True:

    opzione: str = str(input("inserisci un opzione: "))

    if opzione == "iscrivi":

        if max_posti > 0:

            max_posti -= 1
        else:

            print("Non ci sono posti disponibili")

    elif opzione == "annulla":

        if max_posti < 100:

            max_posti += 1

        else:

            print("Tutti i posti sono già disponibili")

    elif opzione == "visualizza":

        print(f"I posti sono: {max_posti}")
        print(f"I posti disponibili sono: {100-max_posti}")
    
    elif opzione == "elimina":

        print(f"Il corso {nome_corso}, è stato eliminato")
        
        nome_corso: str = str(input("inserire il nome del corso: "))

    elif opzione == "esci":

        break

    else:
        
        print("selezione non valida")