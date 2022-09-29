from django.contrib import admin
from django.urls import path, include
# from django.contrib import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("main.urls")),
    path("account/", include("account.urls")),
    path("administrator/", include("administrator.urls")),
] 
