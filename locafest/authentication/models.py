# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=40, unique=True)

    name = models.CharField(max_length=50)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'name']

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        if self.name is not None:
            return self.name.split(' ')[0] or self.email
        return self.email
