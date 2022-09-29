from django.contrib.auth import get_user_model
from django.db import models


class Profile(models.Model):
    """model to extend the user profile"""
    user = get_user_model()
    user = models.ForeignKey(user, on_delete=models.CASCADE, )
    phone = models.PositiveIntegerField()
    email = models.EmailField(blank=True, null=True)
    home_address = models.TextField()

