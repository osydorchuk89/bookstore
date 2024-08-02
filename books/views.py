from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend

from .filters import AuthorFilter, BookFilter
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer


# Create your views here.
class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.prefetch_related("books").all()
    serializer_class = AuthorSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]

    filterset_class = AuthorFilter
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ["full_name"]

    def destroy(self, request, *args, **kwargs):
        Book.objects.filter(authors__id=kwargs["pk"]).delete()
        return super().destroy(request, *args, **kwargs)


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all().prefetch_related("authors").all()
    serializer_class = BookSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]

    filterset_class = BookFilter
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ["title"]
