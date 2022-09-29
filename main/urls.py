from django.urls import path

from main import views

urlpatterns = [
    path("", views.index, name="home"),
    path("complain", views.complain, name="complain"),
    path("complain/track", views.track_complain, name="about"),
    path("contact", views.contact, name="contact"),
    path("about", views.about, name="about"),

    path("about", views.about, name="about"),
]