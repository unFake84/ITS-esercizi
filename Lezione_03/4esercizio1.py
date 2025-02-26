# creo la mia lista di 3 pizze preferite
pizza: list[str] = ["Bufala", "Margherita", "Capricciosa"]

print("")

# utilizzo ciclo FOR per stampare la mia lista personale
for elem in pizza:

    print(elem)

# uso la formattazione per inserire una frase ad ogni iterazione del ciclo

print("")

for i in range(0, len(pizza)):

    print(f"Mi piace la pizza al gusto {pizza[i]}")

# aggiunto una linea alla fine del programma dove inserisco gli indici delle lista in una frase formattata
print(f"\nCome prima pizza amo la {pizza[0]}, \nLa seconda invece è la {pizza[1]} \nLa terza invece è la {pizza[2]} \nAmo veramente la pizza!\n")