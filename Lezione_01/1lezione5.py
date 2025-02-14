n: int = int(input("inserisci un numero: "))
primo = True
if n < 2:
    print("Il numero non è primo")

else:
    div = 2

    while div < n:

        if n % div == 0:
            print("il numero non è primo")
            primo = False
            break
        div += 1
    if primo:
        print("Il numero è primo")