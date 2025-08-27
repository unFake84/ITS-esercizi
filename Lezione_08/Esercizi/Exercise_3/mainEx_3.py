'''
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