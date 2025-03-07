punteggio: int = 0
d1: int = 0
d2: int = 0
sum: int = 0

while punteggio < 100:

    while True:
        
        print(f"Punteggio: {punteggio}")
        d1: int = (int(input("Simulare il primo dado: ")))
        d2: int = (int(input("Simulare il secondo dado: ")))

        if d1 > 0 and d1 <= 6 and d2 > 0 and d2 <= 6:

            sum = d1 + d2
            break
        
        else:

            print("Uno dei due numeri o entrambi non rispettano le regole!.")

    if d1 % 2 == 0 and d2 % 2 == 0 and sum > 8:

        punteggio = 100

    elif d1 == 6 or d2 == 6 or sum == 7:

        punteggio += 10

    else:

        punteggio = 0

        print("Sconfitta!")
        print(punteggio)
        break

if punteggio == 100:
    print("Vittoria!")