# Generated by Django 3.1.6 on 2021-02-13 03:01

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lists', '0002_auto_20210212_1943'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Lists',
            new_name='List',
        ),
    ]
