from azienda_types import *
from azienda import *

print("\t", "-"*10, "[Impiegato Class]", "-"*10)
prova1: Impiegato = Impiegato("Pindus", "Panoncini", Date("12.04.2018"), RealGEZ(2200.50))
print("• Impiegato:\n", prova1)

print("\t", "-"*10, "[Dipartimento Class]", "-"*10)
indirizzo: Indirizzo = Indirizzo("Via suinis 10", CAP("00135"))
prova2: Dipartimento = Dipartimento("Purina #17", {"06-1234567"}, indirizzo)
print("• Sede:\n", prova2)

print("\t", "-"*10, "[Progetto Class]", "-"*10)
prova3: Progetto = Progetto("Pno Research", RealGEZ(500000.0))
print("• Ultima Lab:\n", prova3)