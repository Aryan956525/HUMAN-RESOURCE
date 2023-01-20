from django.db import models

# Create your models here.
class Enquiry(models.Model):
    name=models.CharField(max_length=50)
    gender=models.CharField(max_length=6)
    address=models.CharField(max_length=200)
    contactno=models.CharField(max_length=15)
    emailaddress=models.EmailField(max_length=50)
    enquirytext=models.CharField(max_length=500)
class JobSeeker(models.Model):
    name=models.CharField(max_length=50)
    gender=models.CharField(max_length=6)
    address=models.CharField(max_length=200)
    contactno=models.CharField(max_length=15)
    emailaddress=models.EmailField(max_length=50,primary_key=True)
    qualification=models.CharField(max_length=50)
    experience=models.CharField(max_length=10)
    keyskills=models.CharField(max_length=200)
    dob=models.CharField(max_length=30)
    aadharno=models.CharField(max_length=12)
    regdate=models.CharField(max_length=30)
class AdminLogin(models.Model):
    userid=models.CharField(max_length=50,primary_key=True)
    password=models.CharField(max_length=20)









