from django.urls import path
from . import views

urlpatterns = [
    path("makedecks/", views.home, name="home"),
]