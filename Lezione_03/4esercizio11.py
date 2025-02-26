# un pò di umbridge
print('\n')

# riprendo lista pers es4-1 e creo una lista nuova,poi uso funzione .APPEND per aggiungere un elemento a ciascuna lista
pizza: list[str] = ["Bufala", "Margherita", "Capricciosa"]
# friend_pizza: list[str] = pizza[:] crea una lista con lo slice [ : ]
friend_pizza = list(pizza) # crea una lista identica a "pizza"


pizza.append("Boscaiola")
friend_pizza.append("4Formaggi")

# dimostro che la mia lista è aggiornata usando il ciclo FOR
print('My favorite pizzas are:\n')
for mio in pizza:

    print(mio)

# umbridge
print('')
print('And')
print('')

# dimostro che la seconda lista è aggiornata usando il ciclo FOR
print('My friend\'s favorite pizzas are:\n')
for suo in friend_pizza:
    print(suo)

# umb
print('\n')