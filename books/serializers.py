from rest_framework.serializers import ModelSerializer
from .models import Author, Book


class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = ["first_name", "last_name", "date_of_birth", "books"]


class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = ["title", "isbn", "date_of_publication", "authors"]
