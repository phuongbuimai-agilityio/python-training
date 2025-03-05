from django.db import models
from core.models import AbstractBaseModel
from config.settings.base import AUTH_USER_MODEL


class Student(AbstractBaseModel):
    """Represents a student who can enroll in courses."""

    user = models.OneToOneField(
        AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="student"
    )

    def __str__(self):
        return self.user.username
