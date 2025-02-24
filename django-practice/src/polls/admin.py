from django.contrib import admin

from .models import Course, Enrollment, Student, User


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_filter = ["is_active"]
    list_display = ["title", "is_active"]
    actions = ["make_active", "make_inactive"]

    @admin.action(description="Mark selected courses as active")
    def make_active(self, request, queryset):
        updated_count = queryset.update(is_active=True)
        self.message_user(request, f"{updated_count} course(s) were marked as active.")

    @admin.action(description="Mark selected courses as inactive")
    def make_inactive(self, request, queryset):
        updated_count = queryset.update(is_active=False)
        self.message_user(
            request, f"{updated_count} course(s) were marked as inactive."
        )


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    search_fields = ["user__username"]
    list_filter = ["user"]


@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_filter = ["student", "course"]
    list_display = ["student", "course", "enrolled_at"]


admin.site.register(User)
