from django.contrib.auth.models import User
from django.db import models


class Company(models.Model):
    user = models.OneToOneField(User, related_name='company', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, null=True)
    website = models.CharField(max_length=100, null=True)
    creation_date = models.DateField('creation date')
    about = models.CharField(max_length=200, null=True)
    address = models.TextField(max_length=200)
    telephone_number = models.PositiveIntegerField()

    class Meta:
        ordering = ['name']
