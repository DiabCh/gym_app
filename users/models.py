from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.translation import gettext_lazy as _


# We interact with AuthUser through AuthUserManager

class AuthUserManager(BaseUserManager):
    def create_user(self, email, password, first_name, last_name
                    ):
        if not email:
            raise ValueError ('Users must have an email address')
        if not first_name:
            raise ValueError ('Users must have a fname')
        if not last_name:
            raise ValueError ('Users must have a lname')
        if not password:
            raise ValueError('Users must have a password')
        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(
            self, email, password, first_name, last_name
    ):

        user = self.create_user(email, password, first_name, last_name)
        user.is_staff = True
        user.is_superuser = True

        user.save(using=self._db)

        return user


# Base Auth User model can either inherent AbstractUser for django's base
# settings or BaseAbstractUser to be written from the ground up.
class AuthUser(AbstractUser):
    username = None
    first_name = models.CharField(verbose_name=_('first name'), max_length=150, null=False)
    last_name = models.CharField(verbose_name=_('last name'), max_length=150, null=False)
    email = models.EmailField(verbose_name=_('email address'), unique=True, null=False)
    password = models.CharField(verbose_name=_('password'), max_length=128, null=True, default=None)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = AuthUserManager()

    def __str__(self):
        return self.email

    def __repr__(self):
        return self.__str__()