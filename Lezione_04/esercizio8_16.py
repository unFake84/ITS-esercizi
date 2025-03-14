'''
Imports: Using a program you wrote that has one function in it, store that function in a separate file.
Import the function into your main program file, and call the function using each of these approaches:
import module_name
from module_name import function_name
from module_name import function_name as fn
import module_name as mn
from module_name import *
'''

import esercizio8_2

from .esercizio8_3 import make_shirt

from .esercizio8_2 import favorite_book as fn

import esercizio8_2 as mn

from .esercizio8_2 import *

favorite_book("Il Signore Degli Anelli.")