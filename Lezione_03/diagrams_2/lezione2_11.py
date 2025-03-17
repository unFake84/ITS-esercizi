while True:

    try:
    
        utente: int = (int(input("Inserire numero intero: ")))
        break

    except ValueError:

        print("Deve essere inserito un numero intero.")

if utente%2 == 0 and utente > 10:

    print("Numero valido.")

else:

    print("Numero non valido.")