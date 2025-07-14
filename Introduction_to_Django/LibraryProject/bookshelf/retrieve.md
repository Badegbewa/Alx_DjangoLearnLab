# retrieve.md
books = Book.objects.all()

for b in book:
    print(b.title, b.author, b.publication_year)

# output
1984 Goerge Orwell 1949
