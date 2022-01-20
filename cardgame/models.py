from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

# class UserList(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     score = models.IntegerField(default = 0)

#     def __str__(self):
#         return self.user.username

# class Attack(models.Model):
#     # 한명의 유저가 여러 게임을 진행할 수 있음
#     # 회원가입을 통해 생성된 유저가 user 변수로 들어옴.
#     attack_user = models.ForeignKey(UserList, on_delete=models.CASCADE, default='admin', related_name='attack_user')
#     defense_user = models.ForeignKey(UserList, on_delete=models.CASCADE, related_name='defense_user')

#     attack_num = models.IntegerField(null=True, blank=True ,choices=CARD_CHOICES)
#     defense_num = models.IntegerField(null=True, blank=True, choices=CARD_CHOICES)

#     def __str__(self):
#         return self.user
