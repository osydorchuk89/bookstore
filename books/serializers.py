from rest_framework.serializers import ModelSerializer, SlugRelatedField

from .models import Author, Book


class AuthorSerializer(ModelSerializer):
    books = SlugRelatedField(many=True, slug_field="title", queryset=Book.objects.all())

    class Meta:
        model = Author
        fields = ["id", "first_name", "last_name", "date_of_birth", "books"]

    def get_full_name(self, author: Author):
        return f"{author.first_name} {author.last_name}"


class BookSerializer(ModelSerializer):
    authors = SlugRelatedField(many=True, slug_field="full_name", queryset=Author.objects.all())

    class Meta:
        model = Book
        fields = ["id", "title", "isbn", "date_of_publication", "authors"]
