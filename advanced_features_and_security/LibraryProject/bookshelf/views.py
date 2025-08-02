from django.contrib.auth.decorators import permission_required
from django.shortcuts import render
from .models import Book

@permission_required('bookshelf.can_view', raise_exception=True)
def view_books(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/view_books.html', {'books': books})

@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    return render(request, 'bookshelf/create_book.html')

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, book_id):
    return render(request, 'bookshelf/edit_book.html')

def book_list(request):
    books = Book.objects.all() 
    return render(request, 'bookshelf/book_list.html', {'books': books})


Book.objects.filter(title__icontains=book_list)

from django.shortcuts import render
from .forms import ExampleForm

def example_form_view(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            # Process the data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            # Save or use the data securely here
            return render(request, 'bookshelf/success.html')
    else:
        form = ExampleForm()
    
    return render(request, 'bookshelf/form_example.html', {'form': form})

