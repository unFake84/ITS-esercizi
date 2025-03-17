# 1 Tests for equality and inequality with strings
banana = "fragola"
print("La banana è grande quanto una fragola?\nprevedo False.")
print(banana != "fragola")
print("-----------------------------------------------------------------------")

# 2 Tests using the lower() method
grande_raccordo_anulare = "G.R.A."
print("Il GRA si scrive in maiuscolo,\nprevedo True.")
print(grande_raccordo_anulare.lower() != grande_raccordo_anulare.upper())
print("-----------------------------------------------------------------------")

# 3a Numerical tests involving equality,
n = 7
print("I numeri moltiplicati per uno, hanno lo stesso prodotto\nIo prevedo True.")
print((n*1) == n)
print("-----------------------------------------------------------------------")

# 3b and inequality, 
print("Sette è diverso da sei,\nprevedo True.")
print(7 != 6)
print("-----------------------------------------------------------------------")

# 3c greater than and less than,
print("Il numero 7 è minore di 6,\nprevedo False.")
print(7 < 6)
print("")
print("Il numero 7 è maggiore di 6,\nprevedo True.")
print(7 > 6)
print("-----------------------------------------------------------------------")

# 3d greater than or equal to, and less than or equal to.
print("Il numero sette è maggiore o uguale a 6,\nprevedo True.")
print( 7 >= 6)
print("")
print("Il numeor 7 è minore o uguale a 6,\nprevedo False.")
print(7 <= 6)
print("-----------------------------------------------------------------------")

# 4 Tests using the AND keyword and the OR keyword
print("Sette per uno E uno per sette è la stessa cosa,\nprevedo True.")
print((7*1) == 7 and (1*7) == 7)
print("")
#print(())
print("-----------------------------------------------------------------------")

# 5  Test whether an item is in a list
lista: list[str] = ["a", "b", "c", "d", "e"]
print("La lettera A si trova dentro la lista,\nprevedo True.")
print("a" in lista)
print("")
print("La lettera F è dentro la lista,\nprevedo False")
print("f" in lista)