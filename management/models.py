from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

import datetime


# class Room(models.Model):
#     name = models.CharField(max_length=255)
#     code = models.CharField(max_length=5)


class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True,
    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    ROLES = [(0, "Admin"), (1, "Staff"), (2, "Normal user")]
    # room = models.ForeignKey("Room", on_delete=models.PROTECT)
    role = models.SmallIntegerField(choices=ROLES, null=True, default=2)

    objects = MyUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


class Author(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True)
    date_of_birth = models.DateField(null=True)
    date_of_death = models.DateField(null=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True)
    published_date = models.DateField(null=True)
    author = models.ForeignKey("Author", on_delete=models.PROTECT)
    created_at = models.DateField(default=datetime.date.today())

    STATUSES = [(0, "Pending"), (1, "Published"), (2, "Canceled")]
    status = models.SmallIntegerField(default=0, choices=STATUSES)

    def __str__(self):
        return self.name


class Genere(models.Model):
    name = models.CharField(max_length=255)


class GenegeBook(models.Model):
    book = models.ForeignKey("Book", on_delete=models.SET_NULL, null=True)
    genere = models.ForeignKey("Genere", on_delete=models.SET_NULL, null=True)
    number_of_book = models.SmallIntegerField(default=0)
