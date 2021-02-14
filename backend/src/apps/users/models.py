from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


# Create user manager
class User_manager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('User must have an email address to register')

        user = self.model(email=self.normalize_email(email))

        user.set_password(password)  # Password is hashed, so needs to saved separately
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(email, password=password)
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user


# Create user model
class User(AbstractBaseUser):
    email = models.EmailField(verbose_name='Email address',
                              max_length=255, unique=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = User_manager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True


class User_profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='profile_images')

    linkedin_profile = models.CharField(max_length=200)
    website = models.CharField(max_length=200)

    def __str__(self):
        return self.first_name


