from django import forms
from .models import *
from django.utils.translation import gettext_lazy as _

class AttackForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ('attacker_num', 'defender')
        labels = {
            'attacker_num': _('내가 고른 카드'),
            'defender': _('공격할 상대는?'),
        }

class DefendForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['defender_num']
        labels = {
            'defender_num': _('내가 고른 카드(defend)'),
        }