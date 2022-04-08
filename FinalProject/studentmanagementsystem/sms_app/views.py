from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'sms/index.html')


def adminlogin(request):
    return render(request,'sms/adminlogin.html')

def studentlogin(request):
    return render(request,'sms/studentlogin.html')

def resetpassword(request):
    return render(request,'sms/resetpassword.html')

def dashboard(request):
    return render(request,'sms/admindashboard.html')




# for Student dashboard
def studentdashboard(request):
    return render(request,'sms/studentdashboard/dashboard.html')

def result(request):
    return render(request,'sms/studentdashboard/result.html')
    
