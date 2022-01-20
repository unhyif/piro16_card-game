from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *
from random import *

def attack(request):
    if request.method == "POST":
        rule_list = ["BIG", "SMALL"]
        chosen_rule = choice(rule_list)

        # game = Game(attacker=request.user, rule=chosen_rule)
        game = Game(attacker=User.objects.get(id=1), rule=chosen_rule) # Game object 생성
        form = AttackForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect("cardgame:detail", game.id) # 게임 디테일 보여줄 건지 전적 보여줄 건지??

    else:
        form = AttackForm()
        form.fields["defender"].queryset = User.objects.all().exclude(id=1) # request.id
        return render(request, "cardgame/attack.html", {"form":form})


def detail(request, pk):
    game = get_object_or_404(Game, id=pk)
    
    # if request.user == game.attacker:
    if User.objects.get(id=1) == game.attacker:
        attacker_in = True # 로그인한 유저가 attacker
    else:
        attacker_in = False # 로그인한 유저가 defender
    return render(request, "cardgame/detail.html", {"game":game, "attacker_in":attacker_in})
        # templete에서 {% if attacker_in %} {% else %} 를 통해, 게임 정보를 서술할 때 "나"의 입장이 attacker 입장인지 defender 입장인지 식별 가능함