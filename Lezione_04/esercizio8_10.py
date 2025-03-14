'''
Sending Messages:
Start with a copy of your program from Exercise 8-9.
Write a function called send_messages() that prints each text message and moves each message to a new list called sent_messages as it’s printed.
After calling the function, print both of your lists to make sure the messages were moved correctly.
'''

lista: list[str] = ["Ciao!", "A dopo!", "Addio!"]

def show_messages(*args) -> list[str]:

    for _ in lista:

        print(_)

#show_messages()

def send_messages(*args) -> list[str]:

    sent_messages: list[str] = []
    lunghezza: int = len(lista)

    for _ in range(lunghezza):

        sent_messages.append(lista[0])
        lista.pop(0)
        #print(lista)

    print(f"Lista = {lista}")
    print(f"Sent_messages = {sent_messages}")

if __name__ == "__main__":

    send_messages(lista)