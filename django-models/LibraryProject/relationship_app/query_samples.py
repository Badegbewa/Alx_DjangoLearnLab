from relationship_app.models import Author, Book, Library, Librarian

# 1. Query all books by a specific author
author = Author.objects.create(name="Dan Brown")
book = Book.objects.create(title="Lost Symbol", author=author)

# 2. List Books in a Library
library_name = "Central Library"
library = Library.objects.create(name=library_name)
library.books.add(book)

library = Library.objects.get(name=library_name)

books_in_library = library.books.all()
print(f"Books in {library.name}:", [book.title for book in books_in_library])

# 3. Retrieve the librarian for the library
librarian = Librarian.objects.create(name="John Eddy", library=library)
librarian = Librarian.objects.get(library=library)
print("Librarian:", librarian.name)
