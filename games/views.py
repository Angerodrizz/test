from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse
from django.db.models import Sum
from django.contrib import messages
from .models import games

def index(request):
    return render(request,"games/index.html")

def register(request): 
    if request.method == "POST":
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        password2=request.POST['password2']
        if not password==password2:
            messages.warning(request, 'Passswords do not match, please try again.')
            return render(request,'orders/registration.html')
        user=User.objects.create_user(username, email, password)
        user.first_name=first_name
        user.last_name=last_name
        user.save()
        messages.success(request, f'{username}, your user has been created. Please, log in!')
        return render(request, 'games/login.html')   
    return render(request,'games/registration.html')

def login_u(request):
    if request.method == "POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password) 
        if user is not None:
            login(request,user)
            return HttpResponseRedirect(reverse("index"))
        else:
            messages.warning(request,'Invalid credentials, please try again')
            return render(request,"games/login.html") 
    return render(request,"games/login.html")     
    
def logout_u(request):
    logout(request)
    messages.warning(request,'Logged out.')
    return render(request,"games/index.html")



def menu(request):
    context = {
        "games": games.objects.all(),
    }
        
    return render(request,"games/games.html", context)
