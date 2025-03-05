from django.contrib import admin

from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    search_fields = ["user__username"]
    list_filter = ["user__gender"]
    list_display = ["id", "username", "email", "gender"]

    def get_queryset(self, request):
        return (
            super()
            .get_queryset(request)
            .filter(user__is_superuser=False, user__is_staff=False)
        )

    def id(self, obj):
        return obj.user.id

    def username(self, obj):
        return obj.user.username

    def email(self, obj):
        return obj.user.email

    def gender(self, obj):
        return obj.user.gender

    id.admin_order_field = "user__id"
    username.admin_order_field = "user__username"
    email.admin_order_field = "user__email"
    gender.admin_order_field = "user__gender"
