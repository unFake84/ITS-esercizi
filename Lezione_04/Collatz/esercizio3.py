'''

lista di num int disordinata restituisce una lista di interi ordinata dal piu piccolo al piu grande = BUBBLESORT

'''

def ordinalista(lista: list[int]) -> list[int]:

    lista_ordinata: list[int] = []

    for i in range(len(lista)):

        for j in range(lista[i]):

            lista_ordinata.append(i)

    return lista_ordinata

if __name__ == "__main__":

    lista_disordinata: list[int] = ordinalista([5, 2, 8, 6, 7, 1, 12, 9, 3])
    print(lista_disordinata)