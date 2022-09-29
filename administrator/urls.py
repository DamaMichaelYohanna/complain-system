from django.urls import path
from administrator import views
urlpatterns = [
    path("", views.all_complains, name="complains"),
    path('verify', views.verify, name="verify complain"),
]