'''
Messages: Make a list containing a series of short text messages.
Pass the list to a function called show_messages(), which prints each text message.
'''

lista: list[str] = ["Ciao!", "A dopo!", "Addio!"]

def show_messages(*args) -> list[str]:

    for i in lista:

        print(i)

if __name__ == "__main__":

    show_messages()