from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.shortcuts import redirect

urlpatterns = [
    path("users/", include("users.urls")),
    path("students/", include("students.urls")),
    path("", lambda request: redirect("courses/", permanent=False)),
    path("courses/", include("courses.urls")),
    path("admin/", admin.site.urls),
]

# API URLS
# urlpatterns += [
#     path(settings.API_ROOT_ENDPOINT, include("config.api_router")),
# ]

if settings.DEBUG:
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
