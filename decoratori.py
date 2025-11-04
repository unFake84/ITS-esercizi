import time

def cronometro(fun):

    def wrapper(*args):
        start = time.time()
        fun(*args)
        print(f"{time.time() - start:.6f}")

    return wrapper

@cronometro                 # equivalente
def ciao():
    print("Hello")

# ciao = cronometro(ciao)   # equivalente
ciao()


#######################
# RIPASSO ESAME
def min_max(lista: list[float]) -> tuple[float, float]:

    minimo: int = lista[0]
    massimo: int = lista[0]

    for num in lista:
        if num < minimo:
            minimo = num

        elif num > massimo:
            massimo = num

    return (minimo, massimo)

##################
def conta_parole(frase: list[str]) -> dict[str, int]:

    dizio: dict[str, int] = {}
    lista_pulita: list[str] = []
    frase = [f.lower().split() for f in frase]

    for indice in frase:

        for parola in indice:

            frase_pulita: str = ""
            for lettera in parola:

                if lettera in "abcdefghijklmnopqrstuvxyz":
                    frase_pulita += lettera

            lista_pulita.append(frase_pulita)

    for occorrenza in lista_pulita:

        if occorrenza not in dizio:
            dizio[occorrenza] = 1
        else:
            dizio[occorrenza] += 1

    return dizio

frase = ["Ciao co,me stai?", "ciao"]
print(conta_parole(frase))

def babolsort(lista: list[int]) -> list[int]:
    lista_ordinata: list[int] = [lista[0]]
    copia_lista: list[int] = lista

    for numero in copia_lista:

        if numero > lista_ordinata[-1]:
            lista_ordinata.append(numero)

        elif numero < lista_ordinata[0]:
            lista_ordinata.insert(0, numero)

    return lista_ordinata

lista: list[int] = [5, 3, 2, 1, 8, 4]
print(babolsort(lista))