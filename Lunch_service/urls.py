from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("menu_choice_app.urls", namespace="menu_choice_app"))
]
