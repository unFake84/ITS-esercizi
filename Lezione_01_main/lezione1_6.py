n: int = int(input("inserisci un numero: "))

i = n-1
fattoriale = n

if n < 0:

    print("Il numero inserito deve essere positivo")

else:

    while i != 1:
        
        fattoriale *= i
        i-=1

print(fattoriale)