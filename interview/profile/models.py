from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class UserProfile(AbstractUser):
    email = models.EmailField(_("email address"), unique=True)

    is_admin = models.BooleanField(_("admin"), default=False)

    avatar = models.ImageField(upload_to='avatars', blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
