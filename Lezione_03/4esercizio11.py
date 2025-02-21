# un pò di lambridge
print('\n')

# riprendo lista pers es4-1 e creo una lista nuova, uso funzione .APPEND per aggiungere un elemento a ciascuna lista
pizza: list[str] = ["Bufala", "Margherita", "Capricciosa"]
friend_pizza: list[str] = ["Diavola", "Marinara", "Napoli"]
pizza.append("Boscaiola")
friend_pizza.append("4Formaggi")

# dimostro che la mia lista è aggiornata usando il ciclo FOR
print('My favorite pizzas are:\n')
for mio in pizza:
    print(mio)

# lambridge
print('')
print('And')
print('')

# dimostro che la seconda lista è aggiornata usando il ciclo FOR
print('My friend\'s favorite pizzas are:\n')
for suo in friend_pizza:
    print(suo)

# lmb
print('\n')