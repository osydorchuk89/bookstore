from django.contrib import admin
from .models import Author, Book


# Register your models here.
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    ordering = ("full_name",)
    list_display = ("full_name", "date_of_birth", "author_books")

    def author_books(self, obj):
        return ", ".join([book.title for book in obj.books.all()])


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    ordering = ("title",)
    list_display = ("title", "book_authors", "isbn", "date_of_publication")

    def book_authors(self, obj):
        return ", ".join([author.full_name for author in obj.authors.all()])
