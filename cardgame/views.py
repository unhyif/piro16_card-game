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
            return redirect('cardgame:main_ready')
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
    return render(request, "cardgame/detail.html", {"game":game, "attacker_in":attacker_in, "status":status(pk)})

def delete(request, pk):
   game = get_object_or_404(Game, id=pk)
   game.delete()
   return redirect('cardgame:list')

def defend(request, pk):
    game = get_object_or_404(Game, id=pk)

    if request.method == "POST":
        form = DefendForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            get_winner(game)
            return redirect("cardgame:detail", pk=game.id)

    else:
        form = DefendForm()
        return render(request, "cardgame/defend.html", {"form":form})


def get_winner(game):
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

        else:
            game.winner = game.defender
            game.attacker.score -= game.attacker_num
            game.defender.score += game.defender_num
            game.save()
            game.attacker.save()
            game.defender.save()


def status(pk):
    game = get_object_or_404(Game, id=pk)
    
    if not game.defender_num: # 공격만 한 상태
        return 1
    else: # 승패 난 상태
        return 2

def ranking(request):
    users = Profile.objects.all().order_by('-score')
    index = users.count
    ctx = {'users':users, 'index':index}

    return render(request, template_name='cardgame/ranking.html', context=ctx)


# def list(request):
#     related_games = loginuser(request).attack.all().union(loginuser(request).defend.all())
#     return render(request, "cardgame/list.html", {"related_games":related_games, })  

def list(request):
    user=request.user
    game = Game.objects.all()
    ctx = {'game': game,'user': user}
    return render(request, "cardgame/list.html", context=ctx)