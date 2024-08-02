import datetime
from isbnlib import canonical, is_isbn10, is_isbn13
from django.core.exceptions import ValidationError


def validate_date(value):
    if value > datetime.date.today():
        raise ValidationError("Please provide a date in the past.")


def validate_isbn(value):
    isbn = canonical(value)
    if (not is_isbn13(isbn)) and (not is_isbn10(isbn)):
        raise ValidationError("Please provide a valid ISBN.")
