from django.urls import path

from . import views

app_name = "emfood"
urlpatterns = [
    path("", views.index, name="index"),
    path("register", views.register, name="register"),
    path("share",views.share, name="share"), 
    path("share",views.sharefood, name="sharefood"),
    #path("", views.delete, name="delete"),
]