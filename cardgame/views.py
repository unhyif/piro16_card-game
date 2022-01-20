from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
def signup(request):
    if request.method == "POST":
        if request.POST["password"] == request.POST["password2"]:
            user = User.objects.create_user(
                username = request.POST["username"],
                password = request.POST["password1"]
            )
            auth.login(request, user)
            return redirect('/')
        return render(request, 'cardgame/signup.html')
    return render(request, 'cardgame/signup.html')

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('main')
        else:
            return render(request, 'cardgame/login.html', {'error':'username or password is incorrect'})
    else:
        return render(request, 'cardgame/login.html')

def logout(request):
    auth.logout(request)
    return redirect('main_ready')

def main_ready(request):
    return render(request, 'cardgame/main_ready.html')    

def main(request):
    return render(request, 'cardgame/main.html')