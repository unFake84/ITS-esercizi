'''
Sandwiches:
Write a function that accepts a list of items a person wants on a sandwich.
The function should have one parameter that collects as many items as the function call provides,
and it should print a summary of the sandwich that’s being ordered. Call the function three times,
using a different number of arguments each time.
'''

def sandwiches(*args) -> None:

    lista: list[str] = []

    for i in args:

        lista.append(i)
        print(f"[{i}] was added!")

    print(f"Your sandwich is composed of: {', '.join(lista)}")

if __name__ == "__main__":

    print("-------------------------------------------------")
    print("First order:")
    sandwiches("Hamburger", "Pomodoro", "Bacon")
    print("-------------------------------------------------")
    print("Second order:")
    sandwiches("Cheese", "Ham")
    print("-------------------------------------------------")
    print("Third order:")
    sandwiches("Tomato", "Avocade", "Ribs", "Onion Rings")
    print("-------------------------------------------------")