glossario: dict[str, str] = {
                    "if": "if true enters the instruction block",
                    "while": "allows a loop to be started, thanks to the use of a counter",
                    "for": "allows automatic iteration, without the use of a counter",
                    "Any": "allows any type of data to be inserted in lists, sets and dictionaries ",
                    ".pop()": "allows the removal of elements in lists, sets and dictionaries",
}

print("-----------------------------------------------------------------------")

for key, value in glossario.items():

    print(f"{key}:\n{value}")
    print("-----------------------------------------------------------------------")