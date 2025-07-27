from django.contrib.auth.decorators import permission_required
from django.shortcuts import render
from .models import Book

# View books (only if user has 
@permission_required('bookshelf.can_view', raise_exception=True)
def view_books(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/view_books.html', {'books': books})

# Create a new book (only if user has can_create permission)
@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    return render(request, 'bookshelf/create_book.html')

# Edit a book (only if user has can_edit permission)
@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, book_id):
    return render(request, 'bookshelf/edit_book.html')

