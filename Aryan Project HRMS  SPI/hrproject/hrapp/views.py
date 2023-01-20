from django.shortcuts import render, redirect, reverse
from . models import Enquiry, JobSeeker, AdminLogin
import datetime
from django.core.exceptions import ObjectDoesNotExist
from adminzone.models import Notification

# Create your views here.
def index(request):
    nf=Notification.objects.all()
    return render(request,"index.html",{'nf':nf})
def aboutus(request):
    nf=Notification.objects.all()
    return render(request,"aboutus.html",{'nf':nf})
def registration(request):
    nf=Notification.objects.all()
    return render(request,"registration.html",{'nf':nf})
def login(request):
    nf=Notification.objects.all()
    return render(request,"login.html",{'nf':nf})
def contactus(request):
    nf=Notification.objects.all()
    return render(request,"contactus.html",{'nf':nf})
def saveenq(request):
    name=request.POST['name']
    gender=request.POST['gender']
    address=request.POST['address']
    contactno=request.POST['contactno']
    emailaddress=request.POST['emailaddress']
    enquirytext=request.POST['enquirytext']
    enq=Enquiry(name=name,gender=gender,address=address,contactno=contactno,emailaddress=emailaddress,enquirytext=enquirytext)
    enq.save()
    msg='Enquiry is saved.'
    return render(request,"contactus.html",{'msg':msg})
def savejobseeker(request):
    name=request.POST['name']
    gender=request.POST['gender']
    address=request.POST['address']
    contactno=request.POST['contactno']
    emailaddress=request.POST['emailaddress']
    qualification=request.POST['qualification']
    experience=request.POST['experience']
    keyskills=request.POST['keyskills']
    dob=request.POST['dob']
    aadharno=request.POST['aadharno']
    regdate=datetime.datetime.today()
    js=JobSeeker(name=name,gender=gender,address=address,contactno=contactno,emailaddress=emailaddress,qualification=qualification,experience=experience,keyskills=keyskills,dob=dob,aadharno=aadharno,regdate=regdate)
    js.save()
    msg='Registration is done.'
    return render(request,"registration.html",{'msg':msg})
def validateuser(request):
    userid=request.POST['userid']
    password=request.POST['password']
    msg=''
    try:
        obj=AdminLogin.objects.get(userid=userid,password=password)
        if obj is not None:
            request.session['userid']=userid
            return redirect(reverse('adminzone:adminhome'))
    except ObjectDoesNotExist:
        msg='Invalid User'
    return render(request,"login.html",{'msg':msg})




