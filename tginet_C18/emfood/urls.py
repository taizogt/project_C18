from django.urls import path

from . import views

app_name = "emfood"
urlpatterns = [
    path("", views.index, name="index"),
    path("register", views.register, name="register"),
]