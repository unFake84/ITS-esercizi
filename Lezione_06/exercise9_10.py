'''
Imported Restaurant:

1.
    Using your latest Restaurant class, store it in a module.
    Make a separate file that imports Restaurant.
    
2.
    Make a Restaurant instance, and call one of Restaurant’s methods to show
    that the import statement is working properly.

'''

# 1.
from exercise9_4 import Restaurant

# 2.
istanza: Restaurant = Restaurant("Da Boe", "Meglio non saperlo", 2)

istanza.describe_restaurant()
istanza.open_restaurant()
print("Oggi sono stati serviti", istanza.get_number_served(), "clienti.")