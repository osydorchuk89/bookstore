from django.db import models

from .validators import validate_date, validate_isbn


# Create your models here.
class Author(models.Model):

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(validators=[validate_date])
    full_name = models.CharField(max_length=200, default="", editable=False)

    class Meta:
        verbose_name_plural = "Authors"
        ordering = ["full_name"]

    def save(self, *args, **kwargs):
        self.full_name = f"{self.first_name} {self.last_name}"
        super(Author, self).save(*args, **kwargs)

    def __str__(self):
        return self.full_name


class Book(models.Model):
    title = models.CharField(max_length=500)
    isbn = models.CharField(max_length=20, unique=True, validators=[validate_isbn])
    date_of_publication = models.DateField(validators=[validate_date])
    authors = models.ManyToManyField(Author, related_name="books")

    class Meta:
        verbose_name_plural = "Books"
        ordering = ["title"]

    def __str__(self):
        return self.title
