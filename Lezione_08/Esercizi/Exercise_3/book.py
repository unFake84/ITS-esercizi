'''
    [1]
    Create a Book class containing the following attributes: title, author, isbn.
    The book class must contains the following methods:

        __str__,
        method to return a string representation of the book.

        from_string,
        a class method to create a Book instance from a string in the format "title, author, isbn".
        It means that you must use the class reference cls to create a new object of the Book class using a string.

    Example: 

    book_str: str = "La Divina Commedia, D. Alighieri, 999000666"
    divina_commedia: Book = Book.from_string(book_str)

    In this case, divina_commedia should be an instance of the Book class with:

        title = "La Divina Commedia"
        author = "D. Alighieri"
        isbn = "999000666"
'''

class Book:

    def __init__(self, title: str, author: str, isbn: str) -> None:
        self.title = title
        self.author = author
        self.isbn = isbn

    def __str__(self) -> str:
        return f"\ntitle = \"{self.title}\"\n"\
                f"author = \"{self.author}\"\n"\
                f"isbn = \"{self.isbn}\"\n"

    @classmethod
    def from_string(cls, stringa: str) -> "Book":
        div_stringa: list[str] = stringa.split(", ")
        oggetto: Book = cls(*div_stringa) #l'operatore * spacchetta automaticamene la lista (div_stringa)
        # oggetto: Book = cls(div_stringa[0].title(), div_stringa[1].title(), div_stringa[2]) <-- senza operatore *
        return oggetto

if __name__ == "__main__":

    book_str: str = "La Divina Commedia, D. Alighieri, 999000666"
    divina_commedia: Book = Book.from_string(book_str)
    print(divina_commedia)