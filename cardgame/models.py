from tkinter import CASCADE
from django.db import models
from random import *

class Game(models.Model): # ModelForm 만들 때 field 수동으로 설정 (not "__all__")

    five_nums1, five_nums2 = [], []
    for i in range(5):
        ran = randint(1,10)
        while ran in five_nums1:
            ran = randint(1,10)
        five_nums1.append(ran) # 중복되지 않는 5개의 숫자
        five_nums1.sort()
    for i in range(5):
        ran = randint(1,10)
        while ran in five_nums1:
            ran = randint(1,10)
        five_nums2.append(ran)
        five_nums2.sort()

    NUM_CHOICE1 = [(n, n) for n in five_nums1] # for attacker, 리스트 요소가 tuple 이여야 하므로
    NUM_CHOICE2 = [(n, n) for n in five_nums2] # for defender

    RULE_CHOICE = [("BIG","BIG"), ("SMALL","SMALL")]


    attacker = models.ForeignKey(User, on_delete=models.CASCADE, related_name="attack", verbose_name="공격자") # "공격하기" 누르면 views.py에서 request.user로 설정(form으로 선택받지 않음)
    # related_name: ex) attacker가 user인 Games
    defender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="defend", verbose_name="수비자", blank=True) # forms.py에서 label="공격할 상대는?", field 값 목록에서 attacker exclude 하기
    # related_name: ex) defender가 user인 Games -> request.user.attack.all() 과 request.user.defend.all() 합친 queryset의 .objects.all()을 전적 페이지 template에 전달
    attacker_num = models.IntegerField("공격자 선택", choices=NUM_CHOICE1, blank=True) # label="내가 고른 카드"
    defender_num = models.IntegerField("수비자 선택", choices=NUM_CHOICE2, blank=True, null=True) # label="내가 고른 카드"

    rule = models.CharField("승리 룰", choices=RULE_CHOICE, max_length=5, blank=True) # "공격하기" 누르면 views.py에서 random choice로 ["BIG", "SMALL"] 골라서 field 값 채워줌(form으로 선택받지 않음)
    winner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="승자", blank=True, null=True) # "반격하기" 누르면 views.py에서 rule과 각자의 num에 따라 field 값 채워줌

    def __str__(self):
        return f"{self.id} - {self.attacker.name} VS {self.defender.name}"