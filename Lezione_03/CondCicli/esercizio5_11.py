# creo lista
numbers: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("-----------------------------------------------------------------------")

# ciclo per iterare 'lista' 
for n in numbers:

    # se 'n' è 4 o maggiore di 4 aggiunge TH
    if n >= 4:

        print(f"{n}th")
    
    # se 'n' è =simile= a 3
    elif n == 3:

        print(f"{n}rd")

    # se =simile= a 2
    elif n == 2:

        print(f"{n}nd")

    # altrimenti sotto l'UNO tutto ST!!!!! 
    else:

        print(f"{n}st")

    print("-----------------------------------------------------------------------")