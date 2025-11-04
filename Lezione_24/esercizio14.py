'''
Progettare un sistema di gestione della biblioteca con i seguenti requisiti:

    Classe Book:
        Attributi:
            book_id: str - Identificatore di un libro.
            title: str - titolo del libro.
            author: str - autore del libro
            is_borrowed: boolean - booleano che indica se il libro è in prestito o meno.
        Metodi:
            borrow()-Contrassegna il libro come preso in prestito se non è già preso in prestito.
            return_book()- Contrassegna il libro come restituito.

    Classe Member:
        Attributi:
            member_id: str - identificativo del membro.
            name: str - il nome del membro.
            borrowed_books: list[Book] - lista dei libri presi in prestito.
        Metodi:
            borrow_book(book): aggiunge il libro nella lista borrowed_books se non è già stato preso in prestito.
            return_book(book): rimuove il libro dalla lista borrowed_books.

    Classe Library:
        Attributi:
            books: dict[str, Book] - dizionario che ha per chiave l'id del libro e per valore l'oggetto Book
            members: dict[str, Member] - dizionario che ha per chiave l'id del membro e per valore l'oggetto Membro
        Metodi:
            add_book(book_id: str, title: str, author: str): Aggiunge un nuovo libro nella biblioteca.
            register_member(member_id:str, name: str): Iscrive un nuovo membro nella biblioteca.
            borrow_book(member_id: str, book_id: str): Permette al membro di prendere in prestito il libro.
            return_book(member_id: str, book_id: str): Permette al membro di restituire il libro.
            get_borrowed_books(member_id): list[Book] - restituisce la lista dei libri presi in prestito dal membro.
'''

class Book:
    '''
        Attributi:
            book_id: str - Identificatore di un libro.
            title: str - titolo del libro.
            author: str - autore del libro
            is_borrowed: boolean - booleano che indica se il libro è in prestito o meno.
        Metodi:
            borrow()-Contrassegna il libro come preso in prestito se non è già preso in prestito.
            return_book()- Contrassegna il libro come restituito.
    '''
    def __init__(self, book_id: str, title: str, author: str) -> None:
        self.book_id: str = book_id
        self.title: str = title
        self.author: str = author
        self.is_borrowed: bool = False
    
    def borrow(self) -> None:
        if not self.is_borrowed:
            self.is_borrowed = True
    
    def return_book(self) -> None:
        if self.is_borrowed:
            self.is_borrowed = False

class Member:
    '''
        Attributi:
            member_id: str - identificativo del membro.
            name: str - il nome del membro.
            borrowed_books: list[Book] - lista dei libri presi in prestito.
        Metodi:
            borrow_book(book): aggiunge il libro nella lista borrowed_books se non è già stato preso in prestito.
            return_book(book): rimuove il libro dalla lista borrowed_books.
    '''
    def __init__(self, member_id: str, name: str, borrowed_books: list[Book]|None = None) -> None:
        self.member_id: str = member_id
        self.name: str = name
        self.borrowed_books: list[Book] = borrowed_books if borrowed_books is not None else []
    
    def borrow_book(self, book: Book) -> None:
        if not book.is_borrowed:
            self.borrowed_books.append(book)
            book.borrow()
        else:
            print("Book is already borrowed")
    
    def return_book(self, book: Book) -> None:
        if book.book_id in [libro.book_id for libro in self.borrowed_books]: # evitiamo crash
            self.borrowed_books.remove(book)
            book.return_book()

class Library:
    '''
        Attributi:
            books: dict[str, Book] - dizionario che ha per chiave l'id del libro e per valore l'oggetto Book
            members: dict[str, Member] - dizionario che ha per chiave l'id del membro e per valore l'oggetto Membro
        Metodi:
            add_book(book_id: str, title: str, author: str): Aggiunge un nuovo libro nella biblioteca.
            register_member(member_id:str, name: str): Iscrive un nuovo membro nella biblioteca.
            borrow_book(member_id: str, book_id: str): Permette al membro di prendere in prestito il libro.
            return_book(member_id: str, book_id: str): Permette al membro di restituire il libro.
            get_borrowed_books(member_id): list[Book] - restituisce la lista dei libri presi in prestito dal membro.
    '''
    def __init__(self, books: dict[str, Book] | None = None, members: dict[str, Member] | None = None) -> None:
        self.books = books if books is not None else {}
        self.members = members if members is not None else {}
    
    def add_book(self, book_id: str, title: str, author: str) -> None:
        if book_id not in self.books:
            self.books[book_id] = Book(book_id, title, author)
    
    def register_member(self, member_id: str, name: str) -> None:
        if member_id not in self.members:
            self.members[member_id] = Member(member_id, name)
    
    def borrow_book(self, member_id: str, book_id: str) -> None:
        if member_id in self.members and book_id in self.books:
            self.members[member_id].borrow_book(self.books[book_id])
        
        else:
            print("Member not found") if book_id in self.books else print("Book not found")
    
    def return_book(self, member_id: str, book_id: str) -> None:
        id_libri: list[str] = [l.book_id for l in self.members[member_id].borrowed_books]
        if book_id in id_libri:
            self.members[member_id].return_book(self.books[book_id])
        
        else:
            print("Book not borrowed by this member")
    
    def get_borrowed_books(self, member_id) -> list[Book]:
        return [libro.title for libro in self.members[member_id].borrowed_books]