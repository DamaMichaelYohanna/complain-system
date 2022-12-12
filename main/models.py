from django.contrib.auth import get_user_model
from django.db import models

user = get_user_model()


class Complain(models.Model):
    """model for complains"""
    owner = models.ForeignKey(user, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=300, )
    body = models.TextField()
    status = models.CharField(max_length=30,
                              default="pending",
                              choices=(
                                  ("pending", 'pending'),
                                  ("open", 'open'),
                                  ("viewed", "viewed"),
                                  ("Resolved", "Resolved")
                              )
                              )
    attachment = models.FileField()
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"{self.title}"

