from django.contrib import admin
from .models import *

admin.site.register(User)
@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ['attacker', 'defender', 'winner']
    list_display_links = ['attacker', 'defender', 'winner']
    search_fields = ['attacker__name', 'defender__name', 'winner__name']