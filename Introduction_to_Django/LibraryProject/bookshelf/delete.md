# delete.md

# Get the book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
Book.objects.all()

 # Output:  
> Book deleted successfully.