from importlib.resources import path
from unittest.mock import patch
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='home'),
]
