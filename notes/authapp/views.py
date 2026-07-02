from django.shortcuts import render,redirect
from authapp.models import *
from django.core.mail import send_mail
# Create your views here.

def signup(request):
    if request.method=='POST':
        username=request.POST.get("username")
        password=request.POST.get("password")
        email=request.POST.get("email")

        User.objects.create(username=username,password=password,email=email)

        return redirect('login')
    
    return render(request,'signup_system.html')

def login(request):
    if request.method=='POST':
        username=request.POST.get("username")
        password=request.POST.get("password")
        email=request.POST.get("email")

        user=User.objects.filter(username=username,password=password,email=email).first()

        if user:

            request.session["user_id"]=user.id
            return redirect('home_create_notes')
        
    return render(request,'login_system.html')

def logout(request):
    request.session.flush()
    return redirect('login')

def delete_account(request):
    user_id=request.session.get('user_id')
    user=User.objects.get(id=user_id)

    user.delete()
    return redirect('signup')




