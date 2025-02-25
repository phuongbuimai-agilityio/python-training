from django.db import models
from django.contrib.auth.models import AbstractUser

from core.constants import BaseChoiceEnum


class UserModel(AbstractUser):
    """
    Custom user model that includes "created", "modified" timestamp, "gender" fields.
    """

    class GenderChoices(BaseChoiceEnum):
        MALE = "Male"
        FEMALE = "Female"
        OTHER = "Other"

    gender = models.CharField(max_length=6, choices=GenderChoices.choices())

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
        app_label = "users"

    def __str__(self):
        return self.username
