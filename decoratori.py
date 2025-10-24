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