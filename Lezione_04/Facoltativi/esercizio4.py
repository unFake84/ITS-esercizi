'''
Text Analysis:

    Create a function that takes a paragraph and
    counts the number of occurrences of each word.
    The function should print a report showing the
    most frequent words and their number of occurrences.
    You can use a for loop to iterate over the words in the
    text and a dictionary to store the occurrences.

'''

from string import punctuation

def countWords(text: str) -> None:

    d: dict[str, int] = {}
    text = text.lower().split()                                             # split restituisce una lista
    textList: list[str] = [text.strip(punctuation) for text in text]        # strip restituisce una stringa senza punteggiature (punctuation)
    orderedList: list[str] = []

    for word in textList:

        if word == "":
            continue

        if word not in d:
            d[word] = 1

        else:
            d[word] += 1
    #|1|
    orderedList = list(d.items())
    #|2|
    orderedList.sort(key=lambda x: x[1], reverse=True)

    print(f"Frequences: {d}")
    print(f"Ordered max>min :{orderedList}")

if __name__ == "__main__":

    # countWords("Nel mezzo del cammin di nostra vita mi ritrovai per una selva oscura che la diritta via era smarrita")
    # countWords(" Sopra la panca la capra campa, sotto la panca la capra crepa")
    # countWords("gatto cane gatto uccello cane gatto pesce uccello cane pesce topo cane gatto")
    countWords("apple banana apple banana cherry cherry date date date")








    #|1|
    # for words, occurences in d.items():

    #     if not orderedList:
    #         orderedList.append((words, occurences))

    #     else:
    #         orderedList.append((words, occurences))


    #|2| 90% (non garantiva l'ordine giusto di entrata e uscita)
    # for words, occurences in d.items():
    # if not orderedList:
    #     orderedList.append((words, occurences))
    # elif occurences > orderedList[-1][1]:
    #     orderedList.insert(-1, (words, occurences))
    # else:
    #     orderedList.append((words, occurences))