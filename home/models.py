from django.db import models

# Create your models here.
class task(models.Model):
    Task = models.CharField(max_length=30)
    Task_Description = models.TextField()
    Time =models.DateTimeField(auto_now_add=True)
class contactuser(models.Model):
    Name = models.CharField(max_length=30) 
    Address=models.CharField(max_length=50)
    Description = models.CharField(max_length=30)
    Email=models.EmailField()
    Time=models.DateTimeField(auto_now_add=True)
