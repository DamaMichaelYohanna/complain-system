from django.urls import path

from account import views

urlpatterns = [
    path("login", views.login_page, name="login"),
    path("logout", views.logged_out, name="logout"),
]