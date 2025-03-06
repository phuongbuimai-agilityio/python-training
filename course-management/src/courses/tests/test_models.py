from django.test import TestCase
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from courses.models import Course, Enrollment
from students.models import Student
from users.models import UserModel


class TestCourse(TestCase):
    def setUp(self):
        self.course_data = {
            "title": "Test Course",
            "description": "Test Description",
            "is_active": True,
        }

    def test_required_fields(self):
        # Arrange
        course = Course(description="Test")

        # Act & Assert
        with self.assertRaises(ValidationError):
            course.full_clean()

    def test_default_values(self):
        # Arrange
        course_title = "Test Course"

        # Act
        course = Course.objects.create(title=course_title)

        # Assert
        self.assertTrue(course.is_active)
        self.assertEqual(course.description, "")

    def test_crud_operations(self):
        # Arrange - Create test data
        course_data = self.course_data

        # Act - Create
        course = Course.objects.create(**course_data)

        # Assert - Create
        self.assertEqual(Course.objects.count(), 1)

        # Act - Read
        retrieved_course = Course.objects.get(uuid=course.uuid)

        # Assert - Read
        self.assertEqual(retrieved_course.title, course_data["title"])

        # Arrange - Update
        new_title = "Updated Course"

        # Act - Update
        course.title = new_title
        course.save()
        updated_course = Course.objects.get(uuid=course.uuid)

        # Assert - Update
        self.assertEqual(updated_course.title, new_title)

        # Act - Delete
        course.delete()

        # Assert - Delete
        self.assertEqual(Course.objects.count(), 0)


class TestEnrollment(TestCase):
    def setUp(self):
        self.user = UserModel.objects.create_user(
            username="testuser", password="testpass"
        )
        self.student = Student.objects.create(user=self.user)
        self.course = Course.objects.create(title="Test Course")

    def test_required_fields(self):
        # Arrange
        enrollment = Enrollment()

        # Act & Assert
        with self.assertRaises(ValidationError):
            enrollment.full_clean()

    def test_crud_operations(self):
        # Arrange
        student = self.student
        course = self.course

        # Act - Create
        enrollment = Enrollment.objects.create(student=student, course=course)

        # Assert - Create
        self.assertEqual(Enrollment.objects.count(), 1)

        # Act - Read
        retrieved_enrollment = Enrollment.objects.get(uuid=enrollment.uuid)

        # Assert - Read
        self.assertEqual(retrieved_enrollment.student, student)
        self.assertEqual(retrieved_enrollment.course, course)

        # Act - Delete
        enrollment.delete()

        # Assert - Delete
        self.assertEqual(Enrollment.objects.count(), 0)

    def test_unique_constraint(self):
        # Arrange
        student = self.student
        course = self.course
        Enrollment.objects.create(student=student, course=course)

        # Act & Assert
        with self.assertRaises(IntegrityError):
            Enrollment.objects.create(student=student, course=course)

    def test_relationships(self):
        # Arrange
        enrollment = Enrollment.objects.create(student=self.student, course=self.course)

        # Act & Assert - Test course relationship
        self.assertEqual(enrollment.course.title, "Test Course")

        # Act & Assert - Test student relationship
        self.assertEqual(enrollment.student.user.username, "testuser")

        # Act - Test cascade delete
        self.course.delete()

        # Assert
        self.assertEqual(Enrollment.objects.count(), 0)
