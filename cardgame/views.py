from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *
from random import *

# Authentication

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


# Game

def attack(request):
    if request.method == "POST":
        rule_list = ["BIG", "SMALL"]
        chosen_rule = choice(rule_list)

        game = Game(attacker=request.user, rule=chosen_rule) # Game object 생성
        form = AttackForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect("cardgame:detail", game.id) # 게임 디테일 보여줄 건지 전적 보여줄 건지??

    else:
        form = AttackForm()
        form.fields["defender"].queryset = User.objects.all().exclude(id=request.user.id)
        return render(request, "cardgame/attack.html", {"form":form})

def detail(request, pk):
    game = get_object_or_404(Game, id=pk)
    
    if request.user == game.attacker:
        attacker_in = True # 로그인한 유저가 attacker
    else:
        attacker_in = False # 로그인한 유저가 defender
    return render(request, "cardgame/detail.html", {"game":game, "attacker_in":attacker_in})
        # templete에서 {% if attacker_in %} {% else %} 를 통해, 게임 정보를 서술할 때 "나"의 입장이 attacker 입장인지 defender 입장인지 식별 가능함