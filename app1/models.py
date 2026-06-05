from django.db import models

# Create your models here.
class User(models.Model):
    username=models.CharField(max_length=30)
    email=models.CharField(max_length=40)
    password=models.CharField(max_length=30)

class Contact(models.Model):
    name=models.CharField(max_length=30)
    mail=models.CharField(max_length=40)
    phonenumber=models.CharField(max_length=20)
    message=models.CharField(max_length=500)

class Sign(models.Model):
    sname=models.CharField(max_length=30)
    smail=models.CharField(max_length=40)
    spassword=models.CharField(max_length=30)
    conpass=models.CharField(max_length=30)