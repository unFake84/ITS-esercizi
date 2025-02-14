max: int = int(input("inserisci un numero: "))

cont: int = 1

while cont < 4:
    num: int = int(input("inserisci un numero: "))

    if num > max:
        max = num

    cont += 1
print(f"il numero massimo è: {max}")