from tkinter import CASCADE
from django.conf import settings
from django.db import models
from random import *
from django.contrib.auth.models import User

# User model

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    score = models.IntegerField(default = 0)

    def __str__(self):
        return self.user.username


# Game model

class Game(models.Model):

    five_nums1, five_nums2 = [], [] # 해결 필요... views.py에서 해야 할 듯
    for i in range(5):
        ran = randint(1,10)
        while ran in five_nums1:
            ran = randint(1,10)
        five_nums1.append(ran)
        five_nums1.sort()
    for i in range(5):
        ran = randint(1,10)
        while ran in five_nums2:
            ran = randint(1,10)
        five_nums2.append(ran)
        five_nums2.sort()

    NUM_CHOICE1 = [(n, n) for n in five_nums1] # for attacker
    NUM_CHOICE2 = [(n, n) for n in five_nums2] # for defender

    RULE_CHOICE = [("BIG","BIG"), ("SMALL","SMALL")]


    attacker = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="attack", verbose_name="공격자")
    # related_name: ex) attacker가 user인 Games
    defender = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="defend", verbose_name="수비자", blank=True)
    # related_name: ex) defender가 user인 Games -> request.user.attack.all() 과 request.user.defend.all() 합친 queryset의 .objects.all()을 전적 페이지 template에 전달
    attacker_num = models.IntegerField("공격자 선택", choices=NUM_CHOICE1, blank=True)
    defender_num = models.IntegerField("수비자 선택", choices=NUM_CHOICE2, blank=True, null=True)

    rule = models.CharField("승리 룰", choices=RULE_CHOICE, max_length=5, blank=True)
    winner = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name="승자", blank=True, null=True)

    def __str__(self):
        return f"{self.id} - {self.attacker.user.username} VS {self.defender.user.username}"
