from django.contrib import admin

from .models import UserModel


@admin.register(UserModel)
class UserModelAdmin(admin.ModelAdmin):
    search_fields = ["username"]
    list_display = ["id", "username", "email", "gender", "is_superuser", "is_staff"]
