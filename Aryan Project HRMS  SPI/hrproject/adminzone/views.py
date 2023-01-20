from django.shortcuts import render, redirect
from . models import Notification, Employee
import datetime
from hrapp.models import Enquiry, JobSeeker, AdminLogin

# Create your views here.
def adminhome(request):
    try:
        if request.session['userid'] is not None:
            nf=Notification.objects.all()
            return render(request,"adminhome.html",{'nf':nf})
    except:
        return render(request,"login.html")
def enquiry(request):
    try:
        if request.session['userid'] is not None:
            enq=Enquiry.objects.all()
            return render(request,"enquiry.html",{'enq':enq})
    except:
        return render(request,"login.html")
def jobseeker(request):
    try:
        if request.session['userid'] is not None:
            js=JobSeeker.objects.all()
            return render(request,"jobseeker.html",{'js':js})
    except:
        return render(request,"login.html")
def employee(request):
    try:
        if request.session['userid'] is not None:
            emp=Employee.objects.all()
            return render(request,"employee.html",{'emp':emp})
    except:
        return render(request,"login.html")
def changepassword(request):
    try:
        if request.session['userid'] is not None:
            return render(request,"changepassword.html")
    except:
        return render(request,"login.html")
def logout(request):
    request.session['userid']=None
    return render(request,"login.html")
def addnotification(request):
    notificationtext=request.POST['notificationtext']
    notificationdate=datetime.datetime.today()
    nf=Notification(notificationtext=notificationtext,notificationdate=notificationdate)
    nf.save()
    return redirect('adminzone:adminhome')
def deletenotification(request,id):
    nf=Notification.objects.get(id=id)
    nf.delete()
    return redirect('adminzone:adminhome')
def deleteenquiry(request,id):
    enq=enquiry.objects.get(id=id)
    enq.delete()
    return redirect('adminzone:enquiry')
def deletejobseeker(request,emailaddress):
    js=JobSeeker.objects.get(emailaddress=emailaddress)
    js.delete()
    return redirect('adminzone:jobseeker')
def saveemployee(request):
    empid=request.POST['empid']
    empname=request.POST['empname']
    gender=request.POST['gender']
    address=request.POST['address']
    contactno=request.POST['contactno']
    emailaddress=request.POST['emailaddress']
    doj=request.POST['doj']
    department=request.POST['department']
    designation=request.POST['designation']
    panno=request.POST['panno']
    aadharno=request.POST['aadharno']
    salary=request.POST['salary']
    emp=Employee(empid=empid,empname=empname,gender=gender,address=address,contactno=contactno,emailaddress=emailaddress,doj=doj,department=department,designation=designation,panno=panno,aadharno=aadharno,salary=salary)
    emp.save()
    return redirect('adminzone:employee')
def deleteemployee(request,empid):
    emp=Employee.objects.get(empid=empid)
    emp.delete()
    return redirect('adminzone:employee')
def changepwd(request):
    userid=request.session['userid']
    oldpassword=request.POST['oldpassword']
    newpassword=request.POST['newpassword']
    confirmpassword=request.POST['confirmpassword']
    msg=''
    if(newpassword!=confirmpassword):
        msg='Newpassword and confirmpassword are not matched.'
        return render(request,"changepassword.html",{'msg':msg})
    user=AdminLogin.objects.get(userid=userid,password=oldpassword)
    if user is not None:
        ad=AdminLogin(userid=userid,password=newpassword)
        ad.save()
        return redirect('adminzone:logout')
    else:
        msg='old password is not matched.'
        return render(request,"changepassword.html",{'msg':msg})
def updateemployee(request,empid):
    emp=Employee.objects.get(empid=empid)
    return render(request,"updateemployee.html",{'emp':emp})
def updateemp(request):
    empid=request.POST['empid']
    empname=request.POST['empname']
    gender=request.POST['gender']
    address=request.POST['address']
    contactno=request.POST['contactno']
    emailaddress=request.POST['emailaddress']
    doj=request.POST['doj']
    department=request.POST['department']
    designation=request.POST['designation']
    panno=request.POST['panno']
    aadharno=request.POST['aadharno']
    salary=request.POST['salary']
    emp=Employee(empid=empid,empname=empname,gender=gender,address=address,contactno=contactno,emailaddress=emailaddress,doj=doj,department=department,designation=designation,panno=panno,aadharno=aadharno,salary=salary)
    emp.save()
    return redirect('adminzone:employee')