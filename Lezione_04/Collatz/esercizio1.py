import matplotlib.pyplot as plt

def f(n: float) -> list[float]:

    numeri: list = [n]

    while n != 1:

        if n%2 == 0:

            n /= 2
            #print(n)

        else:

            n = (3*n) + 1
            #print(n)

        numeri.append(n)

    return numeri

    # n /= 2 if n%2 == 0 else (3*n) + 1

    # return n

#f(5)
numeri: list[float] = f(5.0)
plt.plot(numeri)
plt.show()