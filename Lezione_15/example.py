# # lettura file (lettura)
# PATH: str = "Lezione_15/example.txt"
# mode: str = "r"
# encoding: str = "utf-8"

# file = open(PATH)
# output: str = file.read()
# print(output)
# file.close()




# # scrittura file (sovrascrive) -> restituisce un valore (il totale dei caratteri immessi)
# PATH: str = "Lezione_15/example.txt"
# mode: str = "w"
# encoding: str = "utf-8"

# file = open(PATH, mode=mode, encoding=encoding)
# output: str = file.write("Hello World!")
# print(output)
# file.close()



# # append file (aggiungere) -> restituisce un valore (il totale dei caratteri immessi)
PATH: str = "Lezione_15/example.txt"
mode: str = "a"
encoding: str = "utf-8"

file = open(PATH, mode=mode, encoding=encoding)
input_text: str = input("Enter text to write to the file: ")
output: str = file.write(input_text)
print(output)
file.close()