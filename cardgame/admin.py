from django.contrib import admin
from .models import *

admin.site.register(Profile)
@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    search_fields = ['attacker__user__username', 'defender__user__username', 'winner__user__username']
