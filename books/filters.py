from django_filters.rest_framework import FilterSet

from .models import Author, Book


# filters for selecting authors by full name (fully or partially) and date of birth (less than or equal and greater than or equal)
class AuthorFilter(FilterSet):
    class Meta:
        model = Author
        fields = {
            "full_name": ["exact", "contains"],
            "date_of_birth": ["gte", "lte"],
        }


# filters for selecting books by title (fully or partially) and date of publication (less than or equal and greater than or equal)
class BookFilter(FilterSet):
    class Meta:
        model = Book
        fields = {
            "title": ["exact", "contains"],
            "date_of_publication": ["gte", "lte"],
        }
