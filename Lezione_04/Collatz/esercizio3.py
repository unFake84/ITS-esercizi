'''

lista di num int disordinata restituisce una lista di interi ordinata dal piu piccolo al piu grande = BUBBLESORT

'''

def ordinalista(lista: list[int]) -> list[int]:

    # il suo valore è: 9(lista) - 1 = 8
    lung_lista: list[int] = len(lista) - 1 # print 8

    #i=0 range0-8   ->  9 elementi(lista)
    for i in range(lung_lista):

        for j in range(lung_lista - i):

            if lista[j] > lista[j+1]:

                lista[j], lista[j+1] = lista[j+1], lista[j]

    return lista

if __name__ == "__main__":

    lista_disordinata: list[int] = ordinalista([5, 2, 8, 6, 7, 1, 12, 9, 3])
    print(lista_disordinata)