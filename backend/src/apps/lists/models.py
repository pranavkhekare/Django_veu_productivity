from django.db import models
from django.contrib.auth import get_user_model


class List(models.Model):
    user_id = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, default=1)
    list_name = models.CharField(max_length=50)
    description = models.TextField(null=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.list_name


class List_items(models.Model):
    parent_list = models.ForeignKey(List, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.text