'''
Crea un context manager che permette di calcolare il tempo che viene impiegato
ad eseguire le istruzioni che si trovano nel with

with Timer():

    time.sleep(1)

time elapsed: 1.00000

in questo esempio il tempo passato non sarà mai uguale a 1

'''

import time

class Timer:

    def __init__(self):
        self.start_time: float = 0

    def __enter__(self) -> None:
        self.start_time = time.time()

    def __exit__(self, exc_type, exc_value, traceback) -> None|bool:
        if exc_type is not None:

            print(f"Exception type: {exc_type}")
            print(f"Exception value: {exc_value}")
            print(f"Traceback: {traceback}")

        end_time: float = time.time()
        print(f"time elapsed: {end_time - self.start_time:.5f}")

        return False

if __name__ == "__main__":

    with Timer():

        time.sleep(1)