# n: int = int(input("Inserire numero positivo: "))

# if n % 1 == 0 and n > 0:

#     sum = 0
#     i = 1

#     if i > n:
#         print(f"La somma è: {sum}")
    
#     else:
#         sum = sum + i * i
#         i += 1

# else:
#     print("Errore, il numero deve essere positivo")

i = 1
somma = 0

n: int = int(input("Inserire numero positivo: "))
if n > 0:
    while i <= n:
        somma += i**2
        i += 1

    print(f"Il risultato è: {somma}")

else:
    print(f"Errore, il numero deve essere positivo")