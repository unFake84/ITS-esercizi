from persona import Persona
from studente import Studente

# creo un oggetto della classe Persona
fm: Persona = Persona("Federico", "March", 29)

# visualizzare le informazioni relative all'oggeto fm
print(fm)

# creo un oggetto della classe Studente
studente1: Studente = Studente("Mario", "Rossi", 20, "012345")

# visualizzare le informazioni relative all'oggetto studente1
print(studente1)

# controllo se studente1 sia istanza della classe Studente
# isistance(obj, Class) -> controlla se l'oggetto obj sia un instanza della classe Class
# in caso affermativo -> True
# in caso negativo -> False
if isinstance(studente1, Studente):
    
    print("\nstudente1 è istanza della classe Studente")

if isinstance(studente1, Persona):

    print("studente1 è anche istanza della classe Persona")

# controllare se l' oggetto fm sia della classe Persona
if isinstance(fm, Persona):
    
    print("\nl'oggetto fm è istanza della classe Persona")

# controllare se l'oggetto fm è anche istanza della classe Studente
if isinstance(fm, Studente):

    print("\nl'oggetto fm è istanza della classe Persona ed è anche istanza della classe Studente")

else:

    print("\nl'oggetto fm è istanza della classe Persona ma non è istanza della classe Studente")

# controllare che la classe Studente sia sottoclasse della classe Persona
# issubclass(Class1, Class2) -> controlla se Class1 sia sottoclasse della classe Class2
# in caso affermativo -> True
# in caso negativo -> False
if issubclass(Studente, Persona):

    print("\nLa classe Studente è sottoclasse della classe Persona")