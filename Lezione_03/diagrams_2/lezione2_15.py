utente:int
while True:

    try:

        utente: int = int(input("Inserire un numero: "))
        break

    except ValueError:

        print("Per favore inserire un numero intero.")

if utente > 0 and utente <= 100:

    sum: int = 0
    i: int = 1

    while i <= utente:

        if i % 2 == 0:
            sum += i

        i += 1
    
    print(sum)
    


elif utente == 0 or utente < 0:

    print("Errore")