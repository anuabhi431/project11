from django.db import models

class RegModel(models.Model):
    FName=models.CharField(max_length=10)
    LName=models.CharField(max_length=10)
    UName=models.CharField(max_length=10)
    Password=models.CharField(max_length=10)
    CPassword=models.CharField(max_length=10)
    Email=models.EmailField()
    Mobo=models.CharField(max_length=10)

# Create your models here.
