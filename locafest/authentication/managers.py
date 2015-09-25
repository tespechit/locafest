# -*- coding: utf-8 -*-

from django.contrib.auth.models import BaseUserManager
from django.utils.translation import ugettext as _


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        if not email:
            raise ValueError(_("Users must have a valid email address."))

        if not kwargs.get('username'):
            raise ValueError(_("Users must have a valid username."))

        account = self.model(
            email=self.normalize_email(email), username=kwargs.get('username')
        )

        account.set_password(password)
        account.save()

        return account

    def create_superuser(self, email, password, **kwargs):
        account = self.create_user(email, password, **kwargs)

        account.is_admin = True
        account.save()

        return account
