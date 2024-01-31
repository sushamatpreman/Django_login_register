from django.db import models

# Create your models here.
class category(models.Model):
    firstname = models.CharField(max_length=200,null=True,blank=True)
    lastname = models.CharField(max_length=200,null=True)
    email = models.CharField(max_length=200,null=True)
    phonenumber = models.IntegerField(null=True)
    password = models.CharField(max_length=200,null=True)
    confirmpassword = models.CharField(max_length=200,null=True)
    gender = models.CharField(max_length=200,null=True)



