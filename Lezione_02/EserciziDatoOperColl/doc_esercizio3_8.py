'''
Seeing the world:
'''

import time
location: list = ["Halstatt", "Wolfgang am see", "Salisburgo", "Innsbruck", "Vienna"]

# Mostro la lista nel suo ordine originale
print("Lista originale:")
print(location)
time.sleep(2)

# Ordino la lista in ordine alfabetico crescente con la funzione SORTED
s = sorted(location)
print(f"\nLista Ordinata:\n{s}")
time.sleep(2)

# Ordino la lista all'incontrario con la funzione SORTED(REVERSE)
r = sorted(location, reverse = True)
print(f"\nLista invertita:\n{r}")
time.sleep(2)

# Mostro la lista nel suo ordine originale
print(f"\nLa lista è ancora nel suo ordine originale:\n{location}")
time.sleep(2)

# ||Cambio|| l'ordine della lista 
location.reverse()
print(f"\nUsato REVERSE per cambiare l'ordine della lista:\n{location}")
time.sleep(2)

# ||Ripristino|| l' ordine della lista
location.reverse()
print(f"\nL'ordine della lista si è ripristinata:\n{location}")
time.sleep(2)

# ||Sistemo|| l' ordine della lista in ordine alfabetico crescente
location.sort()
print(f"\nFunzione SORT per sistemare la lista in ordine alfabetico crescente:\n{location}")
time.sleep(2)

# ||Sistemo|| l'ordine della lista in ordine alfabetico decrescente
location.sort(reverse = True)
print(f"\nFunzione SORT per sistemare la lista in ordine alfabetico decrescente:\n{location}")
time.sleep(2)