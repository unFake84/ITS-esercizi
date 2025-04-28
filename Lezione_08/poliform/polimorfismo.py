from persona import Persona
from alieno import Alien

# creare un oggetto p della classe Persona
p: Persona = Persona("Dioni", "Manon", 40)

# visualizzare le informazioni dell'oggetto p della classe Persona
print(p)
print("\n")
# creare un oggetto et della classe Alieno
et: Alien = Alien("Andromeda")

# visualizzare le informazioni dell' oggetto et
print(et)

# invocare il metodo speak() della classe Persona
p.speak()

# invocare il metodo speak() di un alieno
et.speak()