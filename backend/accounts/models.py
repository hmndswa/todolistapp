from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    phone_number  = models.CharField(max_length=20, blank=True)

    #Avoid duplicates
    email = models.EmailField(unique=True)

