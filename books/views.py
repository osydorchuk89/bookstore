from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

from .filters import AuthorFilter, BookFilter
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer


class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.prefetch_related("books").all()
    serializer_class = AuthorSerializer

    filterset_class = AuthorFilter
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ["full_name"]

    # override the default destroy method to make sure that if an author is removed, all his/her books are also removed
    def destroy(self, request, *args, **kwargs):
        Book.objects.filter(authors__id=kwargs["pk"]).delete()
        return super().destroy(request, *args, **kwargs)


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all().prefetch_related("authors").all()
    serializer_class = BookSerializer

    filterset_class = BookFilter
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ["title"]
