from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.mail import send_mail
from django.db import models
from django.contrib.auth.models import Group
from django.db.models.signals import post_save
from django.dispatch import receiver

from django.urls import reverse

from .managers import CustomUserManager


# Authentication


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField('Ник', max_length=50)
    email = models.EmailField('Адрес электронной почты', unique=True)

    date_joined = models.DateTimeField('Дата регистрации', auto_now_add=True)
    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.email}"

    class Meta:
        verbose_name = 'Аккаунт'
        verbose_name_plural = 'Аккаунты'


    def email_user(self, subject, message, from_email=None, **kwargs):
        '''
        Sends an email to this User.
        '''
        send_mail(subject, message, from_email, [self.email], **kwargs)
