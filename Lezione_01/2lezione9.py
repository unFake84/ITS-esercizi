n: int = int(input("inserire un numero intero positivo: "))
numbers = 0
divisibili = 0

if n > 0:

    while numbers < 10:
        number: int = int(input(f"inserisci il {numbers+1}° numero: ")) 

        if number % n == 0:
            divisibili += 1
        
        numbers += 1
    print(f"Il risultato è: {number}")

else:
    
    print("Errore, devi inserire un numero intero positivo!!")