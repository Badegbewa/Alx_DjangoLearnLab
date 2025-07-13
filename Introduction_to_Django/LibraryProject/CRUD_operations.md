# Create
 
# Create a new book instance
from bookshelf.models import Book

book = Book(title="1984", author="George Orwell", publication_year=1949)
book.save()


# Retrieve

# Retrieve all books
from bookshelf.models import Book

books = Book.objects.all()
for b in books:
    print(b.title, b.author, b.publication_year)

>  **Output:**  
> 1984 George Orwell 1949

```python
# Retrieve  book
book = Book.objects.get(title="1984")
print(book.title, book.author, book.publication_year)
```

>  **Output:**  
> 1984 George Orwell 1949

---

# Update

```python
# Update book title
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
```

>  # Output  
> Book title updated successfully.

---

# Delete

```python
# Delete book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
```

>  *Output:**  
> Book deleted successfully.

```python
# Confirm deletion
Book.objects.all()
```

>  **Output:**  
> `<QuerySet []>` – no books found

