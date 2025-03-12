'''
Album:
Write a function called make_album() that builds a dictionary describing a music album.
The function should take in an artist name and an album title, and it should return a dictionary containing these two pieces of information.
Use the function to make three dictionaries representing different albums.
Print each return value to show that the  dictionaries are storing the album information correctly.
Use None to add an optional parameter to make_album() that allows you to store the number of songs on an album.
If the calling line includes a value for the number of songs, add that value to the album’s dictionary.
Make at least one new function call that includes the number of songs on an album.
'''

def make_album(artist: str, album: str) -> dict:

    dictionary = {"nome": artist, "album": album}
    return dictionary

album = make_album("Pink Floyd", "Another brick in the wall")
album2 = make_album("Gigi D'Agostino", "L'Amour Toujours")
album3 = make_album("Vasco Rossi", "Bollicine")
print(f"{album['nome']}: {album['album']}")
print(f"{album2['nome']}: {album2['album']}")
print(f"{album3['nome']}: {album3['album']}")

# metodo alternativo
#print(album["artist"])
#print(album["album"])