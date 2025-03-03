# creo la mia lista di 3 pizze preferite
pizza: list[str] = ["Bufala", "Margherita", "Capricciosa"]

# umb
print("")

# utilizzo ciclo FOR per stampare la mia lista personale
for elem in pizza:

    print(elem)

# uso la formattazione per inserire una frase ad ogni iterazione del ciclo

# umb
print("")

# loop 'for 'con 'i' itero da 'range' 0 a max 'len' la lista 'pizza'
for i in range(0, len(pizza)):

    # uso 'f' (formattazione) ad ogni iterazione di 'i' 1(bufala)-2(margherita)-3(capricciosa) + frase preimpostata
    print(f"Mi piace la pizza al gusto {pizza[i]}")

# aggiunto una linea alla fine del programma dove inserisco gli indici delle lista in una frase formattata
# dimostrando che usando la 'f' + gli indici della lista 'pizza[index]' posso accedere ad ognuno di essi con l'index
print(f"\nCome prima pizza amo la {pizza[0]}, \nLa seconda invece è la {pizza[1]} \nLa terza invece è la {pizza[2]} \nAmo veramente la pizza!\n")