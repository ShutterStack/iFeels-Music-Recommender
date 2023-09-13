from django.db import models

# Create your models here.
class Contact(models.Models):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    sugg_feed = models.TextField()
    date = models.DateField()