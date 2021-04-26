from django.db import models


class Chapter(models.Model):
    number = models.PositiveIntegerField()
    name = models.CharField(max_length=100)
