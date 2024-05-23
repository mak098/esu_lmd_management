from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def home(request):
    return render(request,'auth-login.html')

@login_required
def index(request):
    return render(request,'index.html')
    

def signin(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect("dashbord")
        else:
            messages.error(request,"nom d\'utilisateur ou mot de pass incorrect")
    return render(request, 'auth-login.html',locals())

@login_required
def signout(request):
    logout(request)
    return redirect('signin')