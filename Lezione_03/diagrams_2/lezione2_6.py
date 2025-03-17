x: int = int(input("Inserire numero positivo: "))

if x > 0:

    i = 1
    somma = 0

    while i <= 10:

        n: int = int(input(f"Inserire il {i} numero positivo: "))

        if x % 2 == 0:

            if n > x / 2:

                somma += n

        if n < x:

            somma += n

        i += 1

    print(f"La somma é: {somma}")

else:

    print(f"(Errore il numero deve essere positivo!)")