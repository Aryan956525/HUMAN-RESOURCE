from django.urls import path
from . import views

urlpatterns=[
    path('adminhome/',views.adminhome,name='adminhome'),
    path('enquiry/',views.enquiry,name='enquiry'),
    path('jobseeker/',views.jobseeker,name='jobseeker'),
    path('employee/',views.employee,name='employee'),
    path('changepassword/',views.changepassword,name='changepassword'),
    path('logout/',views.logout,name='logout'),
    path('addnotification/',views.addnotification,name='addnotification'),
    path('deletenotification/?P<id>\d+',views.deletenotification,name='deletenotification'),
    path('deleteenquiry/?P<id>\d+',views.deleteenquiry,name='deleteenquiry'),
    path('deletejobseeker/?P<emailaddress>\s+',views.deletejobseeker,name='deletejobseeker'),
    path('saveemployee/',views.saveemployee,name='saveemployee'),
    path('deleteemployee/P<empid>\d+',views.deleteemployee,name='deleteemployee'),
    path('changepwd/',views.changepwd,name='changepwd'),
    path('updateemployee/?P<empid>\d+',views.updateemployee,name='updateemployee'),
    path('updateemp/',views.updateemp,name='updateemp'),
]