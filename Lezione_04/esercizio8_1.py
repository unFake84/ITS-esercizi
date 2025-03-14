'''
Message: Write a function called display_message()
that prints one sentence telling everyone what you are learning about in this chapter.
Call the function, and make sure the message displays correctly.
'''

def display_message(name: str, ) -> None:

    print(f"Sig. {name}, today I am learning the functions.")

if __name__ == "__main__":

    utente: str = (input("Insert name: "))

    display_message(utente)