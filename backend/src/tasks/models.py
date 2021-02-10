from django.db import models


# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=120)
    description = models.CharField(max_length=500)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.title
