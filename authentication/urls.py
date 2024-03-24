from django.urls import path, include
from .views import (
    first_page,
)

urlpatterns = [
    path("", first_page, name="first-page"),
    path("account/", include("django.contrib.auth.urls")),
]
