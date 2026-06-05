from django.http import HttpResponse
from django.shortcuts import *
from.models import User
from.models import Contact
from.models import Sign

# Create your views here.
def home(request):
    return render(request,"home.html")
def menu(request):
    return render(request,"menu.html")
def north_indian(request):
    return render(request,"nind.html")
def south_indian(request):
    return render(request,"sind.html")
def chinese(request):
    return render(request,"chin.html")
def starters(request):
    return render(request,"starter.html")
def pizzas_burgers(request):
    return render(request,"pizzburg.html")
def dessert(request):
    return render(request,"dessert.html")
def contact_us(request):
    if request.method=='POST':
        a=request.POST.get("name")
        b=request.POST.get("mail")
        c=request.POST.get("phonenumber")
        d=request.POST.get("message")
        e=Contact(name=a,mail=b,phonenumber=c,message=d)
        e.save()
    return render(request,"contactapp.html")
def about_us(request):
    return render(request,"aboutus.html")
def profile(request):
    return render(request,"profrest.html")
def sign_in(request):
    if request.method=='POST':
        a=request.POST.get("sname")
        b=request.POST.get("smail")
        c=request.POST.get("spassword")
        d=request.POST.get("conpass")
        e=Sign(sname=a,smail=b,spassword=c,conpass=d)
        e.save()
    return render(request,"signrest.html")
def log_in(request):
    if request.method=='POST':
        a=request.POST.get("username")
        b=request.POST.get("email")
        c=request.POST.get("password")
        d=User(username=a,email=b,password=c)
        d.save()
    return render(request,"logrest.html")

