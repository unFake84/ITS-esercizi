# dal modulo esercizio.py importare la classe MovieCatalog
from esercizio import MovieCatalog

# creare un oggetto della MovieCatalog
catalog: MovieCatalog = MovieCatalog()

# aggiungiamo un regista e dei film la catalogo
catalog.add_movie("Steven Spielberg", ["Casper", "Ritorno al futuro"])

# visualizziamo il catalogo
print(catalog.getCatalog())

#                # catalog.add_movie("Steven Spielberg2", ["Casper2", "Ritorno al futuro2"])
#                # print(catalog.getCatalog())
#                # print(catalog)

# aggiungere un altro film di steven spielberg al catalogo
catalog.add_movie("Steven Spielberg", ["ET"])

print(catalog.getCatalog())

# aggiungere un nuovo regista
catalog.add_movie('Quentin Tarantino', ["Pulp Fiction", "Kill Bill"])

#print(catalog.getCatalog())

# rimuovere il film "ET" dal catalogo
catalog.remove_movie("Steven Spielberg", "ET")

#print(catalog.getCatalog())

catalog.remove_movie("Steven Spielberg", "Ritorno al futuro")
catalog.remove_movie("Steven Spielberg", "Casper")

print(catalog.getCatalog())
# print(catalog)

print(catalog.list_directors()) # solo la lista dei registi