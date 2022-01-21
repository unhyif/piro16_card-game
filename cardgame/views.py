from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *
from random import *

def login_user(request): # 로그인 중인 Profile object
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

def main_ready(request): # 로그인 안 됐을 때 홈화면
    return render(request, 'cardgame/main_ready.html')    

def main(request): # 로그인 됐을 때 홈화면
    return render(request, 'cardgame/main.html')



# Game

def attack(request): # 공격하기 누르면 Game object 생성
    if request.method == "POST":
        chosen_rule = choice(["BIG", "SMALL"])

        game = Game(attacker=login_user(request), rule=chosen_rule) # attacker가 login_user이고, 랜덤으로 choice된 rule을 가진 Game
        form = AttackForm(request.POST, instance=game) # form에 해당하는 instance를 방금 만든 game으로 지정
        if form.is_valid():
            form.save() # form에 담긴 정보가 game에게 전달
            return redirect("cardgame:detail", game.id)

    else:
        form = AttackForm() # attacker_num, defender만 field로 가진 form
        form.fields["defender"].queryset = Profile.objects.all().exclude(user=request.user) # 자기 자신 제외한 유저 목록
        return render(request, "cardgame/attack.html", {"form":form})

def detail(request, pk):
    game = get_object_or_404(Game, id=pk)
    return render(request, "cardgame/detail.html", {"game":game, "login_user":login_user(request)})

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
            get_winner(game) # game의 모든 field 채워짐
            return redirect("cardgame:detail", pk=game.id)

    else:
        form = DefendForm() # defender_num만 field로 가진 form
        return render(request, "cardgame/defend.html", {"form":form})

def get_winner(game):
    if game.rule == "BIG":
        if game.attacker_num > game.defender_num:
            game.winner = game.attacker
            game.attacker.score += game.attacker_num
            game.defender.score -= game.defender_num
        
        elif game.attacker_num == game.defender_num:
            game.winner = None

        else:
            game.winner = game.defender
            game.attacker.score -= game.attacker_num
            game.defender.score += game.defender_num

    else:
        if game.attacker_num < game.defender_num:
            game.winner = game.attacker
            game.attacker.score += game.attacker_num
            game.defender.score -= game.defender_num
        
        elif game.attacker_num == game.defender_num:
            game.winner = None

        else:
            game.winner = game.defender
            game.attacker.score -= game.attacker_num
            game.defender.score += game.defender_num

    game.save()
    game.attacker.save()
    game.defender.save()

def ranking(request):
    users = Profile.objects.all().order_by('-score')
    index = users.count
    ctx = {'users':users, 'index':index}
    return render(request, template_name='cardgame/ranking.html', context=ctx)

def list(request):
    related_games = login_user(request).attack.all().union(login_user(request).defend.all())
    return render(request, "cardgame/list_copy.html", {"related_games":related_games, "login_user":login_user(request)})  


# def list(request):
#     user=request.user
#     game = Game.objects.all()
#     ctx = {'game': game,'user': user}
#     return render(request, "cardgame/list.html", context=ctx)