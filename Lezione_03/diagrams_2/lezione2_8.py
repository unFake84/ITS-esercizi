somma = 0
print("Inserire due numeri, di cui il primo deve essere minore del secondo.")

a: int = int(input("inserisci il primo numero: "))
b: int = int(input("inserisci il secondo numero: "))

if a < b and a > 0:

    while a <= b:

        somma += a
        a += 1

    else:
        
        print(f"Il risultato è: {somma} ")

else:
    
    print("Errore!")