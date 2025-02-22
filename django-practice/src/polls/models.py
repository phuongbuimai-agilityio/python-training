from django.db import models

from core.models import AbstractBaseModel


class User(AbstractBaseModel):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.username


class Course(AbstractBaseModel):
    """Represents a Course that students can enroll in."""

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Student(AbstractBaseModel):
    """Student profile linked to a User."""

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Enrollment(AbstractBaseModel):
    """Tracks which students are enrolled in which courses."""

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrolled_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ["student", "course"]

    def __str__(self):
        return f"{self.student.user.username} enrolled in {self.course.title}"
