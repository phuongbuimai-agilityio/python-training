from django.test import TestCase, Client
from django.urls import reverse

from users.models import UserModel


class TestLoginView(TestCase):
    def setUp(self):
        self.client = Client()
        self.login_url = reverse("users:login")
        self.redirect_url = reverse("index")

        # Create test user
        self.user_data = {
            "username": "testuser",
            "password": "testpass123",
            "email": "test@example.com",
            "gender": "Male",
        }
        self.user = UserModel.objects.create_user(
            username=self.user_data["username"],
            email=self.user_data["email"],
            password=self.user_data["password"],
            gender=self.user_data["gender"],
        )

    def test_login_url(self):
        # Act
        response = self.client.get(self.login_url)

        # Assert
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "users/login.html")

    def test_valid_login(self):
        # Arrange
        credentials = {
            "username": self.user_data["username"],
            "password": self.user_data["password"],
        }

        # Act
        response = self.client.post(self.login_url, credentials)

        # Assert
        self.assertRedirects(response, self.redirect_url)

    def test_invalid_username(self):
        # Arrange
        invalid_credentials = {
            "username": "wronguser",
            "password": self.user_data["password"],
        }

        # Act
        response = self.client.post(self.login_url, invalid_credentials)

        # Assert
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "users/login.html")
        self.assertFalse(response.wsgi_request.user.is_authenticated)
        self.assertFormError(
            response.context["form"],
            None,
            "Please enter a correct username and password. Note that both fields may be case-sensitive.",
        )

    def test_invalid_password(self):
        # Arrange
        invalid_credentials = {
            "username": self.user_data["username"],
            "password": "wrongpass",
        }

        # Act
        response = self.client.post(self.login_url, invalid_credentials)

        # Assert
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "users/login.html")
        self.assertFalse(response.wsgi_request.user.is_authenticated)
        self.assertFormError(
            response.context["form"],
            None,
            "Please enter a correct username and password. Note that both fields may be case-sensitive.",
        )

    def test_empty_form_submission(self):
        # Arrange
        empty_data = {"username": "", "password": ""}

        # Act
        response = self.client.post(self.login_url, empty_data)

        # Assert
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "users/login.html")
        self.assertFormError(
            response.context["form"], "username", "This field is required."
        )
        self.assertFormError(
            response.context["form"], "password", "This field is required."
        )

    def test_login_page_loads_correctly(self):
        # Act
        response = self.client.get(self.login_url)

        # Assert
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "users/login.html")
        self.assertContains(response, "<form")

    def test_redirect_authenticated_user(self):
        # Arrange
        self.client.force_login(self.user)

        # Act
        response = self.client.get(self.login_url)

        # Assert
        self.assertRedirects(response, self.redirect_url)

    def test_logout(self):
        # Arrange
        self.client.force_login(self.user)
        self.assertTrue(self.client.session.get("_auth_user_id"))

        # Act
        response = self.client.get(reverse("users:logout"))

        # Assert
        self.assertRedirects(response, self.redirect_url)
        self.assertFalse(self.client.session.get("_auth_user_id"))
