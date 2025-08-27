'''
    [4]
    Finally, write a simple driver program.
    After creating a library, you should begin by creating instances of Book and Member.
    Wherever appropriate, use class methods (such as from_string) to instantiate objects from strings, improving clarity and modularity.

    Once your objects are created, simulate some basic library operations:

        1. Register new members to the library.
            This could involve adding Member objects to a collection maintained by the library.

        2. Add books to the library’s collection.

        3. Lend books to members.
            This will involve marking a book as borrowed and associating it with a specific member.

        4. At each significant step, print the state of the library to track how it changes:
                before lending any book,
                after books have been lent.
'''

from book import Book
from member import Member
from library import Library
import random

library: Library = Library()
print(library)

books_list = [
    Book.from_string("Il nome della rosa, Umberto Eco, 100001"),
    Book.from_string("1984, George Orwell, 100002"),
    Book.from_string("Orgoglio e pregiudizio, Jane Austen, 100003"),
    Book.from_string("Delitto e castigo, Fëdor Dostoevskij, 100004"),
    Book.from_string("I promessi sposi, Alessandro Manzoni, 100005"),
    Book.from_string("Moby Dick, Herman Melville, 100006"),
    Book.from_string("Il signore degli anelli, J. R. R. Tolkien, 100007"),
    Book.from_string("La Divina Commedia, Dante Alighieri, 100008"),
    Book.from_string("Cime tempestose, Emily Brontë, 100009"),
    Book.from_string("Il vecchio e il mare, Ernest Hemingway, 100010"),
    Book.from_string("Don Chisciotte della Mancia, Miguel de Cervantes, 100011"),
    Book.from_string("Il piccolo principe, Antoine de Saint-Exupéry, 100012"),
    Book.from_string("Frankenstein, Mary Shelley, 100013"),
    Book.from_string("Harry Potter e la pietra filosofale, J. K. Rowling, 100014"),
    Book.from_string("Il codice da Vinci, Dan Brown, 100015"),
    Book.from_string("Ulisse, James Joyce, 100016"),
    Book.from_string("Le avventure di Sherlock Holmes, Arthur Conan Doyle, 100017"),
    Book.from_string("La fattoria degli animali, George Orwell, 100018"),
    Book.from_string("Il ritratto di Dorian Gray, Oscar Wilde, 100019"),
    Book.from_string("Guerra e pace, Lev Tolstoj, 100020")
]

for book in books_list:
    library.add_book(book)

members_list: list[Member] = [
    Member.from_string("Mario Rossi, 20001"),
    Member.from_string("Giovanni Bianchi, 20002"),
    Member.from_string("Lucia Verdi, 20003"),
    Member.from_string("Francesca Neri, 20004"),
    Member.from_string("Alessandro Gialli, 20005"),
    Member.from_string("Sara Blu, 20006"),
    Member.from_string("Lorenzo Marrone, 20007"),
    Member.from_string("Chiara Viola, 20008"),
    Member.from_string("Federico Arancio, 20009"),
    Member.from_string("Elena Rosa, 20010")
]

for member in members_list:
    library.register_member(member)

for _ in range(random.randint(1, 20)):
    book: Book = random.choice(books_list)
    member: Member = random.choice(members_list)

    try:
        library.lend_book(book, member)
        print(f":{book.title}: lent to :{member.member_id}:")
    except ValueError as err:
        print(f"Can not lent :{book.title}: to :{member.member_id}: {err}")

for member in library.members:

    if member.borrowed_books:
        print(member)
    else:
        print(f"Member :{member.member_id}: has no books")

print(library)
Library.library_statistics()