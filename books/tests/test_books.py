from django.contrib.auth.models import User
from rest_framework import status
import pytest
from books.models import Book
from model_bakery import baker
from faker import Faker

pytestmark = pytest.mark.django_db
fake = Faker()


@pytest.mark.django_db
class TestBooks:

    def test_if_anonymous_user_can_read_all_books(self, api_client):
        get_response = api_client.get("/api/store/books/")
        assert get_response.status_code == status.HTTP_200_OK

    def test_if_anonymous_user_can_read_specific_book(self, api_client):
        book = baker.make(Book)
        get_response = api_client.get(f"/api/store/books/{book.id}/")
        assert get_response.status_code == status.HTTP_200_OK
        assert get_response.data["isbn"] == book.isbn

    def test_if_anonymous_user_cannot_post_book(self, api_client):
        book = baker.make(Book)
        isbn = fake.isbn13()
        post_response = api_client.post(
            "/api/store/books/",
            {
                "title": book.title,
                "isbn": isbn,
                "date_of_publication": book.date_of_publication,
            },
        )
        assert post_response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_if_anonymous_user_cannot_patch_book(self, api_client):
        book = baker.make(Book)
        patch_response = api_client.patch(
            f"/api/store/books/{book.id}/",
            {"title": "A New Book"},
        )
        assert patch_response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_if_anonymous_user_cannot_delete_book(self, api_client):
        book = baker.make(Book)
        delete_response = api_client.delete(f"/api/store/books/{book.id}/")
        assert delete_response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_if_authenticated_user_can_post_book(self, api_client):
        book = baker.make(Book)
        isbn = fake.isbn13()
        api_client.force_authenticate(user=User())
        post_response = api_client.post(
            "/api/store/books/",
            {
                "title": book.title,
                "isbn": isbn,
                "date_of_publication": book.date_of_publication,
            },
        )
        assert post_response.status_code == status.HTTP_201_CREATED
        assert post_response.data["isbn"] == isbn

    def test_if_authenticated_user_can_patch_book(self, api_client):
        book = baker.make(Book)
        new_title = "A New Book"
        api_client.force_authenticate(user=User())
        patch_response = api_client.patch(
            f"/api/store/books/{book.id}/",
            {"title": new_title},
        )
        assert patch_response.status_code == status.HTTP_200_OK
        assert patch_response.data["title"] == new_title

    def test_if_authenticated_user_can_delete_book(self, api_client):
        book = baker.make(Book)
        api_client.force_authenticate(user=User())
        delete_response = api_client.delete(f"/api/store/books/{book.id}/")
        assert delete_response.status_code == status.HTTP_204_NO_CONTENT

    def test_if_authenticed_user_cannot_post_invalid_data(self, api_client):
        book = baker.make(Book)
        api_client.force_authenticate(user=User())
        post_response = api_client.post(
            "/api/store/books/",
            {
                "title": book.title,
                "isbn": "abcde",
                "date_of_publication": book.date_of_publication,
            },
        )
        assert post_response.status_code == status.HTTP_400_BAD_REQUEST
