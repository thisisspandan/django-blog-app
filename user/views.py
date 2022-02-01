from django.shortcuts import render,redirect
from .forms import RegisterForm,LoginForm
from django.contrib import messages
from django.conf import settings
from user.models import User
from django.contrib.auth import login,authenticate,logout



# Create your views here.

def register(request):
    
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        email = form.cleaned_data.get("email")
        phone = form.cleaned_data.get("phone")

        newUser = User(username =username, email=email, phone=phone)
        newUser.set_password(password)

        newUser.save()
        login(request,newUser)
        messages.success(request,"Successfully Registered...")

        return redirect("index")
    context = {
            "form" : form
        }
    return render(request,"register.html",context)

    
    
def loginUser(request):
    form = LoginForm(request.POST or None)

    context = {
        "form":form
    }

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username = username,password = password)

        if user is None:
            messages.info(request,"Incorrect Username/Password")
            return render(request,"login.html",context)

        messages.success(request,"You have successfully logged in")
        login(request,user)
        return redirect("index")
    return render(request,"login.html",context)

def logoutUser(request):
    logout(request)
    messages.success(request,"Successfully logged out")
    return redirect("index")

