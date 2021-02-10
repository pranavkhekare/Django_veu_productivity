# Generated by Django 3.1.6 on 2021-02-10 21:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_is_staff'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_profile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='users.user')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='profile_images')),
                ('linkedin_profile', models.CharField(max_length=200)),
                ('website', models.CharField(max_length=200)),
            ],
        ),
    ]
