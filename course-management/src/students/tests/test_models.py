from django.test import TestCase
from django.core.exceptions import ValidationError
from courses.models import Course, Enrollment
from students.models import Student
from users.models import UserModel


class TestStudent(TestCase):
    def setUp(self):
        self.user_data = {
            "username": "testuser",
            "password": "testpass",
            "email": "test@example.com",
        }
        self.user = UserModel.objects.create_user(**self.user_data)

    def test_required_fields(self):
        # Arrange
        student = Student()

        # Act & Assert
        with self.assertRaises(ValidationError):
            student.full_clean()

    def test_crud_operations(self):
        # Arrange
        user = self.user

        # Act - Create
        student = Student.objects.create(user=user)

        # Assert - Create
        self.assertEqual(Student.objects.count(), 1)

        # Act - Read
        retrieved_student = Student.objects.get(uuid=student.uuid)

        # Assert - Read
        self.assertEqual(retrieved_student.user.username, self.user_data["username"])

        # Act - Delete
        student.delete()

        # Assert - Delete
        self.assertEqual(Student.objects.count(), 0)

    def test_user_relationship(self):
        # Arrange
        student = Student.objects.create(user=self.user)

        # Act & Assert - Test user relationship
        self.assertEqual(student.user.username, self.user_data["username"])
        self.assertEqual(student.user.email, self.user_data["email"])

    def test_cascade_delete_from_user(self):
        # Act
        self.user.delete()

        # Assert
        self.assertEqual(Student.objects.count(), 0)

    def test_enrollments_relationship(self):
        # Arrange
        student = Student.objects.create(user=self.user)
        course1 = Course.objects.create(title="Course 1")
        course2 = Course.objects.create(title="Course 2")

        # Act
        Enrollment.objects.create(student=student, course=course1)
        Enrollment.objects.create(student=student, course=course2)

        # Assert
        self.assertEqual(student.enrollment_set.count(), 2)
        self.assertIn(
            course1, [enrollment.course for enrollment in student.enrollment_set.all()]
        )
        self.assertIn(
            course2, [enrollment.course for enrollment in student.enrollment_set.all()]
        )
