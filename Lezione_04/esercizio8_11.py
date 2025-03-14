'''
Archived Messages:
Start with your work from Exercise 8-10. Call the function send_messages() with a copy of the list of messages.
After calling the function, print both of your lists to show that the original list has retained its messages.
'''

lista: list[str] = ["Ciao!", "A dopo!", "Addio!"]

def show_messages(*args) -> list[str]:

    for _ in lista:

        print(_)

def send_messages(*args) -> list[str]:

    sent_messages: list[str] = []
    lunghezza: int = len(lista)

    for _ in range(lunghezza):

        sent_messages.append(lista[0])
        #lista.pop(0)
        #print(lista)

    print(f"Lista = {lista}")
    print(f"Sent_messages = {sent_messages}")

if __name__ == "__main__":

    send_messages(lista)