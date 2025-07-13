from bookshelf.models import Book

# Create a book and save it to the database
book = Book(title="1984", author="George Orwell", publication_year=1949)
book.save()

print(book)

