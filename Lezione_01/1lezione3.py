sum: int = 0
cont: int = 1

while cont <= 5:

    n: int = int(input("inserisci un numero: "))

    if n > 0:
        
        sum += n
    
    cont += 1
    
print(f"La somma dei soli numeri positivi è: {sum}")