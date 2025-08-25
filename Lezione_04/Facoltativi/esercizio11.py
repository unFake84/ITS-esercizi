'''
Sieve of Eratosthenes Prime Number Generator:

    Create a function that generates a list of prime numbers up to a specified limit using
    the Sieve of Eratosthenes algorithm.
    Initialize an array of all numbers up to the limit, marking each number as prime initially.
    Iterate through the array, starting from 2, and mark every multiple of the current number as non-prime.
    The remaining unmarked numbers are the prime numbers within the limit.
    Return the list of prime numbers.

'''

def sieveEratosthenes(limit: int) -> list[int]:

    if limit < 2:
        raise ValueError("The limit number should be equal or upper by 2.")

    lista_numerata: list[int] = [n for n in range(2, limit + 1)]
    lista_booleani: list[bool] = [True for _ in lista_numerata]
    lista_primi: list[int] = []

    for i, num in enumerate(lista_numerata):

        if lista_booleani[i]:
            lista_primi.append(num)
        
        multiplo: int = num * 2

        while multiplo <= limit:

            indice: int = multiplo - 2 #<- perche lista_numerata parte da 2
            lista_booleani[indice] = False
            multiplo += num

    return lista_primi

if __name__ == "__main__":

    print(sieveEratosthenes(50))









    # for num in lista_numerata:
    #     for duplicati in lista_numerata:
    #         print(num, duplicati)
    #         if num%duplicati == 0:
    #             break
    #         lista_primi.append(num) if num not in lista_primi else None












    # lista_numerata: list[int] = [n for n in range(2, limit + 1)]
    # limiti_massimi: list[int] = []
    # lista_primi: list[int] = []

    # for n in lista_numerata:

    #     if int(n**0.5) not in limiti_massimi:
    #         limiti_massimi.append(int(n**0.5))


    # print("Lista numerata: ", lista_numerata)
    # print("Limiti massimi: ", limiti_massimi)
    # print(f"Lista primi: {lista_primi}")









    # for num in lista_numerata:
    #     print(f"num: [{num}]")
    #     for lim in limiti_massimi:
    #         if lim >= 2:
    #             print("lim: ", lim)
    #             if num%lim == 0:
    #                 print("\nmodulo\n")
    #                 print("-"*10)
    #             else:
    #                 if num not in lista_primi:
    #                     print(f"aggiunto: {num}")
    #                     lista_primi.append(num)
    #     print("-"*10)














    # lista_numerata: list[int] = [n for n in range(2, limit + 1)]
    # lista_primi: list[int] = []

    # for passo in lista_numerata:
    #     if passo**5:
    #         lista_primi.append(2) if not lista_primi else None
    #         lista_primi.append(passo)


    # print(lista_numerata)
    # print(lista_primi)








    # lista_numerata: list[int] = [n for n in range(2, limit + 1)]
    # passo_p2: list[int] = []
    # passo_p3: list[int] = []
    # passo_p5: list[int] = []
    # lista_primi: list[int] = []

    # for p2 in lista_numerata:
    #     if p2%lista_numerata[0] != 0:
    #         passo_p2.append(p2)
    # lista_primi.append(2)
    
    # for p3 in passo_p2:
    #     if p3%passo_p2[0] != 0:
    #         passo_p3.append(p3)
    # lista_primi.append(3) if limit >= 3 else None
    
    # for p5 in passo_p3:
    #     if p5%passo_p3[0] != 0:
    #         passo_p5.append(p5)
    # lista_primi.append(5) if limit >= 5 else None
    # lista_primi.extend(passo_p5)

    # print(lista_numerata)
    # print(passo_p2)
    # print(passo_p3)
    # print(passo_p5)
    # print(lista_primi)