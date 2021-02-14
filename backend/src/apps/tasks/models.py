from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
class Task(models.Model):
    user_id = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=120)
    description = models.CharField(max_length=500, default='')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.title
