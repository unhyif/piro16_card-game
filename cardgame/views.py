from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *
from random import *

def loginuser(request):
    return Profile.objects.get(user=request.user)


# Authentication

def signup(request):
    if request.method == "POST":
        if request.POST.get("password1") == request.POST.get("password2"):
            user = User.objects.create_user(
                username = request.POST.get("username"),
                password = request.POST.get("password1")
            )
            Profile.objects.create(user=user)
            auth.login(request, user)
            return redirect('/')
        return render(request, 'cardgame/signup.html')
    return render(request, 'cardgame/signup.html')

def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return render(request, 'cardgame/main.html', {'user':user})
        else:
            return render(request, 'cardgame/login.html', {'error':'username or password is incorrect'})
    else:
        return render(request, 'cardgame/login.html')

def logout(request):
    auth.logout(request)
    return redirect('cardgame:main_ready')

def main_ready(request):
    return render(request, 'cardgame/main_ready.html')    

def main(request):
    return render(request, 'cardgame/main.html')


# Game

def attack(request):
    if request.method == "POST":
        rule_list = ["BIG", "SMALL"]
        chosen_rule = choice(rule_list)

        game = Game(attacker=loginuser(request), rule=chosen_rule) # Game object 생성
        form = AttackForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect("cardgame:detail", game.id)

    else:
        form = AttackForm()
        form.fields["defender"].queryset = Profile.objects.all().exclude(user=request.user)
        return render(request, "cardgame/attack.html", {"form":form})

def detail(request, pk):
    game = get_object_or_404(Game, id=pk)
    
    if loginuser(request) == game.attacker:
        attacker_in = True # 로그인한 유저가 attacker
    else:
        attacker_in = False # 로그인한 유저가 defender
    return render(request, "cardgame/detail.html", {"game":game, "attacker_in":attacker_in})
        # templete에서 {% if attacker_in %} {% else %} 를 통해, 게임 정보를 서술할 때 "나"의 입장이 attacker 입장인지 defender 입장인지 식별 가능함

def delete(request, pk):
   game = get_object_or_404(Game, id=pk)
   game.delete()
   return redirect('cardgame:main')
      # !!!!! list 페이지 만들고나서 redirect 수정하기

def defend(request, pk):
    game = get_object_or_404(Game, id=pk)

    if request.method == "POST":
        form = DefendForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            game_win(game)
            return redirect("cardgame:detail", pk=game.id)

    else:
        form = DefendForm()
        return render(request, "cardgame/defend.html", {"form":form})

def game_win(game):
    if game.rule == 'BIG':
        if game.attacker_num > game.defender_num:
            game.winner = game.attacker
            game.attacker.score += game.attacker_num
            game.defender.score -= game.defender_num
            game.save()
            game.attacker.save()
            game.defender.save()
        
        elif game.attacker_num == game.defender_num:
            game.winner = None
            game.save()
            game.attacker.save()
            game.defender.save()

        else:
            game.winner = game.defender
            game.attacker.score -= game.attacker_num
            game.defender.score += game.defender_num
            game.save()
            game.attacker.save()
            game.defender.save()

    else:
        if game.attacker_num < game.defender_num:
            game.winner = game.attacker
            game.attacker.score += game.attacker_num
            game.defender.score -= game.defender_num
            game.save()
            game.attacker.save()
            game.defender.save()
        
        elif game.attacker_num == game.defender_num:
            game.winner = None
            game.save()
            game.attacker.save()
            game.defender.save()

        else:
            game.winner = game.defender
            game.attacker.score -= game.attacker_num
            game.defender.score += game.defender_num
            game.save()
            game.attacker.save()
            game.defender.save()