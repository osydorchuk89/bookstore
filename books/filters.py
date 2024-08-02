from django_filters.rest_framework import FilterSet

from .models import Author, Book


class AuthorFilter(FilterSet):
    class Meta:
        model = Author
        fields = {
            "full_name": ["exact", "contains"],
            "date_of_birth": ["gte", "lte"],
        }


class BookFilter(FilterSet):
    class Meta:
        model = Book
        fields = {
            "title": ["exact", "contains"],
            "date_of_publication": ["gte", "lte"],
        }
