from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from users.models.managers import CustomUserManager
from django.db import models


class User(AbstractUser):
    phone_number = PhoneNumberField('Номер телефона', unique=True)

    # USERNAME_FIELD = 'phone_number'
    # REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
