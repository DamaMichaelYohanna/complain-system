from django.contrib.auth import get_user_model
from django.db import models

user = get_user_model()


class Complain(models.Model):
    """model for complains"""
    owner = models.ForeignKey(user, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=300, )
    body = models.TextField()
    attachment = models.FileField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}"


class ComplainTrack(models.Model):
    status = models.CharField(max_length=30,
                              default="pending",
                              choices=(
                                  ("pending", 'pending'),
                                  ("viewed", "viewed"),
                                  ("replied", "replied")
                              )
                              )
    complain = models.ForeignKey(Complain, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.complain}"
