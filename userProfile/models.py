from django.contrib.auth.models import AbstractUser
from django.db import models


class UserProfile(AbstractUser):
    firstName = models.CharField("First Name", max_length=240)
    lastName = models.CharField("Last Name", max_length=240)
    email = models.EmailField()
    password =  models.CharField("Password", max_length=240)
    document = models.CharField("Document", max_length=20)
    phone = models.CharField(max_length=20)
    last_login = models.DateTimeField("Last Login", auto_now_add=True)
    registrationDate = models.DateTimeField("Registration Date", auto_now_add=True)
    is_superuser = models.BooleanField(default=False)

    def __str__(self):
        return self.firstName
