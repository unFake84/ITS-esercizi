'''
    [3]
    Create a Library class with the following attributes: books, members, total_books (i.e., a class attribute to
    keep track of the total number of Book instances).
    The library class must contain the following methods:

        add_book,
        to add a book to the library and increment total_books.

        remove_book,
        to remove a book from the library and decrement total_books.

        register_member,
        to add a member to the library.

        lend_book,
        to lend a book to a member. It should check if the book is available and if the member is registered.

        __str__,
        method to return a string representation of the library with the list of books and members.

        library_statistics,
        a class method to print the total number of books.
'''

from book import Book
from member import Member

class Library:

    total_books: int = 0
    real_total_books: int = 0

    def __init__(self) -> None:
        self.books: list[Book] = []
        self.members: list[Member] = []

    def add_book(self, book: Book|str) -> None:
        if isinstance(book, str):
            book = Book.from_string(book)

        self.books.append(book)
        Library.total_books += 1
        Library.real_total_books += 1

    def remove_book(self, book: Book|str) -> None:
        if isinstance(book, str):
            book = Book.from_string(book)

        if book in self.books:
            self.books.remove(book)
            Library.total_books -= 1

        else:
            raise ValueError(f":{book}: Not in Database")

    def register_member(self, member: Member|str) -> None:
        if isinstance(member, str):
            member = Member.from_string(member)

        self.members.append(member)

    def lend_book(self, book: Book, member: Member) -> None:
        if member not in self.members:
            raise ValueError(f"Member :{member.member_id}: not registered")

        if book not in self.books:
            raise ValueError(f"Book :{book.title}: not in database")

        self.books.remove(book)
        member.borrow_book(book)
        Library.total_books -= 1

    def __str__(self) -> str:
        catalogo: str = ""

        if self.books:
            catalogo += f"\nBOOKS:\n{'Cod':<8}{'Libro':<20}{'Autore':<15}\n"

            for libro in self.books:
                catalogo += f"{libro.isbn:<8}{libro.title if len(libro.title) <= 20 else libro.title[:17] + '..':<20}{libro.author:<15}\n"

        else:
            catalogo += "\nNo books in database\n"

        if self.members:
            catalogo += f"\nMEMBERS:\n{'Id':<8}{'Nome':<20}\n"

            for membro in self.members:
                catalogo += f"{membro.member_id:<8}{membro.name:<20}\n"

        else:
            catalogo += "\nNo members in database\n"

        return catalogo

    @classmethod
    def library_statistics(cls) -> None:
        print(
            f"Total numbers of books: {Library.real_total_books}\n"\
            f"Total numbers of books borrowed: {Library.real_total_books - Library.total_books}"    
            )

if __name__ == "__main__":

    book1: Book = Book.from_string("Il nome della rosa, Umberto Eco, 100001")
    book2: Book = Book.from_string("1984, George Orwell, 100002")
    book3: Book = Book.from_string("Orgoglio e pregiudizio, Jane Austen, 100003")
    book4: Book = Book.from_string("Delitto e castigo, Fëdor Dostoevskij, 100004")
    book5: Book = Book.from_string("I promessi sposi, Alessandro Manzoni, 100005")
    book6: Book = Book.from_string("Harry Potter e la pietra filosofale, J. K. Rowling, 100014")

    library: Library = Library()
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)
    library.add_book(book4)
    library.remove_book(book4)
    library.add_book(book5)
    library.add_book(book6)

    member1: Member = Member.from_string("Mario Rossi, 20001")
    member2: Member = Member.from_string("Giovanni Bianchi, 20002")
    member3: Member = Member.from_string("Lucia Verdi, 20003")
    member4: Member = Member.from_string("Francesca Neri, 20004")
    member5: Member = Member.from_string("Alessandro Gialli, 20005")

    library.register_member(member1)
    library.register_member(member2)
    library.register_member(member3)
    library.register_member(member4)
    library.register_member(member5)

    # library.lend_book(book3, member1) 
    library.lend_book(book5, member1)

    try:
        library.lend_book(book3,member1)

    except ValueError as err:
        print(f"{err}")

    #print(member1)
    print(library)
    library.library_statistics()























    # member6: Member = Member.from_string("Sara Blu, 20006")
    # member7: Member = Member.from_string("Lorenzo Marrone, 20007")
    # member8: Member = Member.from_string("Chiara Viola, 20008")
    # member9: Member = Member.from_string("Federico Arancio, 20009")
    # member10: Member = Member.from_string("Elena Rosa, 20010")





    # book6: Book = Book.from_string("Moby Dick, Herman Melville, 100006")
    # book7: Book = Book.from_string("Il signore degli anelli, J. R. R. Tolkien, 100007")
    # book8: Book = Book.from_string("La Divina Commedia, Dante Alighieri, 100008")
    # book9: Book = Book.from_string("Cime tempestose, Emily Brontë, 100009")
    # book10: Book = Book.from_string("Il vecchio e il mare, Ernest Hemingway, 100010")
    # book11: Book = Book.from_string("Don Chisciotte della Mancia, Miguel de Cervantes, 100011")
    # book12: Book = Book.from_string("Il piccolo principe, Antoine de Saint-Exupéry, 100012")
    # book13: Book = Book.from_string("Frankenstein, Mary Shelley, 100013")
    # book14: Book = Book.from_string("Harry Potter e la pietra filosofale, J. K. Rowling, 100014")
    # book15: Book = Book.from_string("Il codice da Vinci, Dan Brown, 100015")
    # book16: Book = Book.from_string("Ulisse, James Joyce, 100016")
    # book17: Book = Book.from_string("Le avventure di Sherlock Holmes, Arthur Conan Doyle, 100017")
    # book18: Book = Book.from_string("La fattoria degli animali, George Orwell, 100018")
    # book19: Book = Book.from_string("Il ritratto di Dorian Gray, Oscar Wilde, 100019")
    # book20: Book = Book.from_string("Guerra e pace, Lev Tolstoj, 100020")