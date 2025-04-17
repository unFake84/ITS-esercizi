'''

Somma di due numeri

Crea una funzione lambda che accetti due numeri e restituisca la loro somma.

'''

from typing import Callable
from typing import Any

somma:Callable[[Any, Any], Any] = lambda a, b: a + b

print(somma(10.5, 5))