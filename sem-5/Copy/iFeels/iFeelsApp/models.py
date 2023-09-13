from django.db import models

# Create your models here.
class Contact(models.Models):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.TextField(max_Length=10)
    sugg_feed = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name