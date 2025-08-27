'''
[2]
Create a Member class with the following attributes: name, member_id, borrowed_books.
The member class must contain the following methods:

    borrow_book,
    to add a book to the borrowed_books list.

    return_book,
    to remove a book from the borrowed_books list.

    __str__,
    method to return a string representation of the member.

    from_string,
    a class method to create a Member instance from a string in the format "name, member_id".
    It means that you must use the class reference cls to create a new object of the Member class using a string.
'''

from book import Book

class Member:

    def __init__(self, name: str, member_id: str, borrowed_books: list[Book]|None = None) -> None:
        self.name = name
        self.member_id = member_id
        self.borrowed_books = borrowed_books if borrowed_books is not None else None

    def borrow_book(self, book: Book) -> None:
        if self.borrowed_books is not None:

            if book not in self.borrowed_books:
                self.borrowed_books.append(book)
            else:
                raise ValueError(f":{book.title}: allready in list")

        else:
            self.borrowed_books = [book]

    def return_book(self, book: Book) -> None:
        if self.borrowed_books is not None:

            if book in self.borrowed_books:
                self.borrowed_books.remove(book)
            else:
                raise ValueError(f":{book.title}: not in member :{self.member_id}: list")

        else:
            raise ValueError(f"Member :{self.member_id}: has no book on loan")
        
        if self.borrowed_books == []:
            self.borrowed_books = None
    
    def __str__(self) -> str:
        final_string: str = f"Member :{self.member_id}: borrowed books:\n"

        if self.borrowed_books is not None:
            qnti: int = 0

            for book in self.borrowed_books:
                qnti += 1
                final_string += f"\n[{qnti}]"
                final_string += str(book) + "-"*50
        
        elif self.borrowed_books is None:
            final_string += "No borrowed books"
        
        return final_string if self.borrowed_books is not None else f"Member :{self.member_id}: has no book on loan"
    
    @classmethod
    def from_string(cls, stringa: str) -> "Member":
        div_stringa: list[str] = stringa.split(", ")
        oggetto: Member = cls(*div_stringa)

        return oggetto

if __name__ == "__main__":

    print("TEST 1")
    member_1: Member = Member("Mario", "12345")
    print(member_1)

    print("TEST 2")
    stringa1: str = "Giovanni, 12346"
    member_2: Member = Member.from_string(stringa1)
    print(member_2)

    print("TEST 3")
    libro1: Book = Book.from_string("La Divina Commedia, D. Alighieri, 999000666")
    libro2: Book = Book.from_string("Il Mio Primo Bach, Bach, 999010699")
    libro3: Book = Book.from_string("I Pilastri Della Terra, K. Follet, 889000901")
    libro4: Book = Book.from_string("Il Cliente, J. Chrisman, 889000902")

    member_1.borrow_book(libro1)
    
    try:
        member_1.borrow_book(libro1) # solleva un ValueError (giusto)

    except ValueError as err:
        print(f"Error: {err}")

    member_1.borrow_book(libro2)
    member_1.return_book(libro1)
    print(member_1)

    member_2.borrow_book(libro3)
    # member_2.borrow_book(libro1) assegna cmq lo stesso libro se già assegnato (>>Library)
    member_2.borrow_book(libro4)
    print(member_2)

    try:
        member_2.return_book(libro1)

    except ValueError as err:
        print(f"Error: {err}")
    
    member_1.return_book(libro2)
    print(member_1)