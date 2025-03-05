from django.db import models
from core.models import AbstractBaseModel


class Course(AbstractBaseModel):
    """Represents a Course that students can enroll in."""

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Enrollment(AbstractBaseModel):
    """Represents a student's enrollment in a course."""

    student = models.ForeignKey("students.Student", on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrolled_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ["student", "course"]

    def __str__(self):
        return f"{self.student.user.username} enrolled in {self.course.title}"
