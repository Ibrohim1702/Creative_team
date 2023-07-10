from django.db import models

# Create your models here.


class Contact(models.Model):
    email = models.CharField(max_length=128)
    password = models.CharField(max_length=20)
    message = models.TextField()

    def __str__(self):
        return self.email