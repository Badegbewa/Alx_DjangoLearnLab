from relationship_app.models import Author, Book

# 1. Query all books by a specific author
author = Author.objects.get(name="Dan Brown")
books_by_author = Book.objects.filter(author=author)
print("Books by Dan Brown:", books_by_author)

from relationship_app.models import Library, Book
# 2. List all books in a library
library = Library.objects.get(name="library_name")
books_in_library = library.books.all()
print("Books in Central Library:", books_in_library)

from relationship_app.models import Librarian, Library
# 3. Retrieve the librarian for a library
librarian = Librarian.objects.get(library=library)
print("Librarian for Central Library:", librarian.name)
