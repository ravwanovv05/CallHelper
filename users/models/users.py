from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from users.models.managers import CustomUserManager
from django.db import models


class User(AbstractUser):
    username = models.CharField(
        'Имя пользователя', max_length=64, unique=True, null=False, blank=False
    )
    email = models.EmailField('Почта', unique=True, null=False, blank=False)
    phone_number = PhoneNumberField('Номер телефона', unique=True, null=False, blank=False)

    USERNAME_FIELD = 'username'
    # REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
