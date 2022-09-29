from django.urls import path

from account import views

urlpatterns = [
    path("login", views.LoginPage.as_view(), name="login"),
    path("logout", views.logged_out, name="logout"),
]