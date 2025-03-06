from django.test import TestCase
from django.core.exceptions import ValidationError

from users.models import UserModel


class TestUserModel(TestCase):
    def setUp(self):
        self.valid_user_data = {
            "username": "testuser",
            "email": "test@example.com",
            "password": "testpassword123",
            "gender": "Male",
        }

    def test_required_fields(self):
        # Arrange
        user_data = self.valid_user_data.copy()
        del user_data["username"]

        # Act & Assert
        with self.assertRaises(ValidationError):
            user = UserModel(**user_data)
            user.full_clean()

        # Arrange
        user_data = self.valid_user_data.copy()
        del user_data["gender"]

        # Act & Assert
        with self.assertRaises(ValidationError):
            user = UserModel(**user_data)
            user.full_clean()

    def test_create_user(self):
        # Arrange
        user_data = self.valid_user_data.copy()

        # Act
        user = UserModel.objects.create_user(**user_data)

        # Assert
        self.assertEqual(user.username, user_data["username"])
        self.assertEqual(user.email, user_data["email"])
        self.assertEqual(user.gender, user_data["gender"])
        self.assertTrue(user.check_password(user_data["password"]))

    def test_read_user(self):
        # Arrange
        users = [
            UserModel(
                username=f"testuser{i}", email=f"test{i}@example.com", gender="Male"
            )
            for i in range(10)
        ]
        UserModel.objects.bulk_create(users)

        # Act: Retrieve a specific user by a known username
        expected_user = users[0]
        retrieved_user = UserModel.objects.get(username=expected_user.username)

        # Assert
        self.assertEqual(retrieved_user.username, expected_user.username)
        self.assertEqual(retrieved_user.email, expected_user.email)
        self.assertEqual(retrieved_user.gender, expected_user.gender)

    def test_update_user(self):
        """Test updating a user's email."""
        # Arrange
        user_data = self.valid_user_data.copy()
        user = UserModel.objects.create_user(**user_data)

        # Act
        new_email = "updated@example.com"
        user.email = new_email
        user.save()
        user.refresh_from_db()  # Ensures the updated value is actually stored in the database

        # Assert
        self.assertEqual(user.email, new_email)

    def test_update_user_invalid_email(self):
        """Test updating a user's email with an invalid email pattern."""
        # Arrange
        user_data = self.valid_user_data.copy()
        user = UserModel.objects.create_user(**user_data)

        # Act
        invalid_email = "invalid-email"
        user.email = invalid_email

        # Assert
        with self.assertRaises(ValidationError):
            user.full_clean()

    def test_delete_user(self):
        # Arrange
        user_data = self.valid_user_data.copy()
        user = UserModel.objects.create_user(**user_data)
        user_id = user.id

        # Act
        user.delete()

        # Assert
        with self.assertRaises(UserModel.DoesNotExist):
            UserModel.objects.get(id=user_id)

    def test_gender_choices(self):
        # Arrange
        valid_user_data = self.valid_user_data.copy()
        invalid_user_data = self.valid_user_data.copy()
        invalid_user_data["gender"] = "Invalid"

        # Act & Assert - Valid gender
        user = UserModel(**valid_user_data)
        user.full_clean()
        self.assertEqual(user.gender, "Male")

        # Act & Assert - Invalid gender
        with self.assertRaises(ValidationError):
            invalid_user = UserModel(**invalid_user_data)
            invalid_user.full_clean()
