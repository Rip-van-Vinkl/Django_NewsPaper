from django.contrib import admin
from django.urls import path
from djangonewspaper.views import index

urlpatterns = [
    path('index', index)
]