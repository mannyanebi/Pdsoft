from django.db import models

# Create your models here.
class ContactDetail(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    message = models.TextField(blank=True)