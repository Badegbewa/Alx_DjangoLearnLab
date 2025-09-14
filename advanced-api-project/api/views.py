from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer

class BookListCreateView(generics.ListCreateAPIView):
    """
    GET /books/ → list all books
    POST /books/ → create a new book (only if logged in)
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_permissions(self):
        if self.request.method == "POST":
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET /books/<id>/ → get one book
    PUT/PATCH /books/<id>/ → update it (only if logged in)
    DELETE /books/<id>/ → delete it (only if logged in)
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_permissions(self):
        if self.request.method in ["PUT", "PATCH", "DELETE"]:
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]

def get_queryset(self):
    queryset = Book.objects.all()
    year = self.request.query_params.get("year")
    if year:
        queryset = queryset.filter(publication_year=year)
    return queryset
