from django.db import models
from core.models import AbstractBaseModel
from users.models import UserModel


class Student(AbstractBaseModel):
    """Represents a student who can enroll in courses."""

    user = models.OneToOneField(UserModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
