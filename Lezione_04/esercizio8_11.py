'''
Archived Messages:
Start with your work from Exercise 8-10. Call the function send_messages() with a copy of the list of messages.
After calling the function, print both of your lists to show that the original list has retained its messages.
'''

def show_messages(*args) -> None:

    for messaggio in lista:

        print(messaggio)

def send_messages(*args) -> None:

    print("-----------------------------")
    #print("Show_messages:")
    #show_messages()
    sent_messages: list[str] = []

    for lista in args:

        #cont: int = 0

        for elemento in lista:

            #print(f"---------{cont+1} iteration--------- [elemento = {cont}]")
            sent_messages.append(elemento)
            #print(f"[{elemento}] added to sent_messages!")
            #cont += 1
        
    print("-----------------------------")
    print(f"Lista = {lista}")
    print(f"Sent_messages = {sent_messages}")
    print("-----------------------------")

if __name__ == "__main__":

    lista: list[str] = ["Ehi!", "Ciao!", "A dopo!", "Addio!"]

    send_messages(lista)