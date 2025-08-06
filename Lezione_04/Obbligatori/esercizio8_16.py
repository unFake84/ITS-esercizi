'''
Imports: Using a program you wrote that has one function in it, store that function in a separate file.
Import the function into your main program file, and call the function using each of these approaches:
import module_name
from module_name import function_name
from module_name import function_name as fn
import module_name as mn
from module_name import *
'''

# #-----------------------------------------------------------------------------------
# import esercizio8_2

# esercizio8_2.favorite_book("Il Signore Degli Anelli.")
# #-----------------------------------------------------------------------------------

# #-----------------------------------------------------------------------------------
# from esercizio8_3 import make_shirt

# make_shirt(text = "Yabadabadooo", size = "XXL")
# #-----------------------------------------------------------------------------------

# #-----------------------------------------------------------------------------------
# from esercizio8_5 import describe_city as fn

# fn("Venice")
# fn("London", "England")
# #-----------------------------------------------------------------------------------

# #-----------------------------------------------------------------------------------
# import esercizio8_2 as mn

# mn.favorite_book("Liebestraum No.3")
# #-----------------------------------------------------------------------------------
from typing import Any
from esercizio8_7 import *

dati: dict[Any] = make_album("Bach", "Il mio primo Bach", 10)

# # # 1 modo
# print(
#   f"L'artista {dati['artista']} ha fatto modo che dopo quasi 300 anni dalla sua morte, " \
#       f"gli è stato dedicato un libro chiamato: {dati['albums']}, " \
#            f"contiene {dati['traccie']} traccie da lui composte." \
# )

# 2 modo
print(f"""
    L'artista {dati['artista']} ha fatto modo che dopo quasi 300 anni dalla sua morte, 
        gli è stato dedicato un libro chiamato: {dati['albums']}, 
            contiene {dati['traccie']} traccie da lui composte.\n"""
)
#-----------------------------------------------------------------------------------