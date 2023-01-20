from django.db import models

# Create your models here.
class Notification(models.Model):
    notificationtext=models.CharField(max_length=200)
    notificationdate=models.CharField(max_length=30)
class Employee(models.Model):
    empid=models.IntegerField(primary_key=True)
    empname=models.CharField(max_length=50)
    gender=models.CharField(max_length=6)
    address=models.TextField()
    contactno=models.CharField(max_length=15)
    emailaddress=models.EmailField(max_length=50)
    doj=models.CharField(max_length=30)
    department=models.CharField(max_length=50)
    designation=models.CharField(max_length=50)
    panno=models.CharField(max_length=10)
    aadharno=models.CharField(max_length=12)
    salary=models.IntegerField()
