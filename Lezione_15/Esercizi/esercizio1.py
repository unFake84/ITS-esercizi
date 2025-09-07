'''
Crea un context manager usando una classe
Definisci una classe FileManager che implementa un context manager che gestisce le risorse dei file.

Implementa appropriatamente la funzione __init__, __enter__ e la funzione  __exit__

Esempio di funzionamento:
Il context manager deve permettere di aprire il file, effettuare operazioni e chiudere la risorsa aperta.

with FileManager('example.txt', 'w') as f:

    f.write('Hello, world!')
'''

import os, typing

class FileManager:

    def __init__(self, file_name: str, mode: str, encoding: str = "utf-8") -> None:
        self.file_name: str = file_name
        self.mode: str = mode
        self.encoding: str = encoding
        self.connection: typing.TextIO|None = None

    def __enter__(self) -> None:
        print("File Opened")

        path_file: str = "/home/its/ITS-esercizi/Lezione_15/Esercizi/"
        full_path: str = os.path.join(path_file, self.file_name)

        self.connection = open(full_path, self.mode, encoding = self.encoding)
        print(f"Will save in: {full_path}" if self.mode == "w" else f"Opening the file '{self.file_name}'")
        return self.connection

    def __exit__(self, exc_type, exc_value, traceback) -> None|bool:
        print("File exiting")

        if exc_type is not None:
            print(f"Exception type: {exc_type}")
            print(f"Exception value: {exc_value}")
            print(f"Traceback: {traceback}")

        if self.connection is not None:
            self.connection.close()

        return False

if __name__ == "__main__":

    # with FileManager('example.txt', 'w') as f:

    #     f.write('Hello, world!')

    # with FileManager('example.txt', 'r') as f:
    #     print(f.read())

    try:
        with FileManager('example2.txt', 'w') as f2:
            f2.write("Prima riga")
            1/0
            f2.write("Questa riga non verrà mai scritta")

        with FileManager('example.txt', 'r') as f:
            print(f.read())
            1/0

    except ZeroDivisionError as err:
        print("Error caught, but file closed successfully")