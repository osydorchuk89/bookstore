from django.db import models


# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()

    class Meta:
        verbose_name_plural = "Authors"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Book(models.Model):
    title = models.CharField(max_length=500)
    isbn = models.CharField(max_length=20)
    date_of_publication = models.DateField()
    authors = models.ManyToManyField(Author, related_name="books")

    class Meta:
        verbose_name_plural = "Books"

    def __str__(self):
        return self.title
