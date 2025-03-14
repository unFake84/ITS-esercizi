'''
Sandwiches:
Write a function that accepts a list of items a person wants on a sandwich.
The function should have one parameter that collects as many items as the function call provides,
and it should print a summary of the sandwich that’s being ordered. Call the function three times,
using a different number of arguments each time.
'''

def sandwitches(*args) -> list:

    lista: list[str] = []

    for i in lista:

        lista.append(i)
        print(F"[{i}] was added!")

if __name__ == __name__:

    print(sandwitches("Hanburger", "Pomodoro", "Bacon"))