from django.contrib import admin
from django.contrib.auth.hashers import make_password

from .models import UserModel


@admin.register(UserModel)
class UserModelAdmin(admin.ModelAdmin):
    search_fields = ["username"]
    list_display = ["id", "username", "email", "gender", "is_superuser", "is_staff"]

    def save_model(self, request, obj, form, change):
        """
        Overrides the save_model method to hash the password before saving the user object.

        Args:
            request (HttpRequest): The current request object.
            obj (Model): The user model instance being saved.
            form (ModelForm): The form instance used to update the model.
            change (bool): A boolean indicating whether the model is being changed or added.

        Notes:
            The password is hashed only if the object is new or if the password field is updated.
        """
        if not change or form.cleaned_data.get("password"):
            obj.password = make_password(obj.password)
        super().save_model(request, obj, form, change)
