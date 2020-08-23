from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("", include("hello_World.urls")),
]