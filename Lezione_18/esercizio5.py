'''
An interactive calculator:
It is required to develop an interactive calculator with at least 10 test cases
using UnitTest trying to (possibly) cover all execution paths!
User input is assumed to be a formula that consists of a number, an operator (at least + and -),
and another number, separated by white space (e.g. 1 + 1).
Split user input using str.split(), and check whether the resulting list is valid:

    If the input does not consist of 3 elements, raise a FormulaError, which is a custom Exception.
    Try to convert the first and third inputs to a float (like so: float_value = float(str_value)).
    Catch any ValueError that occurs, and instead raise a FormulaError.
    If the second input is not '+' or '-', again raise a FormulaError.
    If the input is valid, perform the calculation and print out the result.
    The user is then prompted to provide new input, and so on, until the user enters quit.
'''

import os

# creo classe da utilizzare come ponte(penso)
class FormulaError(Exception):

    pass

# funzione che ha come scopo; di prendere una stringa, controllare se è formato da: numero operatore* numero.
#                                                                            * l'operatore deve essere: + o -
def sum_OR_sub(operation: str) -> float:

    # <se> l'input è di tipo stringa
    if isinstance(operation, str):

        '''
        operation: must be 'str' type
        '''

        # divido la stringa proveniente da 'operation'
        # e la divido dentro la lista 'listacheck' utilizzando
        # la funzione .spilt(" ") che divide la stringa anche su ogni singolo spazio

        listacheck: list[str] = operation.split(" ")
        listaok: list[str] = []

        # utilizzo ciclo for per eliminare gli spazi vuoti se presenti
        for _ in listacheck:

            if _ != " ":

                listaok.append(_)

        len_lista: int = len(listaok) # <-- deve essere 3 per far funzionare la funzione

        # creata la variabile che controlla se gli indici sono esattamente 3
        if len_lista != 3:

            # se non sono esattamente 3 spiego all'utente cosa potrebbe essere andato storto
            raise FormulaError(
                "An expression of this format must be entered:\n\t[number] [operator] [number] (e.g. 3 + 4 or 3 - 4)\n"
                f"\tYour Try: {operation}\n"
                f"\tParsed input: {listaok}"
            )
        
        # provo a convertire i presunti numeri in float
        try:

            index0: float = float(listaok[0])
            index2: float = float(listaok[2])

        # se non è possibile
        except ValueError:
            
            raise FormulaError("Numbers not valid")

        # creo variabile per controllo dell'operatore
        index1: str = listaok[1]

        # se nell'indice 1, che è destinato al operatore
        if index1 not in ("+", "-"):

            # non è presente il + oppure il -
            raise FormulaError(
                f"The operator {index1} is not valid\n"
                "Must be: + or -"
                )
        
    # se invece è di un altro tipo es: int, float
    else:

        raise FormulaError("It must be a string, first")

    # ritorna j + k se l'operatore è presente, altrimenti j - k
    return index0 + index2 if index1 == "+" else index0 - index2

# isoliamo il personal test, senza UniTest
if __name__ == "__main__":

    cleaner: int = 0
    result: float = None
    user: str = ""

    # Simuliamo un app:

    os.system("clear")
    print("\t\t\tWelcome\n\t\tAn interactive calculator\n")
    print(
        "Write an expression in this format: 1 + 2 or 1 - 2 to results\n"\
        "type quit to exit\n"
    )

    while True:

        if cleaner == 2:

            os.system("clear")
            print("\t\t\tWelcome\n\t\tAn interactive calculator\n")
            print(
                "Write an expression in this format: 1 + 2 or 1 - 2 to results\n"\
                "type quit to exit\n"
            )
            if result is None:
                print(f"Insert an expression: {user}\nResult =", "Error type again for more info")
            else:
                print(f"Insert an expression: {user}\nResult =", result)
            cleaner = 0

        cleaner += 1

        user = input("Insert an expression: ")

        if user == "quit":

            print("Closing")
            break

        try:

            result = sum_OR_sub(user)
            print("Result =", result)

        except FormulaError as show_err:

            result = None
            print("Result =", show_err)