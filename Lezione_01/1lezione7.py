counter_pari = 0
counter_dispari = 0
i = 1

while i <= 10:
    n: int = int(input("inserisci un numero: "))

    if n%2==0:
        counter_pari = counter_pari + 1

    else:
        counter_dispari = counter_dispari + 1
    
    i = i + 1
    
print("Numeri pari: ", counter_pari)
print("Numeri dispari: ", counter_dispari)