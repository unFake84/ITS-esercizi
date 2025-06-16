# sto affermando che 1 è maggiore di 0
# se tutto ok non dice nulla
assert 1 > 0

# viene sollevato un assertion error
# assert 1 < 0

# permette di personalizzare il messaggio di errore
# assert <condition being tested>, <error message to be displayed>
# AssertionError: <error message to be displayed>
assert 1 < 0, "The condition is False"