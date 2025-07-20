from relationship_app.models import Author, Book, Library, Librarian

# 1. Create an Author and retrieve using name
author_name = "Dan Brown"
Author.objects.create(name=author_name)
author = Author.objects.get(name=author_name) 

# 2. Create Books linked to the author
book1 = Book.objects.create(title="The Lost Symbol", author=author)
book2 = Book.objects.create(title="Angels and Demons", author=author)

# 3. Filter all books by the author
books_by_author = Book.objects.filter(author=author) 
print(f"Books by {author.name}:", [book.title for book in books_by_author])

# 4. Create a Library and retrieve using name
library_name = "Central Library"
Library.objects.create(name=library_name)
library = Library.objects.get(name=library_name)

# 5. Add books to the library
library.books.add(book1, book2)

# 6. Print books in the library
books_in_library = library.books.all()
print(f"Books in {library.name}:", [book.title for book in books_in_library])

# 7. Create a Librarian linked to the Library
Librarian.objects.create(name="John Eddy", library=library)

# 8. Retrieve the Librarian
librarian = Librarian.objects.get(library=library)
print(f"Librarian of {library.name}:", librarian.name)
