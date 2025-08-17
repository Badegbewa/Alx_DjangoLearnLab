import datetime
from rest_framework import serializers
from .models import Author, Book

class BookSerializer(serializers.ModelSerializer):
    """
    Turns Book objects into JSON and validates input for creating/updating Books.
    """
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']

    def validate_publication_year(self, value):
        """
        Make sure the year is not in the future.
        """
        current_year = datetime.date.today().year
        if value > current_year:
            raise serializers.ValidationError("publication_year cannot be in the future.")
        return value


class AuthorSerializer(serializers.ModelSerializer):
    """
    Shows the author's name AND their books.
    We nest BookSerializer to show a list of that author's books.
    """
    books = BookSerializer(many=True, read_only=True) 

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']
