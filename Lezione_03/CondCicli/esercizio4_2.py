# umb
print()

# creo lista personale
animals: list[str] = ["Gatti", "Cani", "Cavalli"]

# 1a richiesta:
# utilizzo ciclo FOR per stampare ogni elemento 'elem' in output 'print'
for elem in animals:

    # 'elem' diventa 'gatti'-'cani'-cavalli' ad ogni iterazione dentro 'animals' [0, 1, 2]
    print(elem)

# 2a richiesta:
# stampo una frase diversa per ogni elemento della lista
# possibile grazie all'index '[]'.
print()
print(f"I {animals[0].lower()} sono agilissimi")
print(f"I {animals[1].lower()} sono fedelissimi")
print(f"I {animals[2].lower()} sono potentissimi")

# 3a richiesta:
# stampo una frase indicando cosa hanno in comune questi animali.
print()
print(f"I {animals[0]}, i {animals[2]} ed i {animals[1]},\nsono sempre stati\namici e fedeli dell'uomo,\n+o-.")
print()