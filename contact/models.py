from django.db import models

# Create your models here.
class contactDetails(models.Model):
    firstname= models.CharField(max_length=100)
    email= models.EmailField()
    subject=models.CharField(max_length=100)
    comment= models.CharField(max_length=10000)
