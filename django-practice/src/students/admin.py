from django.contrib import admin

from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    search_fields = ["user__username"]
    list_filter = ["user__gender"]
    list_display = ["username", "email", "gender", "is_superuser"]

    def username(self, obj):
        return obj.user.username

    def email(self, obj):
        return obj.user.email

    def gender(self, obj):
        return obj.user.gender

    username.admin_order_field = "user__username"
    email.admin_order_field = "user__email"
    gender.admin_order_field = "user__gender"

    def is_superuser(self, obj):
        return obj.user.is_superuser

    is_superuser.admin_order_field = "user__is_superuser"
    is_superuser.boolean = True
