soglia: int = int(input("inserisci un valore soglia: "))
cont = 0

while cont < 7:
    
    n: int = int(input("inserisci un numero: "))
    
    if n > soglia:
        print("Il numero maggiore é: ", n)

    cont += 1
