'''
User Albums:
Start with your program from Exercise 8-7.
Write a while loop that allows users to enter an album’s artist and title.
Once you have that information, call make_album() with the user’s input and print the dictionary that’s created.
Be sure to include a quit value in the while loop.
'''

def make_album(artist: str, album: str, tracks = None) -> dict:

    dictionary: dict = {}
    dictionary["artista"] = artist
    dictionary["albums"] = album

    if tracks:

        dictionary["traccie"] = tracks

    return dictionary

if __name__ == "__main__":

    # print(make_album("Pink Floyd", "Another brick in the wall"))
    # print(make_album("Gigi D'Agostino", "L'Amour Toujours"))
    # print(make_album("Vasco Rossi", "Bollicine", 8))

    while True:
        
        user1: str = (input("Inserire Artista: "))

        if user1 == "exit":
            
            break
    
        user2: str = (input("Inserire Album: "))

        if user1 == "exit":

            break

        make_album(artist = user1, album = user2)