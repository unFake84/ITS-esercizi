# # Creare un file # #
# with open("Lezione_15/example2.txt", mode="w", encoding="utf-8") as file:

#     message: str = "Hello, world!\n"
#     written_char: int = file.write(message)
#     print(f"Written characters: {written_char}")

# prendere il tempo
import time

class StopWatch:

    def __init__(self):
        
        self.start_time = None
        self.end_time = None

    def __enter__(self):

        self.start_time = time.time() # memorizza l'ora corrente

        return self
    
    def __exit__(self, exc_type, exc_value, traceback):

        self.end_time = time.time()
        elapsed_time = self.end_time - self.start_time
        print(f"Elapsed time: {elapsed_time:.8f} seconds")

        if exc_type is not None:
            print(f"Exception type: {exc_type}")
            print(f"An Error occurred: {exc_value}")
            print(f"Traceback: {traceback}")

        return False

    def __eq__(self, value):
        pass

with StopWatch():

    print("Hello, world!")
    time.sleep(2)
    print("Goodbye, world!")