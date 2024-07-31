from rest_framework.viewsets import ModelViewSet
from django.shortcuts import render
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer


# Create your views here.
class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
