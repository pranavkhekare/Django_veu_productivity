from django.contrib import admin
from .models import Task


# Register your models here.
class Task_admin(admin.ModelAdmin):
    fields = ('title', 'description')
    list_display = ('title', 'description', 'created_at', 'updated_at')


admin.site.register(Task, Task_admin)