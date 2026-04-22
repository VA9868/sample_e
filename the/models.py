from django.db import models

# Create your models here.
class student(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    gender=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email=models.EmailField()
    
    def __str__(self):
        return self.name

class college(models.Model):
    department=models.CharField(max_length=100)
    mark=models.IntegerField()
    subject=models.CharField(max_length=100)
    roomno=models.IntegerField()
    rollno=models.IntegerField()
 
    def __str__(self):
        return self.department


    