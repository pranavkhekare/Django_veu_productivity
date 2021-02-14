from django.contrib import admin
from.models import List


# Register your models here.
# Register your models here.
class Lists_admin(admin.ModelAdmin):
    fields = ('list_name', 'description')
    list_display = ('list_name', 'description', 'user_id', 'created_at', 'updated_at')


admin.site.register(List, Lists_admin)