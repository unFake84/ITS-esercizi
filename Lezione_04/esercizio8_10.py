'''
Sending Messages:
Start with a copy of your program from Exercise 8-9.
Write a function called send_messages() that prints each text message and moves each message to a new list
called sent_messages as it’s printed.
After calling the function, print both of your lists to make sure the messages were moved correctly.
'''

def show_messages(*args) -> None:

    for messaggio in lista:

        print(messaggio)

def send_messages(*args) -> None:

    print("-----------------------------")
    print("Show_messages:")
    show_messages()
    sent_messages: list[str] = []

    for lista in args:

        cont: int = 0

        for elemento in lista:

            print(f"---------{cont+1} iteration--------- [elemento = {cont}]")
            sent_messages.append(elemento)
            print(f"[{elemento}] added to sent_messages!")
            cont += 1
        
    print("-----------------------------")
    print(f"Lista = {lista}")
    print(f"Sent_messages = {sent_messages}")
    print("-----------------------------")

if __name__ == "__main__":

    lista: list[str] = ["Ehi!", "Ciao!", "A dopo!", "Addio!"]

    send_messages(lista)